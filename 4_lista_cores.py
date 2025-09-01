import flet as ft

def main(page: ft.Page):
    page.title = "Seletor de Cores"
    page.padding = 20

    # Container que mudará de cor (como uma caixa colorida)
    caixa_colorida = ft.Container(
        content=ft.Text(
            "Escolha uma cor! 🎨",
            color=ft.Colors.WHITE,
            size=18,
            text_align=ft.TextAlign.CENTER
        ),
        bgcolor=ft.Colors.GREY, # Cor inicial
        width=300,
        height=100,
        border_radius=10, # Bordas arredondadas
        alignment=ft.alignment.center # Centralizar o texto
    )

    def cor_selecionada(evento):
        """
        Esta função é executada sempre que o usuario escolhe uma cor.
        """
        # Peganddo qual cor foi selecionada
        cor_selecionada = evento.control.value

        # Dicionario com as cores disponiveis
        # É como uma "lista de correspondencia" entre nome e cor real
        cores_disponiveis = {
            "Azul": ft.Colors.BLUE,
            "Verde": ft.Colors.GREEN,
            "Vermelho": ft.Colors.RED,
            "Roxo": ft.Colors.PURPLE,
            "Laranja": ft.Colors.ORANGE,
            "Rosa": ft.Colors.PINK,
        }

        # Mudando a cor da caixa 
        caixa_colorida.bgcolor = cores_disponiveis[cor_selecionada]
        caixa_colorida.content.value = f"Cor selecionada: {cor_selecionada} 🦄"

        page.update()

    # Criando a lista suspensa (dropdown)
    selector_cor = ft.Dropdown(
        label="Escolha uma cor",
        width=200,
        options=[
            ft.dropdown.Option("Azul"),
            ft.dropdown.Option("Verde"),
            ft.dropdown.Option("Vermelho"),
            ft.dropdown.Option("Roxo"),
            ft.dropdown.Option("Laranja"),
            ft.dropdown.Option("Rosa")
        ],
        on_change=cor_selecionada # Função que será executada quando escolher         
    )  

    # Adicionando elementos à pagina 
    page.add(
        ft.Text("Seletor de Cores Mágico! ✨", size=24, weight=ft.FontWeight.BOLD),
        selector_cor,
        caixa_colorida
    )

ft.app(target=main)