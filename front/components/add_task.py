import flet as ft
import requests

API_BASE_URL = "http://127.0.0.1:5000/api"

def add_task_user(page: ft.Page):
    def go_to_add_task(e):
        try:
            # Simplemente redirige a la página de creación de tarea
            page.go('/task/create_task')
        except Exception as ex:
            print(ex)
    boton_crear = ft.IconButton(
        icon=ft.icons.ADD_BOX_OUTLINED,
        icon_color=ft.colors.BLUE_400,
        icon_size=30,
        tooltip="Crear tarea",
        on_click=go_to_add_task
    )
    return ft.Column(controls=[boton_crear])