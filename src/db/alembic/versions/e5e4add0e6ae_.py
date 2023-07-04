"""empty message

Revision ID: e5e4add0e6ae
Revises: c602180cf9c9
Create Date: 2023-07-04 09:04:52.315752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5e4add0e6ae'
down_revision = 'c602180cf9c9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointments', sa.Column('available_slot_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'appointments', 'available_slots', ['available_slot_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'appointments', type_='foreignkey')
    op.drop_column('appointments', 'available_slot_id')
    # ### end Alembic commands ###
