"""direct challenges can be private

Revision ID: e43b33a75e6f
Revises: 489ebff657cb
Create Date: 2016-06-11 11:56:37.484088

"""

# revision identifiers, used by Alembic.
revision = 'e43b33a75e6f'
down_revision = '489ebff657cb'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('challenges', sa.Column('is_private', sa.Boolean(), nullable=False, server_default=sa.false()))
    op.add_column('games', sa.Column('is_private', sa.Boolean(), nullable=False, server_default=sa.false()))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('games', 'is_private')
    op.drop_column('challenges', 'is_private')
    ### end Alembic commands ###
