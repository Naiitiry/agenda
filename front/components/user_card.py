import flet as ft
import requests

API_BASE_URL = "http://127.0.0.1:5000/api"

# Función para obtener el nombre de usuario
def get_user_info(username: str, email: str):
    return ft.Row(
        controls=[
            ft.Text(f"Username: {username}"),
            ft.Text(f"Email: {email}"),
        ]
    )

def get_logout_button(page: ft.Page, on_logout: callable) -> ft.Column:

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

    return ft.ElevatedButton(text='Logout',on_click=logout())

# Función para obtener todos los datos del usuario (ej. para ver todos los datos completos)
def get_full_user_data(username: str, email: str) -> ft.Column:
    return ft.Column(
        controls=[
            ft.Text(f"Username: {username}", size=20),
            ft.Text(f"Email: {email}", size=20),
            # Puedes añadir más datos aquí si lo deseas
        ]
    )