from app.controllers import lancamento_controller as lc
from app.database import conecta_banco as db

def movimentacao_view(ft, page):
    estado = {"tipo": "Deposito"}

    def muda_tipo_movimentacao(e):
        if e.control.value:
            estado["tipo"] = "Depósito"
        else:
            estado["tipo"] = "Saque"

        # Atualizando o texto do label do switch
        switch.label = estado["tipo"]
        
        # Atualizando o texto do botão
        botao.text = "Depositar" if estado["tipo"] == "Depósito" else "Sacar"
        
        page.update()

    

    def gravar_movimentacao(e):
        # db.conectar()
        lancamento = {
            "valor": valor.value,
            "descricao": descricao.value,
            "cliente": cliente.value,
        }

        print(lancamento)
        # if estado["tipo"] == "Deposito":
        #    lc.LancamentoController.cadastrar_lancamento(db, valor, "entrada") 
        # else:
        #     pass

        # db.desconectar()
        
        page.update()

    switch = ft.Switch(
        label=estado["tipo"],
        value=True,
        on_change=muda_tipo_movimentacao,
    )

    valor = ft.TextField(label="Valor", prefix_text="R$")
    descricao = ft.TextField(label="Descrição")
    cliente = ft.Dropdown(
            label="Cliente",
            options=[
                ft.dropdown.Option("Cliente 1"),
                ft.dropdown.Option("Cliente 2"),
                ft.dropdown.Option("Cliente 3"),
            ],
            autofocus=True,
        )
    
    botao = ft.ElevatedButton(
        "Depositar",
        on_click=gravar_movimentacao
    )


    return ft.Container(
        content=ft.Column(
            [
                switch,
                cliente,
                valor,
                descricao,
                botao,
                ft.TextButton("Voltar", on_click=lambda e: None),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )