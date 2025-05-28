"""create freebies table

Revision ID: c87044fda2e0
Revises: f576b461a0be
Create Date: 2025-05-28 11:25:24.019367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c87044fda2e0'
down_revision = 'f576b461a0be'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'freebies',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('item_name', sa.String, nullable=False),
        sa.Column('value', sa.Integer, nullable=False),
        sa.Column('dev_id', sa.Integer, sa.ForeignKey('devs.id'), nullable=False),
        sa.Column('company_id', sa.Integer, sa.ForeignKey('companies.id'), nullable=False)
    )


def downgrade():
    op.drop_table('freebies')