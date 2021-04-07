"""Install

Revision ID: 5f83a23d61d5
Revises: aadef6111995
Create Date: 2021-04-07 12:32:24.748924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f83a23d61d5'
down_revision = 'aadef6111995'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('telegram_user_id', sa.Integer(), nullable=True))
    op.drop_index('ix_user_chat_id', table_name='user')
    op.create_index(op.f('ix_user_telegram_user_id'), 'user', ['telegram_user_id'], unique=True)
    op.drop_column('user', 'chat_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('chat_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_user_telegram_user_id'), table_name='user')
    op.create_index('ix_user_chat_id', 'user', ['chat_id'], unique=True)
    op.drop_column('user', 'telegram_user_id')
    # ### end Alembic commands ###
