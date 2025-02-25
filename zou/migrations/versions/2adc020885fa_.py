"""empty message

Revision ID: 2adc020885fa
Revises: 892b264937ec
Create Date: 2019-05-08 16:13:58.958576

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "2adc020885fa"
down_revision = "892b264937ec"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "news",
        "preview_file_id",
        existing_type=postgresql.UUID(),
        nullable=True,
    )
    op.drop_index("ix_news_person_id", table_name="news")
    op.drop_constraint("news_person_id_fkey", "news", type_="foreignkey")
    op.drop_column("news", "person_id")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "news",
        sa.Column(
            "person_id", postgresql.UUID(), autoincrement=False, nullable=False
        ),
    )
    op.create_foreign_key(
        "news_person_id_fkey", "news", "person", ["person_id"], ["id"]
    )
    op.create_index("ix_news_person_id", "news", ["person_id"], unique=False)
    op.alter_column(
        "news",
        "preview_file_id",
        existing_type=postgresql.UUID(),
        nullable=False,
    )
    # ### end Alembic commands ###
