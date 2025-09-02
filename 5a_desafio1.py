import flet as ft

def main(page: ft.Page):
    page.title = "Criador de Perfil"
    page.padding = ft.padding.only(top=40, left=20, bottom=20) # padding superior para área segura
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = ft.Colors.GREY_100  # fundo clean moderno
    page.horizontal_alignment = "center" # centralizar na horizontal
    page.vertical_alignment = "center"   # centralizar na vertical

    # Campos do formulário
    campo_nome = ft.TextField(
        label="Nome completo", 
        width=300, 
        border_color=ft.Colors.GREY_400, 
        focused_border_color=ft.Colors.GREEN_600
    )
    campo_idade = ft.TextField(
        label="Idade", 
        width=300, 
        keyboard_type=ft.KeyboardType.NUMBER, 
        border_color=ft.Colors.GREY_400, 
        focused_border_color=ft.Colors.GREEN_600
    )

    dropdown_hobby = ft.Dropdown(
        label="Hobby favorito",
        width=300,
        border_color=ft.Colors.GREY_400,
        focused_border_color=ft.Colors.GREEN_600,
        bgcolor=ft.Colors.WHITE,
        options=[
            ft.dropdown.Option("Leitura 📚"),
            ft.dropdown.Option("Esportes ⚽"),
            ft.dropdown.Option("Música 🎵"),
            ft.dropdown.Option("Jogos 🎮"),
            ft.dropdown.Option("Culinária 👩‍🍳"),
            ft.dropdown.Option("Arte 🎨")
        ]
    )

    # Área do perfil criado (inicialmente oculta)
    cartao_perfil = ft.Container(
        content=ft.Text("Preencha os dados acima"),
        bgcolor=ft.Colors.GREY_50,
        padding=25,
        border_radius=15,
        width=350,
        visible=False,
        shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.GREY_300)
    )

    def criar_perfil(evento):
        if not campo_nome.value or len(campo_nome.value) < 2:
            mostrar_erro("Nome deve ter pelo menos 2 caracteres")
            return
        
        if not campo_idade.value:
            mostrar_erro("Idade é obrigatória")
            return
        
        try:
            idade = int(campo_idade.value)
            if idade < 1 or idade > 120:
                mostrar_erro("Idade deve estar entre 1 e 120 anos")
                return
        except ValueError:
            mostrar_erro("Idade deve ser um número")  
            return

        if not dropdown_hobby.value:
            mostrar_erro("Selecione um hobby")  
            return
        
        criar_cartao_perfil()

    def mostrar_erro(mensagem):
        cartao_perfil.content = ft.Column([
            ft.Icon(ft.Icons.ERROR, color=ft.Colors.RED, size=40),
            ft.Text(f"⚠️ {mensagem}", color=ft.Colors.RED, text_align=ft.TextAlign.CENTER)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER) 
        cartao_perfil.bgcolor = ft.Colors.RED_50
        cartao_perfil.visible = True
        page.update()

    def criar_cartao_perfil():
        idade = int(campo_idade.value)
        if idade < 18:
            categoria = "Jovem"
            cor_icone = ft.Colors.GREEN
        elif idade < 60:
            categoria = "Adulto"    
            cor_icone = ft.Colors.GREEN_600
        else:
            categoria = "Experiente"  
            cor_icone = ft.Colors.GREEN_800

        cartao_perfil.content = ft.Column([
            ft.Icon(ft.Icons.PERSON, size=60, color=cor_icone),
            ft.Text(campo_nome.value, size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_900),
            ft.Text(f"{idade} anos - {categoria}", size=18, color=ft.Colors.GREY_700),
            ft.Text(f"Hobby: {dropdown_hobby.value}", size=15, color=ft.Colors.GREY_600),
            ft.Container(
                content = ft.Text("Perfil criado com sucesso! ✨", color=ft.Colors.WHITE),
                bgcolor=cor_icone,
                padding=10,
                border_radius=20
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10) 

        cartao_perfil.bgcolor = ft.Colors.WHITE
        cartao_perfil.visible = True
        page.update()

    def limpar_campos(evento):
        campo_nome.value = ""
        campo_idade.value = ""
        dropdown_hobby.value = None
        cartao_perfil.visible = False
        page.update()

    linha_botoes = ft.Row([
        ft.ElevatedButton(
            "✨ Criar Perfil",
            on_click=criar_perfil,
            bgcolor=ft.Colors.GREEN_500,
            color=ft.Colors.WHITE,
            width=140,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=30))
        ),
        ft.OutlinedButton(
            "🧹 Limpar",
            on_click=limpar_campos,
            width=140,
            style=ft.ButtonStyle(
                side={ft.ControlState.DEFAULT: ft.BorderSide(1, ft.Colors.GREEN_400)},
                shape=ft.RoundedRectangleBorder(radius=30),
                color={ft.ControlState.DEFAULT: ft.Colors.GREEN_600}
            )
        )
    ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)

    card_principal = ft.Container(
        content=ft.Column([
            ft.Text("👤 Criador de Perfil", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_800, text_align=ft.TextAlign.CENTER),
            ft.Text(
                "Preencha seus dados e crie um perfil estiloso.",
                size=15, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER
            ),
            ft.Container(height=15),
            campo_nome,
            campo_idade,
            dropdown_hobby,
            linha_botoes,
            ft.Container(height=20),
            cartao_perfil
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
        width=420,
        padding=30,
        bgcolor=ft.Colors.WHITE,
        border_radius=16,
        shadow=ft.BoxShadow(blur_radius=18, spread_radius=2, color=ft.Colors.GREY_300)
    )

    # ✅ Centraliza o card no meio da tela
    page.add(
        ft.Row(
            [card_principal],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

ft.app(target=main)
