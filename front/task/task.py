import flet as ft
import requests

API_BASE_URL = "http://127.0.0.1:5000"

def task(page: ft.Page):
    # def fetch_tasks(page: ft.Page):
    #     response = requests.get(f"{API_BASE_URL}/tasks/all_tasks", headers={"Authorization": f"Bearer {page.session.get('jwt_token')}"})
        
    #     if response.status_code == 200:
    #         tasks = response.json()
    #         task_list = ft.ListView(expand=1)
    #         for task in tasks:
    #             task_list.controls.append(
    #                 ft.Text(f"{task['title']} - Due: {task['deadline']}", size=18)
    #             )
            
    #         # [
    #         #     ft.Text(f"{task['title']} - Due: {task['deadline']}", size=18)
    #         #     for task in tasks
    #         # ]
    #         return task_list
    #     else:
    #         task_list = ft.Text("Carga de tareas fallida")
    #         #task_list.controls.append(ft.Text("Carga de tareas fallida"))
    #         return task_list
        
    # fetch_tasks(page)
    # page.update()
    def fetch_tasks(page: ft.Page):
        pass

        #fetch_tasks(page)  # Llamar esta función para cargar las tareas en la interfaz
        #return task_list
