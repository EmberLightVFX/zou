"""empty message

Revision ID: 556526e47daa
Revises: 6f6049877105
Create Date: 2019-03-23 22:01:57.576051

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision = "556526e47daa"
down_revision = "6f6049877105"
branch_labels = None
depends_on = None

ORIGINS = [("web", "Web"), ("script", "Script")]


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "login_log",
        sa.Column(
            "id",
            sqlalchemy_utils.types.uuid.UUIDType(binary=False),
            default=uuid.uuid4,
            nullable=False,
        ),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column(
            "person_id",
            sqlalchemy_utils.types.uuid.UUIDType(binary=False),
            default=uuid.uuid4,
            nullable=False,
        ),
        sa.Column(
            "ip_address",
            sqlalchemy_utils.types.ip_address.IPAddressType(length=50),
            nullable=True,
        ),
        sa.Column(
            "origin",
            sqlalchemy_utils.types.choice.ChoiceType(ORIGINS),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["person_id"],
            ["person.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_login_log_person_id"),
        "login_log",
        ["person_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_login_log_created_at"),
        "login_log",
        ["created_at"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_login_log_person_id"), table_name="login_log")
    op.drop_index(op.f("ix_login_log_created_at"), table_name="login_log")
    op.drop_table("login_log")
    # ### end Alembic commands ###
