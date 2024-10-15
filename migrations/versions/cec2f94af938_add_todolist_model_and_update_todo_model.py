"""Add TodoList model and update Todo model

Revision ID: cec2f94af938
Revises: 2616ce986a82
Create Date: 2024-10-15 08:21:04.041084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cec2f94af938'
down_revision = '2616ce986a82'
branch_labels = None
depends_on = None


def upgrade():
    # Create todolists table
    op.create_table('todolists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    
    # Create a default todolist
    op.execute("INSERT INTO todolists (name) VALUES ('Default List')")
    
    # Add list_id column to todos table, allowing NULL initially
    op.add_column('todos', sa.Column('list_id', sa.Integer(), nullable=True))
    
    # Update existing todos to use the default list
    op.execute("UPDATE todos SET list_id = (SELECT id FROM todolists LIMIT 1)")
    
    # Now set list_id to non-nullable
    op.alter_column('todos', 'list_id', nullable=False)
    
    # Add the foreign key constraint
    op.create_foreign_key(None, 'todos', 'todolists', ['list_id'], ['id'])

def downgrade():
    op.drop_constraint(None, 'todos', type_='foreignkey')
    op.drop_column('todos', 'list_id')
    op.drop_table('todolists')