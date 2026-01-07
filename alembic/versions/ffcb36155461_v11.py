"""V11

Revision ID: ffcb36155461
Revises: 124bec0fd7ff
Create Date: 2026-01-07 17:24:15.986389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ffcb36155461'
down_revision: Union[str, Sequence[str], None] = '124bec0fd7ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
