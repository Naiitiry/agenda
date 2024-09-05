import flet as ft
import requests

API_BASE_URL = "http://127.0.0.1:5000/api"

def add_task(page: ft.Page):
    def go_to_add_task(e):
        page.go('/create_tasks')
    
    boton_crear = ft.IconButton(
        icon=ft.icons.ADD_BUSINESS,
        icon_color=ft.colors.BLUE_400,
        icon_size=30,
        tooltip="Crear tarea",
        on_click=go_to_add_task
    )
    return boton_crear