import flet as ft
import requests
from datetime import datetime

API_BASE_URL = "http://127.0.0.1:5000/api"

def main(page: ft.Page):

    def create_task(e):
        title = title_input.value
        description = description_input.value
        deadline = deadline_picker.value
        # Convertir la fecha seleccionada en un formato adecuado para el backend
        deadline_datetime = datetime.strptime(deadline, "%Y-%m-%d").isoformat()
        try:
            response = requests.post(f'{API_BASE_URL}/create_tasks',json={
                'title':title,
                'description':description,
                'deadline':deadline_datetime.isoformat(), # Enviar en formato ISO 8601
            }, 
            headers={"Authorization": f"Bearer {page.session.get('jwt_token')}"})

            if response.status_code == 201:
                page.snack_bar = ft.SnackBar(ft.Text("Task created successfully!"), bgcolor=ft.colors.GREEN)
                page.snack_bar.open = True
            else:
                print(response.json())
                page.snack_bar = ft.SnackBar(ft.Text("Failed to create task."), bgcolor=ft.colors.RED)
                page.snack_bar.open = True

            page.update()
        except Exception as e:
            print(f'{e}')

    title_input = ft.TextField(label='Title')
    description_input = ft.TextField(label='Description',border_color=ft.colors.GREEN, multiline=True)
    deadline_picker = ft.DatePicker(label='Deadline',on_change=lambda e: page.update())
    submit_task = ft.ElevatedButton(text='Create task',on_click=create_task)

    return ft.Column(
        controls=[
            ft.Text(value="Por favor ingrese los datos para la nueva tarea:"),
            title_input,
            description_input,
            deadline_picker,
            submit_task
        ]
    )

