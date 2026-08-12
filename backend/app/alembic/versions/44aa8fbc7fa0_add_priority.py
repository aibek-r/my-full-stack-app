"""add priority

Revision ID: 44aa8fbc7fa0
Revises: fe56fa70289e
Create Date: 2026-08-12 15:56:10.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "44aa8fbc7fa0"
down_revision = "fe56fa70289e"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "item",
        sa.Column(
            "priority",
            sa.String(length=20),
            nullable=False,
            server_default="medium",
        ),
    )


def downgrade():
    op.drop_column("item", "priority")
