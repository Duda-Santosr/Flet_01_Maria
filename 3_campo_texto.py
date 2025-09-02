import flet as ft

def main(page: ft.Page):
    page.title = "Campo de Texto"
    page.bgcolor = ft.Colors.GREY_100
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # Texto de resposta (inicialmente vazio)
    resposta = ft.Text(
        value="",
        size=18,
        text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.W_500,
    )

    # Campo de entrada
    campo_nome = ft.TextField(
        label="Digite seu nome",
        width=300,
        border_color=ft.Colors.DEEP_PURPLE_200,
        focused_border_color=ft.Colors.DEEP_PURPLE_500,
        cursor_color=ft.Colors.DEEP_PURPLE,
        prefix_icon=ft.Icons.PERSON,
    )

    # Função do botão
    def processar_nome(evento):
        nome_digitado = campo_nome.value.strip()

        if not nome_digitado:
            resposta.value = "⚠️ Por favor, digite seu nome!"
            resposta.color = ft.Colors.RED
        elif len(nome_digitado) < 2:
            resposta.value = "⚠️ Nome muito curto!"
            resposta.color = ft.Colors.ORANGE
        else:
            resposta.value = f"✨ Olá, {nome_digitado}! Bem-vindo(a)!"
            resposta.color = ft.Colors.DEEP_PURPLE_700
        page.update()

    # Botão estilizado
    botao_ok = ft.FilledButton(
        text="Confirmar",
        icon=ft.Icons.CHECK_CIRCLE,
        on_click=processar_nome,
        width=200,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=30),
            bgcolor=ft.Colors.DEEP_PURPLE_400,
            color=ft.Colors.WHITE,
            elevation=6,
        ),
    )

    # Card que agrupa os elementos
    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "👋 Seja bem-vindo!",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.DEEP_PURPLE_700,
                    ),
                    campo_nome,
                    botao_ok,
                    resposta,
                ],
                alignment="center",
                horizontal_alignment="center",
                spacing=20,
            ),
            padding=30,
            border_radius=20,
            bgcolor=ft.Colors.WHITE,
        ),
        elevation=8,
    )

    page.add(card)


ft.app(target=main)