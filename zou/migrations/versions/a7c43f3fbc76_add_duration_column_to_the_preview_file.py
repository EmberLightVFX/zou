"""Add duration column to the preview file

Revision ID: a7c43f3fbc76
Revises: 05b7dc79a416
Create Date: 2023-11-14 14:44:34.569736

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = "a7c43f3fbc76"
down_revision = "05b7dc79a416"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("preview_file", schema=None) as batch_op:
        batch_op.add_column(sa.Column("duration", sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("preview_file", schema=None) as batch_op:
        batch_op.drop_column("duration")
    # ### end Alembic commands ###
