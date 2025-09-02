import flet as ft

def main(page: ft.Page):
    page.title = "Contador Completo"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.bgcolor = ft.Colors.BLUE_50  # fundo suave azul

    valor_contador = 0

    # Elementos da interface
    display_contador = ft.Text(
        value="0",
        size=60,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_600,
        text_align=ft.TextAlign.CENTER
    )

    info_contador = ft.Text(
        value="Contador iniciado em 0",
        size=16,
        color=ft.Colors.BLUE_400,
        text_align=ft.TextAlign.CENTER,
        italic=True
    )

    def atualizar_display():
        """Atualiza display e cor baseado no valor"""
        display_contador.value = str(valor_contador)

        if valor_contador > 0: 
            display_contador.color = ft.Colors.BLUE_700
            info_contador.value = "💙 Valor positivo"
        elif valor_contador < 0:
            display_contador.color = ft.Colors.BLUE_900
            info_contador.value = "💙 Valor negativo"
        else: 
            display_contador.color = ft.Colors.BLUE_600
            info_contador.value = "✨ Contador zerado"

        page.update()

    def incrementar(e):
        nonlocal valor_contador
        valor_contador += 1
        atualizar_display()

    def decrementar(e):
        nonlocal valor_contador
        valor_contador -= 1
        atualizar_display()

    def resetar(e):
        nonlocal valor_contador
        valor_contador = 0
        atualizar_display()

    # Botões
    page.add(
        ft.Column(
            controls=[
                ft.Text("🔢 Contador Completo", 
                        size=28, 
                        weight=ft.FontWeight.BOLD, 
                        color=ft.Colors.BLUE_700),
                ft.Container(height=10),
                display_contador,
                info_contador,
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            "➖", 
                            on_click=decrementar, 
                            width=80, height=80,
                            bgcolor=ft.Colors.BLUE_100, 
                            color=ft.Colors.WHITE,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=40)) # arredondado fofo
                        ),
                        ft.ElevatedButton(
                            "➕", 
                            on_click=incrementar, 
                            width=80, height=80,
                            bgcolor=ft.Colors.BLUE_700, 
                            color=ft.Colors.WHITE,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=40))
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=50
                ),
                ft.ElevatedButton(
                    "🔄 Reset", 
                    on_click=resetar, 
                    width=140, height=50,
                    bgcolor=ft.Colors.BLUE_300, 
                    color=ft.Colors.WHITE,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=25))
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=25
        )
    )

ft.app(target=main)
