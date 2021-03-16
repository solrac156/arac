from flask_restful import Resource

from libs.strings import accepted_locales, gettext, set_default_locale, refresh


class Language(Resource):
    @classmethod
    def get(cls, locale: str):
        if locale not in accepted_locales:
            return {"message": gettext("language_not_found")}, 404
        set_default_locale(locale)
        refresh()
        return {"message": gettext("language_change_success")}
