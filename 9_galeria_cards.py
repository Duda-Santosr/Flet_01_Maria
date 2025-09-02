# Importa a biblioteca Flet para criar interfaces gráficas
import flet as ft

def criar_card_animal(nome, emoji, descricao, cor):
    """
    Função que cria um card (cartão) visual para cada animal.
    """
    return ft.Container(
        content=ft.Column([
            # Emoji grande no topo do card
            ft.Text(emoji, size=40, text_align=ft.TextAlign.CENTER),
            # Nome do animal em negrito e branco
            ft.Text(nome, size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            # Descrição menor e com transparência
            ft.Text(descricao, size=12, color=ft.Colors.WHITE70, text_align=ft.TextAlign.CENTER)
        ], 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza tudo horizontalmente
        spacing=8  # Espaço de 8 pixels entre cada elemento
        ),
        bgcolor=cor,  # Cor de fundo do card (varia por animal)
        padding=20,   # Espaçamento interno de 20 pixels
        border_radius=15,  # Bordas arredondadas
        width=160,    # Largura fixa do card
        height=140,   # Altura fixa do card
        # Sombra para dar efeito de profundidade
        shadow=ft.BoxShadow(
            spread_radius=1,  # Expansão da sombra
            blur_radius=8,    # Intensidade do desfoque
            color=ft.Colors.with_opacity(0.25, ft.Colors.BLACK)  # Cinza suave para sombra
        )
    )

def main(page: ft.Page):
    """
    Função principal que define toda a interface do aplicativo.
    Esta função é chamada quando o app inicia.
    """
    
    # Configurações básicas da página/janela
    page.title = "Galeria com Filtros"
    page.bgcolor = ft.Colors.GREY_100  # Fundo cinza claro para um visual moderno
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.scroll = ft.ScrollMode.AUTO
    
    # Lista com todos os dados dos animais
    animais = [
        {"nome": "Gato", "emoji": "🐱", "descricao": "Felino carinhoso", "cor": ft.Colors.GREY_700, "categoria": "Doméstico", "tamanho": "Médio"},
        {"nome": "Cachorro", "emoji": "🐶", "descricao": "Melhor amigo", "cor": ft.Colors.GREY_800, "categoria": "Doméstico", "tamanho": "Grande"},
        {"nome": "Peixe", "emoji": "🐟", "descricao": "Animal aquático", "cor": ft.Colors.GREY_600, "categoria": "Aquático", "tamanho": "Pequeno"},
        {"nome": "Pássaro", "emoji": "🐦", "descricao": "Voa livremente", "cor": ft.Colors.GREY_500, "categoria": "Selvagem", "tamanho": "Pequeno"},
        {"nome": "Coelho", "emoji": "🐰", "descricao": "Saltita pelos campos", "cor": ft.Colors.GREY_700, "categoria": "Doméstico", "tamanho": "Pequeno"},
        {"nome": "Leão", "emoji": "🦁", "descricao": "Rei da selva", "cor": ft.Colors.GREY_800, "categoria": "Selvagem", "tamanho": "Grande"},
        {"nome": "Elefante", "emoji": "🐘", "descricao": "Gigante gentil", "cor": ft.Colors.GREY_600, "categoria": "Selvagem", "tamanho": "Grande"},
        {"nome": "Golfinho", "emoji": "🐬", "descricao": "Mamífero marinho", "cor": ft.Colors.GREY_700, "categoria": "Aquático", "tamanho": "Grande"}
    ]
    
    # GridView para os cards
    area_cards = ft.GridView(
        expand=1,
        runs_count=2,
        max_extent=180,
        child_aspect_ratio=1.0,
        spacing=15,
        run_spacing=15
    )
    
    # Dropdowns para filtro
    filtro_categoria = ft.Dropdown(
        label="Categoria",
        width=150,
        value="Todos",
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.GREY_400,
        border_radius=8,
        color=ft.Colors.GREY_900,
        options=[
            ft.dropdown.Option("Todos"), 
            ft.dropdown.Option("Doméstico"), 
            ft.dropdown.Option("Selvagem"), 
            ft.dropdown.Option("Aquático")
        ]
    )
    
    filtro_tamanho = ft.Dropdown(
        label="Tamanho",
        width=150,
        value="Todos",
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.GREY_400,
        border_radius=8,
        color=ft.Colors.GREY_900,
        options=[
            ft.dropdown.Option("Todos"), 
            ft.dropdown.Option("Pequeno"), 
            ft.dropdown.Option("Médio"), 
            ft.dropdown.Option("Grande")
        ]
    )
    
    campo_busca = ft.TextField(
        label="Buscar",
        width=150,
        prefix_icon=ft.Icons.SEARCH,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.GREY_400,
        border_radius=8,
        color=ft.Colors.GREY_900
    )
    
    contador = ft.Text(
        "",
        size=14,
        color=ft.Colors.GREY_700,
        text_align=ft.TextAlign.CENTER
    )
    
    def carregar_cards(e=None):
        """
        Carrega os cards aplicando filtros.
        """
        area_cards.controls.clear()
        categoria = filtro_categoria.value
        tamanho = filtro_tamanho.value
        busca = (campo_busca.value or "").lower()
        
        filtrados = [
            a for a in animais 
            if (categoria == "Todos" or a["categoria"] == categoria)
            and (tamanho == "Todos" or a["tamanho"] == tamanho)
            and (not busca or busca in a["nome"].lower())
        ]
        
        for animal in filtrados:
            area_cards.controls.append(
                criar_card_animal(animal["nome"], animal["emoji"], animal["descricao"], animal["cor"])
            )
        
        total_filtrados = len(filtrados)
        total_geral = len(animais)
        
        contador.value = (
            f"Mostrando todos os {total_filtrados} animais"
            if total_filtrados == total_geral
            else f"Encontrados {total_filtrados} de {total_geral} animais"
        )
        page.update()
    
    def limpar_filtros(e):
        """
        Limpa os filtros e retorna à lista completa.
        """
        filtro_categoria.value = "Todos"
        filtro_tamanho.value = "Todos"
        campo_busca.value = ""
        carregar_cards()
    
    for controle in [filtro_categoria, filtro_tamanho, campo_busca]:
        controle.on_change = carregar_cards
    
    carregar_cards()
    
    page.add(
        ft.Column([
            ft.Text(
                "🦁 Zoológico Virtual",
                size=28,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                color=ft.Colors.GREY_900
            ),
            ft.Text(
                "Explore diferentes categorias de animais",
                size=16,
                color=ft.Colors.GREY_700,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Row([filtro_categoria, filtro_tamanho],
                   alignment=ft.MainAxisAlignment.CENTER,
                   spacing=20),
            ft.Row([
                campo_busca,
                ft.ElevatedButton(
                    "🧹 Limpar",
                    on_click=limpar_filtros,
                    bgcolor=ft.Colors.GREY_600,
                    color=ft.Colors.WHITE,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
                )
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            contador,
            ft.Container(
                content=area_cards,
                height=400,
                border=ft.border.all(1, ft.Colors.GREY_400),
                border_radius=12,
                padding=10,
                bgcolor=ft.Colors.WHITE,
                shadow=ft.BoxShadow(blur_radius=6, color=ft.Colors.GREY_300)
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15)
    )

# Inicia o aplicativo
ft.app(target=main)
