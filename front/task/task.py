import flet as ft
import requests

API_BASE_URL = "http://127.0.0.1:5000"

def main(page: ft.Page):
    def fetch_tasks(page: ft.Page):
        response = requests.get(f"{API_BASE_URL}/tasks", headers={"Authorization": f"Bearer {page.session.get('jwt_token')}"})
        
        if response.status_code == 200:
            tasks = response.json()
            task_list.controls = [
                ft.Text(f"{task['title']} - Due: {task['deadline']}", size=18)
                for task in tasks
            ]
        else:
            task_list.controls = [ft.Text("Failed to load tasks.", size=18)]
        
        page.update()

    task_list = ft.Column()
    fetch_tasks(page)  # Llamar esta función para cargar las tareas en la interfaz
