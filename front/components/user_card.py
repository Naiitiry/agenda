import flet as ft
import requests

API_BASE_URL = "http://127.0.0.1:5000"

def user_card(page: ft.Page, username: str, on_logout: callable) -> ft.Column:

    def logout(e):
        try:
            # Realizar una solicitud POST al backend para cerrar sesión
            response = requests.post(f"{API_BASE_URL}/auth/logout", headers={"Content-Type": "application/json"})

            if response.status_code == 200:
                # Si el logout es exitoso, ejecutar la función de logout en el frontend
                on_logout()
                # Opcional: Redirigir a la página de inicio de sesión
                page.go("/auth/login")  # Asegúrate de que esta ruta esté configurada en tu aplicación Flet
            else:
                # Mostrar mensaje de error
                if page.snack_bar is None:
                    page.snack_bar = ft.SnackBar(ft.Text("Logout failed, please try again."), bgcolor=ft.colors.RED)
                else:
                    page.snack_bar.content = ft.Text("Logout failed, please try again.")
                    page.snack_bar.bgcolor = ft.colors.RED
                
                page.snack_bar.open = True
                page.update()
        except Exception as ex:
            # Manejar excepciones y mostrar mensaje de error
            if page.snack_bar is None:
                page.snack_bar = ft.SnackBar(ft.Text(f"An error occurred: {str(ex)}"), bgcolor=ft.colors.RED)
            else:
                page.snack_bar.content = ft.Text(f"An error occurred: {str(ex)}")
                page.snack_bar.bgcolor = ft.colors.RED
                
            page.snack_bar.open = True
            page.update()

    # Crear componentes de la tarjeta
    user_info = ft.Text(f"{username}", size=20)
    logout_button = ft.ElevatedButton(text="Logout", on_click=logout)

    # Crear la tarjeta
    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[user_info, logout_button],
                spacing=10
            ),
            padding=10,
            border_radius=10,
            bgcolor="#f0f0f0",
            border=ft.border_radius.all(10)
        ),
    )

    return 