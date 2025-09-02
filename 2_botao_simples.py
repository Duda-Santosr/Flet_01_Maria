import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro Botão"
    page.padding = 30
    page.bgcolor = ft.Colors.BLUE_50
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # Criando um texto que será modificado pelo botão
    mensagem = ft.Text(
        value="Clique no botão abaixo! 👇🏽",
        size=24,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.BLUE_900,
    )

    def botao_clicado(evento):
        """
        Função executada ao clicar no botão.
        """
        mensagem.value = "🎉 Parabéns! Você clicou no botão!"
        mensagem.color = ft.Colors.GREEN_700
        page.update()

    # Criando nosso botão estilizado
    meu_botao = ft.ElevatedButton(
        text="Clique em mim!",
        on_click=botao_clicado,
        width=220,
        height=55,
        bgcolor=ft.Colors.BLUE_600,
        color=ft.Colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15),
            elevation=5,
        )
    )

    # Layout centralizado com espaçamento
    conteudo = ft.Column(
        [
            mensagem,
            meu_botao
        ],
        alignment="center",
        horizontal_alignment="center",
        spacing=20
    )

    # Adicionando os elementos à página
    page.add(conteudo)

ft.app(target=main)