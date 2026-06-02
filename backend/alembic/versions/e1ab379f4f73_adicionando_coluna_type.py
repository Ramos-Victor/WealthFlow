"""Adicionando coluna type

Revision ID: e1ab379f4f73
Revises: 9880acffb93e
Create Date: 2026-06-01 22:32:02.451601

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = 'e1ab379f4f73'
down_revision: Union[str, Sequence[str], None] = '9880acffb93e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
        # 1. Criar o tipo ENUM explicitamente no PostgreSQL
        sa.Enum('RECEITA', 'DESPESA', name='typetransaction').create(op.get_bind())
        
        # 2. Adicionar a coluna que utiliza o novo tipo
        op.add_column('transactions', sa.Column('type', sa.Enum('RECEITA', 'DESPESA', name='typetransaction'), nullable=False))


def downgrade() -> None:
    # 1. Remover a coluna primeiro
    op.drop_column('transactions', 'type')
    
    # 2. Remover o tipo ENUM do banco de dados
    sa.Enum('RECEITA', 'DESPESA', name='typetransaction').drop(op.get_bind())