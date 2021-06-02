"""Install. Using BaseModel in models through mixins (fixing env.py)

Revision ID: f80cb3c44fb3
Revises: b51c63cb3539
Create Date: 2021-06-01 14:31:20.374132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f80cb3c44fb3"
down_revision = "b51c63cb3539"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("timestamp", sa.DateTime(), nullable=True),
        sa.Column("active", sa.Boolean(), nullable=True),
        sa.Column("archived", sa.Boolean(), nullable=True),
        sa.Column("telegram_user_id", sa.Integer(), nullable=True),
        sa.Column("is_bot", sa.Boolean(), nullable=True),
        sa.Column("first_name", sa.String(length=50), nullable=True),
        sa.Column("last_name", sa.String(length=50), nullable=True),
        sa.Column("username", sa.String(length=50), nullable=True),
        sa.Column("language_code", sa.String(length=6), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_user_telegram_user_id"), "user", ["telegram_user_id"], unique=True
    )
    op.create_table(
        "event",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("timestamp", sa.DateTime(), nullable=True),
        sa.Column("active", sa.Boolean(), nullable=True),
        sa.Column("archived", sa.Boolean(), nullable=True),
        sa.Column("google_calendar_event_id", sa.String(length=1024), nullable=True),
        sa.Column("summary", sa.String(length=56), nullable=True),
        sa.Column("start", sa.DateTime(), nullable=True),
        sa.Column("end", sa.DateTime(), nullable=True),
        sa.Column("utc_time_offset", sa.String(length=6), nullable=True),
        sa.Column("timezone", sa.String(length=50), nullable=True),
        sa.Column("conference_link", sa.String(length=2000), nullable=True),
        sa.Column("document_link", sa.String(length=2000), nullable=True),
        sa.Column("description", sa.String(length=1024), nullable=True),
        sa.Column("location", sa.String(length=2000), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_event_google_calendar_event_id"),
        "event",
        ["google_calendar_event_id"],
        unique=True,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_event_google_calendar_event_id"), table_name="event")
    op.drop_table("event")
    op.drop_index(op.f("ix_user_telegram_user_id"), table_name="user")
    op.drop_table("user")
    # ### end Alembic commands ###