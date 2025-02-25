"""Add entity.entity_concept_links

Revision ID: 269d41bfb73f
Revises: feffd3c5b806
Create Date: 2023-12-11 17:11:27.153961

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision = "269d41bfb73f"
down_revision = "feffd3c5b806"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "entity_concept_link",
        sa.Column(
            "entity_in_id",
            sqlalchemy_utils.types.uuid.UUIDType(binary=False),
            default=uuid.uuid4,
            nullable=False,
        ),
        sa.Column(
            "entity_out_id",
            sqlalchemy_utils.types.uuid.UUIDType(binary=False),
            default=uuid.uuid4,
            nullable=False,
        ),
        sa.Column(
            "id",
            sqlalchemy_utils.types.uuid.UUIDType(binary=False),
            default=uuid.uuid4,
            nullable=False,
        ),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["entity_in_id"],
            ["entity.id"],
        ),
        sa.ForeignKeyConstraint(
            ["entity_out_id"],
            ["entity.id"],
        ),
        sa.PrimaryKeyConstraint("entity_in_id", "entity_out_id", "id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("entity_concept_link")
    # ### end Alembic commands ###
