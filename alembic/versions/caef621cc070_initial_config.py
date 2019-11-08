"""Initial config

Revision ID: caef621cc070
Revises:
Create Date: 2019-11-10 15:04:11.918287

"""
import sqlalchemy as sa
from sqlalchemy.schema import CreateSequence

from alembic import op

# revision identifiers, used by Alembic.
revision = "caef621cc070"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    article_id_seq = sa.Sequence("article_id_seq")
    op.execute(CreateSequence(article_id_seq))
    op.create_table(
        "articles",
        sa.Column("id", sa.BigInteger, primary_key=True, server_default=article_id_seq.next_value()),
        sa.Column("body", sa.String(1000)),
        sa.Column("title", sa.String(100)),
        sa.Column("author_id", sa.BigInteger)
    )

    author_id_seq = sa.Sequence("author_id_seq")
    op.execute(CreateSequence(author_id_seq))
    op.create_table(
        "authors",
        sa.Column("id", sa.BigInteger, primary_key=True, server_default=author_id_seq.next_value()),
        sa.Column("first_name", sa.String(1000)),
        sa.Column("last_name", sa.String(100))
    )


def downgrade():
    op.execute("DROP SEQUENCE article_id_seq")
    op.drop_table("articles")

    op.execute("DROP SEQUENCE author_id_seq")
    op.drop_table("authors")
