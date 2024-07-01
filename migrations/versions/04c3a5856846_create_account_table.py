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
    op.create_table('amenity',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=80), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('city',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=80), nullable=False),
                    sa.Column('country_code', sa.String(length=80), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('country',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=80), nullable=False),
                    sa.Column('code', sa.String(length=80), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('code')
                    )
    op.create_table('place',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=80), nullable=False),
                    sa.Column('description', sa.String(length=80), nullable=False),
                    sa.Column('address', sa.String(length=80), nullable=False),
                    sa.Column('latitude', sa.Float(), nullable=False),
                    sa.Column('longitude', sa.Float(), nullable=False),
                    sa.Column('host_id', sa.Integer(), nullable=False),
                    sa.Column('city_id', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
                    sa.ForeignKeyConstraint(['host_id'], ['User.id'], ),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('review',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('rating', sa.Integer(), nullable=False),
                    sa.Column('comment', sa.String(length=80), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('place_id', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.ForeignKeyConstraint(['place_id'], ['place.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['User.id'], )
                    )


def downgrade() -> None:
    pass
