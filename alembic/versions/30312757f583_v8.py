"""v8

Revision ID: 30312757f583
Revises: 616a347fc0e0
Create Date: 2026-01-01 13:57:50.043182

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30312757f583'
down_revision: Union[str, Sequence[str], None] = '616a347fc0e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
