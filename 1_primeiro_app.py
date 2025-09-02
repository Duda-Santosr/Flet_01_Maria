import flet as ft

def main(page: ft.Page):
    """
    Função principal que será executada quando o app iniciar.
    O parâmetro 'page' representa a tela/página do nosso app.
    """

    #  Configurações básicas da página
    page.title = "Meu Primeiro App Flet" #Título que aparece na aba do navegador
    page.padding = 20 # Espaçamento interno da página 
    page.bgcolor = ft.Colors.PINK_50 # Cor de fundo mais suave
    page.horizontal_alignment = "center" # Centralizar conteúdo na horizontal
    page.vertical_alignment = "center"   # Centralizar conteúdo na vertical

    # Criando nosso primeiro elemento: um texto
    meu_texto = ft.Text(
        value="🎉 Hello World! (Primeiro app com Flet!)", # o texto que será exibido
        size=24, # tamanho da fonte
        color=ft.Colors.PINK_900, # cor do texto
        weight=ft.FontWeight.BOLD, # texto em negrito
        text_align=ft.TextAlign.CENTER # centralizar o texto
    )

    # Adicionando o texto à nossa página
    page.add(meu_texto)

    # Vamos adicionar mais alguns elementos para tornar mais interessante
    page.add(
        ft.Text("Bem-vindo ao mundo do desenvolvimento mobile!", size=18, color=ft.Colors.BLACK87, italic=True),
        ft.Text("Com Flet, você pode criar apps incríveis! 📱", size=18, color=ft.Colors.PINK_700, weight=ft.FontWeight.W_600)
    )

    # Criando um botão estilizado (mais feminino e delicado)
    botao = ft.ElevatedButton(
        text="✨ Clique Aqui ✨",
        bgcolor=ft.Colors.PINK_300,
        color=ft.Colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=30), # bem arredondado, tipo "pill button"
            elevation={"": 4}, # sombra mais leve
            padding={"": 15}   # botão maior e mais "fofo"
        ),
        on_click=lambda e: page.snack_bar.open()
    )

    # SnackBar para feedback
    page.snack_bar = ft.SnackBar(ft.Text("Você clicou no botão! 🌸"), open=False)

    # Adicionando o botão em um container delicado
    page.add(
        ft.Container(
            content=botao,
            padding=15,
            margin=10,
            bgcolor=ft.Colors.PINK_100,
            border_radius=25,
            shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.PINK_200)
        )
    )

# Esta linha inicia nossa aplicativo, chamando a função mais
ft.app(target=main)
