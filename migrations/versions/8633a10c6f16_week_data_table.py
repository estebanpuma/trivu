"""week data table

Revision ID: 8633a10c6f16
Revises: 9e226a05b6ae
Create Date: 2022-11-28 19:41:00.768590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8633a10c6f16'
down_revision = '9e226a05b6ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('week_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('neck', sa.Float(), nullable=True),
    sa.Column('waist', sa.Float(), nullable=True),
    sa.Column('body_fat', sa.Float(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('height', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('birth', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('birth')
        batch_op.drop_column('height')

    op.drop_table('week_data')
    # ### end Alembic commands ###