"""add is_casting_standby column to Entity

Revision ID: b97a71306fc8
Revises: 5a291251823c
Create Date: 2022-07-12 14:21:29.530095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b97a71306fc8"
down_revision = "5a291251823c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "entity", sa.Column("is_casting_standby", sa.Boolean(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("entity", "is_casting_standby")
    # ### end Alembic commands ###
