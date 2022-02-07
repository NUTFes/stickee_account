"""separate models file

Revision ID: 9927bb34c952
Revises: 90f58740d955
Create Date: 2022-02-07 00:00:39.073572+09:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9927bb34c952'
down_revision = '90f58740d955'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bureau',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bureau_id'), 'bureau', ['id'], unique=True)
    op.create_table('department',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_department_id'), 'department', ['id'], unique=True)
    op.create_table('grade',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_grade_id'), 'grade', ['id'], unique=True)
    op.create_table('major',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_major_id'), 'major', ['id'], unique=True)
    op.create_table('permission',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_permission_id'), 'permission', ['id'], unique=True)
    op.create_table('position',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_position_id'), 'position', ['id'], unique=True)
    op.create_table('sex',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sex_id'), 'sex', ['id'], unique=True)
    op.create_table('type',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_type_id'), 'type', ['id'], unique=True)
    op.create_table('user_detail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sex_id', sa.Integer(), nullable=True),
    sa.Column('birth', sa.DateTime(), nullable=True),
    sa.Column('tel', sa.String(), nullable=True),
    sa.Column('grade_id', sa.Integer(), nullable=True),
    sa.Column('major_id', sa.Integer(), nullable=True),
    sa.Column('bureau_id', sa.Integer(), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.Column('position_id', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['bureau_id'], ['bureau.id'], ),
    sa.ForeignKeyConstraint(['department_id'], ['department.id'], ),
    sa.ForeignKeyConstraint(['grade_id'], ['grade.id'], ),
    sa.ForeignKeyConstraint(['major_id'], ['major.id'], ),
    sa.ForeignKeyConstraint(['position_id'], ['position.id'], ),
    sa.ForeignKeyConstraint(['sex_id'], ['sex.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_detail_id'), 'user_detail', ['id'], unique=True)
    op.add_column('user', sa.Column('permission_id', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('type_id', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('user_detail_id', sa.Integer(), nullable=True))
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'number',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_foreign_key(None, 'user', 'type', ['type_id'], ['id'])
    op.create_foreign_key(None, 'user', 'permission', ['permission_id'], ['id'])
    op.create_foreign_key(None, 'user', 'user_detail', ['user_detail_id'], ['id'])
    op.drop_column('user', 'department')
    op.drop_column('user', 'grade')
    op.drop_column('user', 'bureau')
    op.drop_column('user', 'sex')
    op.drop_column('user', 'major')
    op.drop_column('user', 'permission')
    op.drop_column('user', 'tel')
    op.drop_column('user', 'position')
    op.drop_column('user', 'birth')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('birth', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('position', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('tel', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('permission', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('major', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('sex', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('bureau', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('grade', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('department', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.alter_column('user', 'number',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('user', 'user_detail_id')
    op.drop_column('user', 'type_id')
    op.drop_column('user', 'permission_id')
    op.drop_index(op.f('ix_user_detail_id'), table_name='user_detail')
    op.drop_table('user_detail')
    op.drop_index(op.f('ix_type_id'), table_name='type')
    op.drop_table('type')
    op.drop_index(op.f('ix_sex_id'), table_name='sex')
    op.drop_table('sex')
    op.drop_index(op.f('ix_position_id'), table_name='position')
    op.drop_table('position')
    op.drop_index(op.f('ix_permission_id'), table_name='permission')
    op.drop_table('permission')
    op.drop_index(op.f('ix_major_id'), table_name='major')
    op.drop_table('major')
    op.drop_index(op.f('ix_grade_id'), table_name='grade')
    op.drop_table('grade')
    op.drop_index(op.f('ix_department_id'), table_name='department')
    op.drop_table('department')
    op.drop_index(op.f('ix_bureau_id'), table_name='bureau')
    op.drop_table('bureau')
    # ### end Alembic commands ###