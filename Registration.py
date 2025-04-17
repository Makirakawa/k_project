import flet as ft

def main(page: ft.Page):
    page.title = "Face check | Registraion"
    page.window_width = 350
    page.window_height = 550
    page.window_resizable = False
    page.bgcolor = "#1F1F1F"  


    input_bg = "#333333"
    hint_color = "#B0B0B0"
    text_color = "#FFFFFF"
    accent = "#3498db"


    login_input = ft.TextField(label="Логин", bgcolor=input_bg, border_color=accent, color=text_color)
    email_input = ft.TextField(label="Email", bgcolor=input_bg, border_color=accent, color=text_color)
    password_input = ft.TextField(label="Пароль", password=True, can_reveal_password=True, bgcolor=input_bg, border_color=accent, color=text_color)
    repeat_password_input = ft.TextField(label="Повторите пароль", password=True, can_reveal_password=True, bgcolor=input_bg, border_color=accent, color=text_color)

    register_button = ft.ElevatedButton("ЗАРЕГИСТРИРОВАТЬСЯ", bgcolor=accent, color="white", height=50)

    login_text = ft.Text("Уже есть аккаунт? ", color=hint_color, size=13)
    login_link = ft.Text("Войти", color=accent, size=13, weight="bold")


    logo = ft.Image(
        src="https://img.icons8.com/ios-filled/100/user.png",
        width=80,
        height=80,
    )

    content = ft.Column(
        controls=[
            ft.Container(content=logo, alignment=ft.alignment.center, padding=20),
            login_input,
            email_input,
            password_input,
            repeat_password_input,
            ft.Container(register_button, padding=10),
            ft.Row([login_text, login_link], alignment=ft.MainAxisAlignment.CENTER)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
        expand=True,
    )

    page.add(content)

ft.app(target=main)
