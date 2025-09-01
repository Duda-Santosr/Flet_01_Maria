import flet as ft

def main(page: ft.Page):
    """
    Função principal que será executada quando o app iniciar.
    O parâmetro 'page' representa a tela/página do nosso app.
    """

    #  Configurações básicas da página
    page.title = "Meu Primeiro App Flet" #Título que aparece na aba do navegador
    page.padding = 20 # Espaçamento interno da página 

    # Criando nosso primeiro elemento: um texto
    meu_texto = ft.Text(
        value="🎉 Hello World! (Primeiro app com Flet!)", # o texto que será exibido
        size=24, # tamanho da fonte
        color=ft.Colors.BLUE, # cor do texto
        weight=ft.FontWeight.BOLD, # texto em negrito
        text_align=ft.TextAlign.CENTER # centralizar o texto
    )

    # Adicionando o texto à nossa página
    page.add(meu_texto)

    # Vamos adicionar mais alguns elementos para tornar mais interessante
    page.add(
        ft.Text("Bem-vindo ao mundo do desenvolvimento mobile!", size=16),
        ft.Text("Com Flet, você pode criar apps incríveis! 📱", size=16, color=ft.Colors.GREEN)
    )

# Esta linha inicia nossa aplicativo, chamando a função mais
ft.app(target=main) 