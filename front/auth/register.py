import flet as ft
import requests
from components.theme import themes_change

# URL base de tu API Flask
API_BASE_URL = "http://127.0.0.1:5000"

def register_page(page: ft.Page, navigate_to_login):
    def register(e):
        # Similar al login, pero con la ruta de registro
        username = username_input.value
        password = password_input.value
        email = email_input.value
        try:
            response = requests.post(f"{API_BASE_URL}/auth/register", json={
                "username": username,
                "password": password,
                "email": email
            })

            print(f"Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")

            if response.status_code == 201:
                result_text.value = "Registration successful! You can now login."
            else:
                result_text.value = "Registration failed! Please try again."

            # Si la respuesta es JSON, la mostramos
            try:
                print(f"Response Content: {response.json()}")
            except ValueError:
                print("No JSON in response.")
            page.update()
        except requests.exceptions.RequestException as error:
            result_text.value = f"Request failed: {error}"
        page.update()
    
    # Función para navegar a la página de login
    def go_to_login(e):
        navigate_to_login()

    username_input = ft.TextField(label="Username", border="underline")
    password_input = ft.TextField(label="Password", password=True,
                                can_reveal_password=True,)
    email_input = ft.TextField(label="Email",border_color=ft.colors.BROWN)
    result_text = ft.Text("")
    register_button = ft.ElevatedButton(text="Register", on_click=register,color=ft.colors.BLUE)
    login_button = ft.ElevatedButton(text="Go to Login", on_click=go_to_login)

    # Cambio de tema
    cambio_de_tema = themes_change(page)

    # Agrega los componentes a la página
    register_color = ft.Container(
        content = ft.Column(
                controls=[
                    #cambio_de_tema,
                    ft.Text("Register", size=30, color=ft.colors.WHITE),
                    username_input,
                    password_input,
                    email_input,
                    register_button,
                    result_text,
                    login_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                expand=True,
                padding=20,
                alignment=ft.alignment.center,
                gradient=ft.LinearGradient(
                        begin=ft.alignment.bottom_left,
                        end=ft.alignment.top_right,
                        colors=["0xffFC819E","0xffF7418F"],
                        stops=[1.0,1.0]
                        ),
                )

    return register_color