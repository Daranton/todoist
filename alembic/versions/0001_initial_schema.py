"""initial schema

Revision ID: 0001_initial_schema
Revises:
Create Date: 2026-03-13

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '0001_initial_schema'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('title', sa.String(), index=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('completed', sa.Boolean(), default=False),
        sa.Column('due_date', sa.String(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('tasks')
