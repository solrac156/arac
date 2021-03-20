from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api
from flask_uploads import patch_request_class, configure_uploads
from marshmallow import ValidationError

from blacklist import BLACKLIST
from db import db
from libs.image_helper import IMAGE_SET
from ma import ma
from oa import oauth
from resources.confirmation import Confirmation, ConfirmationByUser
from resources.github_login import GithubLogin, GithubAuthorize
from resources.image import ImageUpload, Image, AvatarUpload, Avatar
from resources.item import Item, ItemList
from resources.language import Language
from resources.order import Order
from resources.store import Store, StoreList
from resources.user import (
    UserRegister,
    User,
    UserLogin,
    TokenRefresh,
    UserLogout,
    SetPassword,
)

app = Flask(__name__)
load_dotenv(".env", verbose=True)
app.config.from_object("default_config")
app.config.from_envvar("APPLICATION_SETTINGS")
patch_request_class(app, 10 * 1024 * 1024)
configure_uploads(app, IMAGE_SET)
api = Api(app)
jwt = JWTManager(app)
db.init_app(app)
ma.init_app(app)
oauth.init_app(app)
migrate = Migrate(app, db)


@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token["jti"] in BLACKLIST


api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(User, "/user/<int:user_id>")
api.add_resource(UserLogin, "/login")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(UserLogout, "/logout")
api.add_resource(Confirmation, "/user_confirmation/<string:confirmation_id>")
api.add_resource(ConfirmationByUser, "/confirmation/user/<int:user_id>")
api.add_resource(Language, "/language/<string:locale>")
api.add_resource(ImageUpload, "/upload/image")
api.add_resource(Image, "/image/<string:filename>")
api.add_resource(AvatarUpload, "/upload/avatar")
api.add_resource(Avatar, "/avatar/<int:user_id>")
api.add_resource(GithubLogin, "/login/github")
api.add_resource(
    GithubAuthorize, "/login/github/authorized", endpoint="github.authorize"
)
api.add_resource(SetPassword, "/user/password")
api.add_resource(Order, "/order")


if __name__ == "__main__":
    app.run(port=5000)
