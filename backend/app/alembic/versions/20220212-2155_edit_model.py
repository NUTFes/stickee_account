"""edit model

Revision ID: 100558759588
Revises: a7e920252163
Create Date: 2022-02-12 21:55:37.514193+09:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '100558759588'
down_revision = 'a7e920252163'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'user', 'permission', ['permission_id'], ['id'])
    op.create_foreign_key(None, 'user', 'type', ['type_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_constraint(None, 'user', type_='foreignkey')
    # ### end Alembic commands ###
