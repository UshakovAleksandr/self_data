"""add loan_sum to LoanModel

Revision ID: 7299da4b5cff
Revises: d668eebe90d9
Create Date: 2021-06-10 13:28:49.830005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7299da4b5cff'
down_revision = 'd668eebe90d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_loans')
    with op.batch_alter_table('loans', schema=None) as batch_op:
        batch_op.add_column(sa.Column('loan_sum', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('loan_active', sa.Boolean(), nullable=False))
        batch_op.drop_column('loans_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('loans', schema=None) as batch_op:
        batch_op.add_column(sa.Column('loans_active', sa.BOOLEAN(), nullable=False))
        batch_op.drop_column('loan_active')
        batch_op.drop_column('loan_sum')

    op.create_table('_alembic_tmp_loans',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('client_id', sa.INTEGER(), nullable=True),
    sa.Column('payment_rest', sa.INTEGER(), nullable=True),
    sa.Column('payment_rep_month', sa.INTEGER(), nullable=True),
    sa.Column('loan_delinquency', sa.BOOLEAN(), nullable=False),
    sa.Column('loan_sum', sa.INTEGER(), nullable=True),
    sa.Column('loan_active', sa.BOOLEAN(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###