"""v7

Revision ID: 616a347fc0e0
Revises: 783082d9ebf5
Create Date: 2026-01-01 13:57:30.823368

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '616a347fc0e0'
down_revision: Union[str, Sequence[str], None] = '783082d9ebf5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
