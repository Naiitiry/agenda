import flet as ft
import requests
from datetime import datetime

API_BASE_URL = "http://127.0.0.1:5000/api"

def create_new_task(page: ft.Page):

    selected_deadline_text = ft.Text(value="Fecha seleccionada: Ninguna")  # Texto para mostrar la fecha seleccionada
    selected_date = None

    def on_date_selected(e):
        # Cuando el usuario selecciona una fecha, actualizamos el Text
        nonlocal selected_date
        selected_date = e.control.value
        selected_deadline_text.value = f"Fecha seleccionada: {selected_date.strftime('%Y-%m-%d')}"
        page.update()

    def create_task(e):  # Acepta el argumento 'e' aunque no se use
        title = title_input.value
        description = description_input.value
        deadline_datetime = deadline_picker
        
        # Verificar si se ha seleccionado una fecha
        if not selected_date:
            page.snack_bar = ft.SnackBar(ft.Text("Please select a deadline."), bgcolor=ft.colors.RED)
            page.snack_bar.open = True
            page.update()
            return

        # Convertir la fecha seleccionada en un formato adecuado para el backend
        deadline_datetime = selected_date.isoformat()

        try:
            response = requests.post(f'{API_BASE_URL}/create_tasks', json={
                'title': title,
                'description': description,
                'deadline': deadline_datetime, # Enviar en formato ISO 8601
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
        except Exception as ex:
            print(f'El error es: {ex}')

    title_input = ft.TextField(label='Title')
    description_input = ft.TextField(label='Description', border_color=ft.colors.GREEN, multiline=True)
    deadline_picker = ft.ElevatedButton(
        text="Elija fecha limite",
        icon=ft.icons.CALENDAR_MONTH,
        on_click= lambda e: page.open(
            ft.DatePicker(
                first_date=datetime(year=2023, month=10, day=1),
                on_change=on_date_selected
            )
        )
    )
    submit_task = ft.ElevatedButton(text='Create task', on_click=create_task)

    

    return ft.Column(
        controls=[
            ft.Text(value="Por favor ingrese los datos para la nueva tarea:"),
            title_input,
            description_input,
            ft.Text(value="Deadline:"),  # Añadimos la etiqueta manualmente
            deadline_picker,
            selected_deadline_text,
            submit_task
        ]
    )
