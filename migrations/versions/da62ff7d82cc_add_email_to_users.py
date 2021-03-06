"""add email to users

Revision ID: da62ff7d82cc
Revises: 68f5e8686bc6
Create Date: 2021-03-18 19:43:04.305111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "da62ff7d82cc"
down_revision = "68f5e8686bc6"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("email", sa.String(length=80), nullable=False))
    op.create_unique_constraint(op.f("uq_users_email"), "users", ["email"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f("uq_users_email"), "users", type_="unique")
    op.drop_column("users", "email")
    # ### end Alembic commands ###
