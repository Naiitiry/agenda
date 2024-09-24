import flet as ft
import requests

API_BASE_URL = "http://127.0.0.1:5000"

def login_page(page: ft.Page, navigate_to_register):
    def login(e):
        username = username_input.value
        password = password_input.value
        try:
            response = requests.post(f"{API_BASE_URL}/auth/login", json={
                "username": username,
                "password": password
                })
            if response.status_code == 200:
                jwt_token = response.json().get('access_token')
                if jwt_token:
                    page.session.set("jwt_token", jwt_token)
                    page.update()
                else:
                    print("Error: No se recibió el token JWT.")
            else:
                print("Error en el inicio de sesión.")
                
            if response.status_code == 200:
                data = response.json()
                print("Data received:", data)
                # Forzando la redirección sin la verificación de 'Login successful'
                page.session.set("logged_in", True)
                page.session.set("username", username)
                print("Logged in:", page.session.get("logged_in"))
                print("Username:", page.session.get("username"))
                page.go("/home/home")
                page.update()
            else:
                result_text.value = "Login failed! Please check your credentials."
            page.update()
        except requests.exceptions.RequestException as error:
            result_text.value = f"Request failed: {error}"
        page.update()

    def go_to_register(e):
        navigate_to_register()

    username_input = ft.TextField(
                                    label="Username",
                                    label_style=ft.TextStyle(
                                        color=ft.colors.WHITE
                                    ),
                                    border=ft.InputBorder.UNDERLINE,
                                    color=ft.colors.WHITE,
                                    cursor_color=ft.colors.WHITE,
                                    bgcolor=ft.colors.TRANSPARENT,
                                    filled=True,
                                    focused_color=ft.colors.WHITE,
                                    )
    password_input = ft.TextField(
                                label="Password", 
                                label_style=ft.TextStyle(
                                        color=ft.colors.WHITE
                                    ),
                                password=True, 
                                can_reveal_password=True,
                                border=ft.InputBorder.UNDERLINE,
                                color=ft.colors.WHITE,
                                cursor_color=ft.colors.WHITE,
                                bgcolor=ft.colors.TRANSPARENT,
                                filled=True,
                                focused_color=ft.colors.WHITE
                                )
    result_text = ft.Text("")
    login_button = ft.ElevatedButton(text="Login", on_click=login)
    register_button = ft.ElevatedButton(text="Go to Register", on_click=go_to_register)

    login_color = ft.Container(
        content=ft.Column(
                controls=[
                    ft.Text("Login", size=30, color=ft.colors.WHITE),
                    username_input,
                    password_input,
                    login_button,
                    result_text,
                    register_button
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            padding=20,
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["0xff6482AD","0xff7FA1C3"],
                stops=[0.1,1.0]
            ),
            )
    
    return login_color