"""v5

Revision ID: 783082d9ebf5
Revises: b47bb4f21ed9
Create Date: 2026-01-01 13:50:18.729648

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '783082d9ebf5'
down_revision: Union[str, Sequence[str], None] = 'b47bb4f21ed9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
