"""empty message

Revision ID: deb0bbcbf768
Revises: 
Create Date: 2018-09-05 11:27:27.205493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'deb0bbcbf768'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('first_name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=20), nullable=False),
    sa.Column('image_file', sa.String(length=20), nullable=False),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('image_file'),
    sa.UniqueConstraint('username')
    )
    op.create_table('fitpost',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('bodyfat', sa.Integer(), nullable=True),
    sa.Column('rhr', sa.Integer(), nullable=True),
    sa.Column('prog_pic', sa.String(length=20), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('workout', sa.Text(), nullable=True),
    sa.Column('public', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fitpost')
    op.drop_table('user')
    # ### end Alembic commands ###
