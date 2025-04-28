import flet as ft
from app.view.movimentacao_view import movimentacao_view
from app.view.cliente_view import cliente_view

def fechar_aplicacao(page: ft.Page):
    page.window.destroy()

def mostrar_info_aplicativo(page: ft.Page):
    page.dialog.open = True
    page.update()


def main(page: ft.Page):
    page.title = "Meu Banco"
    page.window.width = 1280
    page.window.height = 720
    page.theme_mode = ft.ThemeMode.LIGHT

    def close_dlg(e):
        dlg_modal.open = False
        e.control.page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=150,
        min_extended_width=400,
        # leading=ft.FloatingActionButton(icon=ft.Icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.COMPARE_ARROWS_SHARP,
                selected_icon=ft.Icons.COMPARE_ARROWS_SHARP,
                label="Movimentação",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.PERSON,
                selected_icon=ft.Icons.PERSON,
                label="Clientes",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.INSERT_DRIVE_FILE,
                selected_icon=ft.Icon(ft.Icons.INSERT_DRIVE_FILE),
                label_content=ft.Text("Extrato"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Sobre a aplicação"),
        content=ft.Text("Desenvolvida para estudo do uso do flet por Francisco Márcio"),
        actions=[
            ft.TextButton("Fechar", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def open_dlg_modal(e):
        e.control.page.overlay.append(dlg_modal)
        dlg_modal.open = True
        e.control.page.update()

    app_bar = ft.AppBar(
        leading=ft.Icon(ft.Icons.ATTACH_MONEY),
        title=ft.Text("Meu Banco"),
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.Container(
                content=ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Sobre", on_click= open_dlg_modal),
                        ft.PopupMenuItem(),
                        ft.PopupMenuItem(text="Fechar", on_click=lambda _: fechar_aplicacao(page)),
                        
                    ]
                )
            )
        ],
    )

    page.add(
        app_bar,
        ft.Row(
        [
            rail,
            ft.VerticalDivider(width=1),
            ft.Column(
                # [movimentacao_view(ft, page)], 
                [cliente_view(page)],
                alignment=ft.MainAxisAlignment.START, expand=True
            ),
        ],
        width=page.window.width,
        height=page.window.height - 70,
    ))


ft.app(target=main)

# menu = """


#     [d] Depositar
#     [s] Sacar
#     [e] Extrato
#     [q] Sair
    
# =>"""

# saldo = 0
# limite = 500
# extrato = ""
# numero_saques = 0
# LIMITE_SAQUES = 3

# while True:
#     opcao = input(menu)

#     if opcao == "d":
#         valor = float(input("Informe o valor do depósito: "))
#         if valor > 0:
#             saldo += valor
#             extrato += f"Depósito: R$ {valor:.2f}\n"

#         else:
#             print("Operação falhou! O valor informado é inválido.")

#     elif opcao == "s":
#         valor = float(input("Informe o valor do saque: "))

#         excedeu_saldo = valor > saldo

#         excedeu_limite = valor > limite

#         excedeu_saques = numero_saques >= LIMITE_SAQUES

#         if excedeu_saldo:
#             print("Operação falhou! Você não tem saldo suficiente.")

#         elif excedeu_limite:
#             print("Operação falhou! O valor do saque excede o limite.")

#         elif excedeu_saques:
#             print("Operação falhou! Número máximo de saques excedido.")

#         elif valor > 0:
#             saldo -= valor
#             extrato += f"Saque: R$ {valor:.2f}\n"
#             numero_saques += 1

#         else:
#             print("Operação falhou! O valor informado é inválido.")

#     elif opcao == "e":
#         print("\n================ EXTRATO ================")
#         print("Não foram realizadas movimentações." if not extrato else extrato)
#         print(f"\nSaldo: R$ {saldo:.2f}")
#         print("==========================================")

#     elif opcao == "q":
#         break

#     else:
#         print("Operação inválida, por favor selecione novamente a operação desejada.")