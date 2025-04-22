import flet as ft

def main(page: ft.Page):
    #page.title = "Face check | Registraion"
    page.window.width = 450
    page.window.height = 650
    page.window.resizable = False
    page.bgcolor = "#1F1F1F"  
    page.window.title_bar_hidden = True
    page.window.title_bar_buttons_hidden = True

    input_bg = "#333333"
    hint_color = "#00AAFF"
    text_color = "#FFFFFF"
    accent = "#3498db"

    page.add(
        ft.Row(
            [
                ft.WindowDragArea(ft.Container(ft.Text("Face check | Registraion"), padding=5), expand=True),
                ft.IconButton(ft.Icons.CLOSE, on_click=lambda _: page.window.close())
            ]
        )
    )


    login_input = ft.TextField(label="Логин", bgcolor=input_bg, border_color=accent, color=text_color)
    email_input = ft.TextField(label="Email", bgcolor=input_bg, border_color=accent, color=text_color)
    password_input = ft.TextField(label="Пароль", password=True, can_reveal_password=True, bgcolor=input_bg, border_color=accent, color=text_color)
    repeat_password_input = ft.TextField(label="Повторите пароль", password=True, can_reveal_password=True, bgcolor=input_bg, border_color=accent, color=text_color)

    register_button = ft.ElevatedButton("ЗАРЕГИСТРИРОВАТЬСЯ", bgcolor=hint_color, color="white", height=50, width=300)

    login_text = ft.Text("Уже есть аккаунт? ", color=text_color, size=13)
    login_link = ft.Text("Войти", color=accent, size=13, weight="bold")
    
    # logo = ft.Image(
    #     src="C:\Users\m3ddi\Desktop\k_reg\logo\ic_baseline-face.png",
    #     width="80",
    #     height="80",
    #     )

    content = ft.Column(
        controls=[
            ft.Container( alignment=ft.alignment.center, padding=20),
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
