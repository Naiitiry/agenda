import flet as ft
import requests
from components.theme import current_theme_mode

API_BASE_URL = "http://127.0.0.1:5000/api"

def task(page: ft.Page):
    def fetch_tasks():
        response = requests.get(f"{API_BASE_URL}/all_tasks", headers={"Authorization": f"Bearer {page.session.get('jwt_token')}"})
        print(f"Token JWT: {page.session.get('jwt_token')}")
        if response.status_code == 200:
            tasks = response.json()
            # Establecer colores basados en el tema actual
            if current_theme_mode == ft.ThemeMode.LIGHT:
                container_bgcolor = ft.colors.LIGHT_BLUE_50
                text_color = ft.colors.BLACK
            else:
                container_bgcolor = ft.colors.BLUE_GREY_900
                text_color = ft.colors.WHITE
            if tasks:
                task_list = ft.ListView(expand=1, spacing=10, padding=20)
                for task in tasks:
                    task_list.controls.append(
                        ft.Container(
                            ft.Text(f"{task['title']} - Due: {task['deadline']}", size=18, color=text_color),
                            padding=10,
                            border_radius=5,
                            bgcolor=container_bgcolor,
                        )
                    )
                return task_list
            else:
                return ft.Text("No hay tareas pendientes", size=18, color=ft.colors.RED)
        else:
            return ft.Text("Error al cargar las tareas", size=18, color=ft.colors.RED)

    # Retorna el componente con las tareas o el mensaje de error.
    return fetch_tasks()
