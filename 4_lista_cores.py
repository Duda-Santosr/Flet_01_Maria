import flet as ft

def main(page: ft.Page):
    page.title = "Seletor de Cores"
    page.padding = 20
    page.bgcolor = ft.LinearGradient(  # Fundo gradiente lilás-rosa
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=[ft.Colors.PURPLE_100, ft.Colors.PINK_100]
    )
    page.horizontal_alignment = "center"  # Centralizar conteúdo na horizontal
    page.vertical_alignment = "center"    # Centralizar conteúdo na vertical

    # Container que mudará de cor (como uma caixa colorida)
    caixa_colorida = ft.Container(
        content=ft.Text(
            "Escolha uma cor! 🎨",
            color=ft.Colors.WHITE,
            size=18,
            text_align=ft.TextAlign.CENTER
        ),
        bgcolor=ft.Colors.PURPLE_300, # Cor inicial em lilás
        width=300,
        height=120,
        border_radius=20, # Bordas arredondadas mais suaves
        alignment=ft.alignment.center, # Centralizar o texto
        shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.PURPLE_200) # Sombra lilás suave
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
        caixa_colorida.content.value = f"Cor selecionada: {cor_selecionada} 💜✨"

        page.update()

    # Criando a lista suspensa (dropdown)
    selector_cor = ft.Dropdown(
        label="🌷 Escolha uma cor mágica ✨",
        width=220,
        bgcolor=ft.Colors.PINK_50, # Fundo suave no dropdown
        border_color=ft.Colors.PURPLE_300,
        focused_border_color=ft.Colors.PURPLE_500,
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

    # Card para agrupar tudo e deixar mais delicado
    card = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "💜 Seletor de Cores Mágico 🌸",
                    size=26,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.PURPLE_900,
                    text_align=ft.TextAlign.CENTER
                ),
                selector_cor,
                caixa_colorida
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=20
        ),
        padding=30,
        bgcolor=ft.Colors.WHITE,
        border_radius=25,
        shadow=ft.BoxShadow(blur_radius=20, color=ft.Colors.PURPLE_200),
    )

    # Adicionando elementos à pagina 
    page.add(card)

ft.app(target=main)
