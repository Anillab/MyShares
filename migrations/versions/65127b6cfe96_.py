"""empty message

Revision ID: 65127b6cfe96
Revises: 0f5cdcd191d0
Create Date: 2018-07-04 10:05:14.061403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65127b6cfe96'
down_revision = '0f5cdcd191d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company', sa.Column('Par_value', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('company', 'Par_value')
    # ### end Alembic commands ###
