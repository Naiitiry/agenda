import flet as ft
from components.description import create_appbar
from components.add_task import add_task_user
from components.user_card import *
from task.task import task


def home_page(page: ft.Page, on_logout: callable):
    if not page.session.get("logged_in"):
        page.go("/auth/login")  # Redirige a la página de login si no está autenticado

    username = page.session.get("username")  # Obtener el nombre de usuario de la sesión
    email = page.session.get('email')

    def handle_logout():
        # Eliminar sesión y redirigir al login
        print("Deslogeo exitoso!")
        on_logout
        page.session.set("logged_in", False)
        page.session.remove('username')
        page.session.clear()
        page.go("/auth/login")  # Redirige al login después del logout

    # Traer las tareas
    tareas = task(page)

    # Botón de Crear tareas
    crear_tareas = add_task_user(page)

    # AppBar
    app_bar_user = create_appbar(page,username,email,handle_logout)

    # Añadir componentes a la página
    return ft.Column(
        controls=[
            app_bar_user,
            ft.Text(f"Bienvenido a la página principal {username}", size=24),
            crear_tareas,
            tareas,
        ]
    )