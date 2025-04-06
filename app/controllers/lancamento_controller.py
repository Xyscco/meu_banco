from app.models.lancamento import Lancamento

class LancamentoController:
    def cadastrar_lancamento(conn, lancamento):
        cursor = conn.conectar()
        cursor.execute('''
        INSERT INTO lancamentos (data, descricao, valor, tipo_lancamento)
        VALUES (?, ?, ?, ?)
        ''', (lancamento.data, lancamento.descricao, lancamento.valor, lancamento.tipo_lancamento))

        if lancamento.tipo_lancamento == 'entrada':
            cursor.execute('UPDATE saldo_clientes SET saldo = saldo + ?, ultima_atualizacao = CURRENT_DATE WHERE id = ?''', (lancamento.valor, lancamento.id_cliente))
        else:
            cursor.execute('UPDATE saldo_clientes SET saldo = saldo - ?, ultima_atualizacao = CURRENT_DATE WHERE id = ?''', (lancamento.valor, lancamento.id_cliente))

        conn.commit()
        id_inserido = cursor.lastrowid
        conn.desconectar()
        return id_inserido

    def buscar_por_id(conn, id: int):
        cursor = conn.conectar()
        cursor.execute('SELECT * FROM lancamentos WHERE id = ?', (id,))
        resultado = cursor.fetchone()
        conn.desconectar()

        if resultado:
            return Lancamento(
                id=resultado[0],
                id_cliente=resultado[1],
                data=resultado[2],
                descricao = resultado[3],
                valor = resultado[4],
                tipo_lancamento = resultado[5]
            )