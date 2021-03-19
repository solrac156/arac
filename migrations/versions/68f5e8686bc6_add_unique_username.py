"""add unique username

Revision ID: 68f5e8686bc6
Revises: f616062d26e9
Create Date: 2021-03-18 19:40:45.938857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68f5e8686bc6'
down_revision = 'f616062d26e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(op.f('uq_items_name'), 'items', ['name'])
    op.drop_constraint('items_name_key', 'items', type_='unique')
    op.create_unique_constraint(op.f('uq_stores_name'), 'stores', ['name'])
    op.drop_constraint('stores_name_key', 'stores', type_='unique')
    op.create_unique_constraint(op.f('uq_users_username'), 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq_users_username'), 'users', type_='unique')
    op.create_unique_constraint('stores_name_key', 'stores', ['name'])
    op.drop_constraint(op.f('uq_stores_name'), 'stores', type_='unique')
    op.create_unique_constraint('items_name_key', 'items', ['name'])
    op.drop_constraint(op.f('uq_items_name'), 'items', type_='unique')
    # ### end Alembic commands ###
