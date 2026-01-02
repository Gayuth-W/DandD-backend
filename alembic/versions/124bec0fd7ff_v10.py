"""V10

Revision ID: 124bec0fd7ff
Revises: dd18f099c5cb
Create Date: 2026-01-01 15:12:16.767396

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '124bec0fd7ff'
down_revision: Union[str, Sequence[str], None] = 'dd18f099c5cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        "UPDATE tasks SET is_default = FALSE WHERE is_default IS NULL"
    )

    op.alter_column(
        "tasks",
        "is_default",
        nullable=False
    )

    op.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS unique_default_task_per_stage
        ON tasks (project_id, stage)
        WHERE is_default = true;
    """)


def downgrade() -> None:
    op.execute("DROP INDEX IF EXISTS unique_default_task_per_stage")
    op.alter_column("tasks", "is_default", nullable=True)
