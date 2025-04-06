from models.cliente import Cliente
from typing import Optional, List
from datetime import date

class ClienteController:
    def cadastrar_cliente(conn, cliente):
        cursor = conn.conectar()
        cursor.execute('''
        INSERT INTO clientes (nome, email, cpf_cnpj, tipo_cliente, telefone, endereco, data_nascimento, ativo)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (cliente.nome, cliente.email, cliente.cpf_cnpj, cliente.tipo_cliente,
              cliente.telefone, cliente.endereco,
              cliente.data_nascimento.isoformat() if cliente.data_nascimento else None,
              int(cliente.ativo)))
        
        cursor.execute('INSERT INTO saldo_clientes (id_cliente, saldo, ultima_atualizacao) VALUES (?, ?, CURRENT_DATE)', (cursor.lastrowid, 0))

        conn.commit()
        id_inserido = cursor.lastrowid
        conn.desconectar()
        
        return id_inserido
    
    def buscar_por_id(conn, id: int) -> Optional[Cliente]:
        cursor = conn.conectar()
        cursor.execute('SELECT * FROM clientes WHERE id = ?', (id,))
        resultado = cursor.fetchone()
        conn.desconectar()
        
        if resultado:
            return Cliente(
                id=resultado[0],
                nome=resultado[1],
                email=resultado[2],
                cpf_cnpj=resultado[3],
                tipo_cliente=resultado[4],
                telefone=resultado[5],
                endereco=resultado[6],
                data_nascimento=date.fromisoformat(resultado[7]) if resultado[7] else None
            )
        
        return None
    
    def atualizar(conn, cliente: Cliente) -> bool:
        if not cliente.id:
            return False
        cursor = conn.conectar()
        cursor.execute('''
        UPDATE clientes
        SET nome = ?, email = ?, cpf_cnpj = ?, tipo_cliente = ?, telefone = ?, endereco = ?, data_nascimento = ?, ativo = ?
        WHERE id = ?
        ''', (cliente.nome, cliente.email, cliente.cpf_cnpj, cliente.tipo_cliente,
              cliente.telefone, cliente.endereco,
              cliente.data_nascimento.isoformat() if cliente.data_nascimento else None,
              int(cliente.ativo), cliente.id))
        conn.conn.commit()
        alterado = cursor.rowcount > 0
        conn.desconectar()
        return alterado

    def deletar(conn, id: int) -> bool:
        cursor = conn.conectar()
        cursor.execute('DELETE FROM clientes WHERE id = ?', (id,))
        conn.conn.commit()
        deletado = cursor.rowcount > 0
        # conn.desconectar()
        return deletado

    def listar_todos(conn) -> List[Cliente]:
        cursor = conn.conectar()
        cursor.execute('SELECT * FROM clientes')
        resultados = cursor.fetchall()
        # conn.desconectar()
        return [Cliente(
            id=r[0],
            nome=r[1],
            email=r[2],
            cpf_cnpj=r[3],
            tipo_cliente=r[4],
            telefone=r[5],
            endereco=r[6],
            data_nascimento=date.fromisoformat(r[7]) if r[7] else None
        ) for r in resultados]