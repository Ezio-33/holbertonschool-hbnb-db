"""create account table

Revision ID: 04c3a5856846
Revises: 
Create Date: 2024-07-01 13:21:41.796825

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04c3a5856846'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('User',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(length=120), nullable=False),
                    sa.Column('password', sa.String(length=80), nullable=False),
                    sa.Column('first_name', sa.String(length=80), nullable=False),
                    sa.Column('last_name', sa.String(length=80), nullable=False),
                    sa.Column('is_admin', sa.Boolean(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )


def downgrade() -> None:
    pass
