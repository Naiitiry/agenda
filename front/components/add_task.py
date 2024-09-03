import flet as ft
import requests

API_BASE_URL = "http://127.0.0.1:5000"

def add_task(page: ft.Page):
    def go_to_add_task(e):
        try:
            response = requests.get(f'{API_BASE_URL}/tasks/create_')
        except Exception as e:
            print(e)
    
    return