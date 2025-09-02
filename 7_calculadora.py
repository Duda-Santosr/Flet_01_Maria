import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Simples"
    page.bgcolor = ft.Colors.PINK_50
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)

    # Campos e elementos
    numero1 = ft.TextField(
        label="Primeiro número",
        width=250,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_color=ft.Colors.PINK_300,
        border_radius=12,
        color=ft.Colors.PINK_900
    )

    numero2 = ft.TextField(
        label="Segundo número",
        width=250,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_color=ft.Colors.PINK_300,
        border_radius=12,
        color=ft.Colors.PINK_900
    )

    operacao = ft.Dropdown(
        label="Operação",
        width=250,
        border_color=ft.Colors.PINK_300,
        border_radius=12,
        color=ft.Colors.PINK_900,
        options=[
            ft.dropdown.Option("Soma"),
            ft.dropdown.Option("Subtração"),
            ft.dropdown.Option("Multiplicação"),
            ft.dropdown.Option("Divisão")
        ]
    )

    resultado = ft.Text(
        "Resultado aparecerá aqui",
        size=22,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.PINK_700,
        weight=ft.FontWeight.BOLD
    )

    # Função para calcular
    def calcular(e):
        try:
            num1, num2, op = float(numero1.value), float(numero2.value), operacao.value

            if not op:
                resultado.value, resultado.color = "⚠️ Selecione uma operação", ft.Colors.ORANGE
            elif op == "Divisão" and num2 == 0:
                resultado.value, resultado.color = "❌ Erro: Divisão por zero", ft.Colors.RED
            else:
                simbolos = {
                    "Soma": ("+", num1 + num2),
                    "Subtração": ("-", num1 - num2),
                    "Multiplicação": ("×", num1 * num2),
                    "Divisão": ("÷", num1 / num2)
                }
                simbolo, res = simbolos[op]
                resultado.value, resultado.color = f"{num1} {simbolo} {num2} = {res:.2f}", ft.Colors.PINK_800
        except ValueError:
            resultado.value, resultado.color = "❌ Digite números válidos!", ft.Colors.RED
        page.update()

    # Função para limpar os campos
    def limpar(e):
        numero1.value = numero2.value = operacao.value = ""
        resultado.value, resultado.color = "✨ Campos limpos!", ft.Colors.PINK_500
        page.update()

    # Interface
    page.add(
        ft.Column([
            ft.Text(
                "🧮 Calculadora ",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.PINK_800
            ),
            numero1,
            numero2,
            operacao,
            ft.Row([
                ft.ElevatedButton(
                    "💖 Calcular",
                    on_click=calcular,
                    width=150,
                    bgcolor=ft.Colors.PINK_300,
                    color=ft.Colors.WHITE,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))
                ),
                ft.ElevatedButton(
                    "🧼 Limpar",
                    on_click=limpar,
                    width=150,
                    bgcolor=ft.Colors.PINK_200,
                    color=ft.Colors.PINK_900,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))
                )
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=25),
            ft.Divider(color=ft.Colors.PINK_200, thickness=2),
            resultado
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=25
        )
    )

ft.app(target=main)
