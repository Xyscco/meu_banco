import flet as ft
from app.controllers.cliente_controller import cliente_controller as cc
from app.database import conecta_banco as db


def cliente_view(page):

    # Lista para armazenar os clientes cadastrados
    clientes = []

    def gravar_cliente(e):
        conn = db.conectar()
        # cliente = Cliente
        cc.cadastrar_cliente(conn, )

    # Campo de texto para o nome do cliente
    nome_cliente = ft.TextField(
        label="Nome do Cliente",
        expand=True,  # Ocupar todo o espaço disponível horizontalmente
        autofocus=True
    )
    
    # Container para a lista de clientes
    lista_clientes = ft.ListView(
        expand=True,  # Ocupar o espaço vertical disponível
        spacing=10,
        auto_scroll=True
    )

    # Função para adicionar um novo cliente
    def adicionar_cliente(e):
        if nome_cliente.value:
            # Adiciona o cliente à lista
            clientes.append(nome_cliente.value)
            
            # Adiciona o cliente à lista visual
            lista_clientes.controls.append(
                ft.Container(
                    ft.Text(nome_cliente.value, size=16),
                    padding=10,
                    border_radius=5,
                    bgcolor=ft.colors.BLUE_50,
                    border=ft.border.all(1, ft.colors.BLUE_400)
                )
            )
            
            # Limpa o campo de texto
            nome_cliente.value = ""
            
            # Atualiza a página
            page.update()
    
    # Botão para salvar o cliente
    botao_salvar = ft.ElevatedButton(
        text="Salvar Cliente",
        icon=ft.icons.SAVE,
        on_click=adicionar_cliente,
        expand=True  # Ocupar todo o espaço disponível horizontalmente
    )

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Cadastro de Clientes", size=24, weight=ft.FontWeight.BOLD),
                ft.Divider(height=1),
                # Formulário de cadastro
                ft.Container(
                    content=ft.Column([
                        ft.Text("Novo Cliente", size=16),
                        nome_cliente,
                        botao_salvar
                    ]),
                    padding=20,
                    border_radius=10,
                    bgcolor=ft.colors.WHITE,
                    border=ft.border.all(1, ft.colors.BLACK12),
                ),
                ft.Divider(height=1),
                
                # Título da lista
                ft.Text("Clientes Cadastrados", size=16),
                
                # Container com a lista de clientes (com barra de rolagem)
                ft.Container(
                    content=lista_clientes,
                    height=300,  # Altura fixa para a lista
                    border_radius=10,
                    bgcolor=ft.colors.WHITE,
                    border=ft.border.all(1, ft.colors.BLACK12),
                    padding=10
                )

            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )