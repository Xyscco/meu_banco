import flet as ft

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

    page.add(app_bar)


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