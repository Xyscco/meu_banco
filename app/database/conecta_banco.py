import sqlite3

def conectar():

    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS lancamentos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        cliente_id INTEGER NOT NULL,
                        tipo TEXT NOT NULL CHECK(tipo IN ('entrada', 'saida')),
                        valor DECIMAL(10, 2) NOT NULL,
                        descricao TEXT,
                        data_lancamento DATETIME DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
                    );
                    """)
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS clientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        tipo_cliente TEXT NOT NULL CHECK(tipo IN ('fisica', 'juridica')),
                        cpf_cnpj TEXT UNIQUE NOT NULL,
                        data_nascimento DATE,
                        endereco TEXT,
                        telefone TEXT,
                        email TEXT UNIQUE,
                        data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
                    );
                    """)
    cursor.execute("""
                    CREATE TABLE saldo_clientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        cliente_id INTEGER NOT NULL,
                        saldo DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
                        ultima_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
                    );
                    """)

    conexao.commit()


    return conexao

def desconectar(conexao):
    conexao.close()