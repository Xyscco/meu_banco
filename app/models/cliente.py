from datetime import date
from typing import Optional, List
import enum

class TipoCliente(enum.Enum):
    PESSOA_FISICA = "Pessoa Física"
    PESSOA_JURIDICA = "Pessoa Jurídica"

class Cliente:
    def __init__(self, nome: str, email: str, cpf_cnpj: str, tipo_cliente: str,
                 telefone: Optional[str] = None, endereco: Optional[str] = None,
                 data_nascimento: Optional[date] = None):
        self.id: Optional[int] = None  # Seria definido ao salvar no banco de dados
        self.nome = self.validar_nome(nome)
        self.email = self.validar_email(email)
        self.cpf_cnpj = self.validar_cpf_cnpj(cpf_cnpj)
        self.tipo_cliente = self.validar_tipo_cliente(tipo_cliente)
        self.telefone = telefone
        self.endereco = endereco
        self.data_nascimento = data_nascimento
        self.ativo = True

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
            'endereco': self.endereco,
            'data_nascimento': str(self.data_nascimento) if self.data_nascimento else None,
            'cpf_cnpj': self.cpf_cnpj,
            'tipo_cliente': self.tipo_cliente,
            'ativo': self.ativo
        }
    
