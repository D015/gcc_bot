"""Install

Revision ID: aadef6111995
Revises: 
Create Date: 2021-04-06 17:06:30.455440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aadef6111995'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('base_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chat_id', sa.Integer(), nullable=True),
    sa.Column('is_bot', sa.Boolean(), nullable=True),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('language_code', sa.String(length=6), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['base_model.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_chat_id'), 'user', ['chat_id'], unique=True)
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.String(length=1024), nullable=True),
    sa.Column('summary', sa.String(length=56), nullable=True),
    sa.Column('start', sa.DateTime(), nullable=True),
    sa.Column('end', sa.DateTime(), nullable=True),
    sa.Column('utc_time_offset', sa.String(length=6), nullable=True),
    sa.Column('timezone', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('location', sa.String(length=1024), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['base_model.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_event_event_id'), 'event', ['event_id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_event_event_id'), table_name='event')
    op.drop_table('event')
    op.drop_index(op.f('ix_user_chat_id'), table_name='user')
    op.drop_table('user')
    op.drop_table('base_model')
    # ### end Alembic commands ###
