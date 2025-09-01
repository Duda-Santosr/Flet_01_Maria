import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro Botão"
    page.padding = 20

    # Criando um texto que será modificado pelo botão
    mensagem = ft.Text(
        value="Clique no botão abaixo!👇",
        size=20,
        text_align=ft.TextAlign.CENTER
    )

    def botao_clicado(evento):
        """
        Esta função será executada sempre que o botão for clicado.
        O parâmetro 'evento' contém informações sobre o clique.
        """
        # Mudando o texto da mensagem
        mensagem.value = "🎉 Parabéns! Você clicou no botão!"
        mensagem.color = ft.Colors.GREEN

        # IMPORATANTE: Sempre que modificamos elementos da interface,
        # precisamos chamar page.update() para que as mudanças apareçam na tela
        page.update()

    # Criando nosso botão
    meu_botao = ft.ElevatedButton(
        text="Clique em mim!", # texto que aparece no botão
        on_click=botao_clicado, # função que será executada no clique
        width=200, # largura do botão
        height=50, # altura do botão
        bgcolor=ft.Colors.BLUE, # cor de fundo
        color=ft.Colors.WHITE # cor do texto
    )

    # Adicionando os elementos à página
    page.add(mensagem)
    page.add(meu_botao)

ft.app(target=main)    