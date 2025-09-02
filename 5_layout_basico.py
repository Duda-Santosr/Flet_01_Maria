import flet as ft

def main(page: ft.Page):
    page.title = "Dashboard Compacto"
    page.bgcolor = ft.Colors.GREY_200
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Cabeçalho compacto
    cabecalho = ft.Container(
        content=ft.Text(
            "📊 Dashboard",
            size=18,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLACK87,
        ),
        alignment=ft.alignment.center,
        padding=8,
        bgcolor=ft.Colors.WHITE,
        border_radius=8,
        width=250,
    )

    # Mensagem
    mensagem = ft.Text("", size=14, color=ft.Colors.BLUE_700)

    # Função de clique
    def mostrar_mensagem(e):
        mensagem.value = f"Você clicou em: {e.control.text}"
        page.update()

    # Função para criar botões padronizados
    def criar_botao(texto, icone, cor):
        return ft.FilledButton(
            texto,
            icon=icone,
            width=160,
            height=60,
            bgcolor=cor,
            color=ft.Colors.WHITE,
            on_click=mostrar_mensagem,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=4)  # cantos menos arredondados
            )
        )

    # Botões principais (ações rápidas)
    linha_botoes = ft.Row(
        controls=[
            criar_botao("Adicionar", ft.Icons.ADD, ft.Colors.GREEN_600),
            criar_botao("Editar", ft.Icons.EDIT, ft.Colors.AMBER_600),
            criar_botao("Excluir", ft.Icons.DELETE, ft.Colors.RED_600),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    # Botões do resumo agora também com ícones
    linha_resumo = ft.Row(
        controls=[
            criar_botao("Usuários (1.250)", ft.Icons.PEOPLE, ft.Colors.DEEP_PURPLE),
            criar_botao("Pedidos (320)", ft.Icons.SHOPPING_CART, ft.Colors.ORANGE),
            criar_botao("Vendas (R$ 45K)", ft.Icons.ATTACH_MONEY, ft.Colors.TEAL),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
        wrap=True
    )

    # Layout principal
    layout_principal = ft.Column(
        controls=[
            cabecalho,
            ft.Text("Ações rápidas:", size=16, weight=ft.FontWeight.W_500, color=ft.Colors.BLACK87),
            linha_botoes,
            mensagem,
            ft.Text("Resumo:", size=16, weight=ft.FontWeight.W_500, color=ft.Colors.BLACK87),
            linha_resumo,
        ],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(layout_principal)

ft.app(target=main)