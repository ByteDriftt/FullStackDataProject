"""Add completed column

Revision ID: 2616ce986a82
Revises: e5076b3c8597
Create Date: 2024-10-14 22:59:05.801618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2616ce986a82'
down_revision = 'e5076b3c8597'
branch_labels = None
depends_on = None


def upgrade():
    # Add column as nullable first
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('completed', sa.Boolean(), nullable=True))
    
    # Update existing rows
    op.execute('UPDATE todos SET completed = False WHERE completed IS NULL')
    
    # Now set the column to non-nullable
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.alter_column('completed', nullable=False)


def downgrade():
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.drop_column('completed')