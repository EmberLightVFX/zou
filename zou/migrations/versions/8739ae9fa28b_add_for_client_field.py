"""Add for client field

Revision ID: 8739ae9fa28b
Revises: cf3d365de164
Create Date: 2020-03-11 21:28:29.145467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8739ae9fa28b"
down_revision = "cf3d365de164"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "metadata_descriptor",
        sa.Column("for_client", sa.Boolean(), nullable=True),
    )
    op.create_index(
        op.f("ix_metadata_descriptor_for_client"),
        "metadata_descriptor",
        ["for_client"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_metadata_descriptor_for_client"),
        table_name="metadata_descriptor",
    )
    op.drop_column("metadata_descriptor", "for_client")
    # ### end Alembic commands ###
