"""nullable routing_key

Revision ID: a53738c6cc2f
Revises: 00bed7ede274
Create Date: 2020-04-15 12:24:20.186071

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "a53738c6cc2f"
down_revision = "00bed7ede274"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "amqp_message", "routing_key", existing_type=sa.VARCHAR(), nullable=True
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "amqp_message", "routing_key", existing_type=sa.VARCHAR(), nullable=False
    )
    # ### end Alembic commands ###