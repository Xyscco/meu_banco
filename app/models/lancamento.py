class Lancamento:
    def __init__(self, id_cliente, data, descricao, valor, tipo_lancamento):
        self.id = None
        self.id_cliente = id_cliente
        self.data = data
        self.descricao = descricao
        self.valor = valor
        self.tipo_lancamento = tipo_lancamento