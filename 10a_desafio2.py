import flet as ft

def main(page: ft.Page):
    # Configurações iniciais da página
    page.title = "Loja Virtual Mini"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.scroll = ft.ScrollMode.AUTO # permite rolagem automática
    page.bgcolor = ft.Colors.GREY_50 # cor de fundo da página

    # Estado da aplicação - variáveis que armazenam dados do carrinho
    carrinho = [] # lista que armazena os produtos no carrinho
    total_carrinho = 0.0 # valor total dos produtos no carrinho

    # Elementos da interface (declarando primeiro para serem acessíveis nas funções)
    # Grid que exibe os produtos em formato de grade
    area_produtos = ft.GridView(
        expand=1, # expande para ocupar espaço disponível
        runs_count=2, # 2 colunas de produtos
        max_extent=180, # largura máxima de cada item
        child_aspect_ratio=0.9, # proporção altura/largura dos cards
        spacing= 15, # espaçamento entre cards horizontalmente
        run_spacing=15 # espaçamento entre cards verticalmente
    )
    # Textos que mostram informações do carrinho
    contador_carrinho = ft.Text("Carrinho (0)", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700)
    total_texto = ft.Text("Total: R$ 0,00", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700)
    # Lista que exibe os itens do carrinho
    lista_carrinho = ft.ListView(height=150, spacing=5)
    # Texto para exibir notificações ao usuário
    notificacao = ft.Text("", size=14, color=ft.Colors.BLUE_600, text_align=ft.TextAlign.CENTER)

    def adicionar_ao_carrinho(nome, preco):
        """Adiciona um produto ao carrinho de compras"""
        nonlocal total_carrinho # Permite modificar a variável global total_carrinho
        # Adiciona o produto como dicionário na lista do carrinho
        carrinho.apend({"nome": nome, "preço": preco})
        # Soma e preço do produto ao total
        total_carrinho += preco
        # Atualiza a interface do carrinho
        atualizar_carrinho()
        #Mostra notificações de sucesso
        mostra_notificacao(f"✅ {nome} adicionado!")

    def criar_card_produto(nome, preco, categoria, emoji, cor):
        """Cria um card de produto reutilizável que funciona como botão"""
        return ft.Container(
            content=ft.Column([
                # Emoji do produto
                ft.Text(emoji, size=40, text_align=ft.TextAlign.CENTER),
                # Nome do produto
                ft.Text(
                    nome, 
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                    max_line=2, # Permite quebra de linha para nomes longos
                    overflow=ft.TextOverFlow.ELLIPSIS # adiciona ... se muito longo
                ),
                # Preço do produto
                ft.Text(
                    f"R$ {preco:.2f}",
                    size=14,
                    color=ft.Colors.WHITE70,
                    text_align=ft.TextAlign.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10 # espaçamento entre elementos da coluna
            ),
            bgcolor=cor, # cor de fundo específica do produto
            padding=20, # espaçamento interno
            border_radius=15, # bordas arredondadas
            width=160, # largura fixa do card
            height=180, # altura fixa do card
            # Sombra para dar profundidade
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=8,
                color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK)
            ),
            # Tornando o card inteiro clicável - chama função de adicionar o carrinho
            on_click=lambda e, n=nome, p=preco: adicionar_ao_carrinho(n, p),
            # Efeito visual de ondulação ao clicar (ripple effect)
            ink=True,
            # Animação suave para transições
            animate=ft.animation.Animation(300, ft.AnimationCurve.EASE_OUT)
        )

    # Lista de produtos disponíveis na loja
    # Cada produto é um dicionário com informações como nome, preço, categoria, emoji e cor
    produtos = [
        {"nome": "Smartphone", "preco": 899.99, "categoria": "Eletrônicos", "emoji": "📱", "cor": ft.Colors.BLUE_600},
        {"nome": "Notebook", "preco": 2499.90, "categoria": "Eletrônicos", "emoji": "💻", "cor": ft.Colors.PURPLE_600},
        {"nome": "Tênis", "preco": 299.99, "categoria": "Roupas", "emoji": "👟", "cor": ft.Colors.GREEN_600},
        {"nome": "Camiseta", "preco": 89.90, "categoria": "Roupas", "emoji": "👕", "cor": ft.Colors.ORANGE_600},
        {"nome": "Livro", "preco": 45.00, "categoria": "Educação", "emoji": "📚", "cor": ft.Colors.BROWN_600},
        {"nome": "Fone", "preco": 199.99, "categoria": "Eletrônicos", "emoji": "🎧", "cor": ft.Colors.RED_600},
        {"nome": "Relógio", "preco": 350.00, "categoria": "Acessórios", "emoji": "⌚", "cor": ft.Colors.TEAL_600},
        {"nome": "Óculos", "preco": 250.00, "categoria": "Acessórios", "emoji": "🕶️", "cor": ft.Colors.INDIGO_600}
    ]   

    # Elementos de filtro da interface
    # Dropdown para filtrar por categoria
    filtro_categoria = ft.Dropdown(
        label= "Categoria",
        width= 150,
        value="Todas", # valor padrão
        options=[
            ft.dropdown.Option("Todas"),
            ft.dropdown.Option("Eletrônicos"),
            ft.dropdown.Option("Roupas"),
            ft.dropdown.Option("Educação"),
            ft.dropdown.Option("Acessórios")
        ]
    )

    # Dropdown para filtrar por faixa de preço
    filtro_preco = ft.Dropdown(
        label= "Preço",
        width= 150,
        value="Todos", # valor padrão
        options=[
            ft.dropdown.Option("Todos"),
            ft.dropdown.Option("Até R$ 100"),
            ft.dropdown.Option("R$ 100-500"),
            ft.dropdown.Option("Acima de R$ 500")
        ]
    )