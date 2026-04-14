"""add timer_duration to labs and violations to attempts

Revision ID: 001_add_timer_violations
Revises: bd18b4e571c6
Create Date: 2026-04-14 16:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001_add_timer_violations'
down_revision = 'bd18b4e571c6'
branch_labels = None
depends_on = None


def upgrade():
    # Add timer_duration column to labs table
    op.add_column('labs', sa.Column('timer_duration', sa.Integer(), nullable=True, default=0))
    
    # Add violations column to attempts table
    op.add_column('attempts', sa.Column('violations', sa.Text(), nullable=True))


def downgrade():
    op.drop_column('attempts', 'violations')
    op.drop_column('labs', 'timer_duration')
