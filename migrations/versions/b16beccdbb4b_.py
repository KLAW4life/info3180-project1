"""empty message

Revision ID: b16beccdbb4b
Revises: 
Create Date: 2023-03-12 12:27:11.649229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b16beccdbb4b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property_portfolio',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('bedroom', sa.Integer(), nullable=True),
    sa.Column('bathroom', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('type', sa.String(length=10), nullable=True),
    sa.Column('photo', sa.String(length=400), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property_portfolio')
    # ### end Alembic commands ###
