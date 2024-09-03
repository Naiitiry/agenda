import flet as ft
from auth.login import login_page
from auth.register import register_page
from home.home import home_page

def main(page: ft.Page):
    page.title = "Task Management App"
    page.window.width = 800
    page.window.height = 600
    page.window.resizable = False

    def route_change(route):
        page.views.clear()
        if page.route == '/auth/login':
            login = login_page(page,lambda: page.go('/auth/register'))
            page.views.append(login)

        if page.route == '/auth/register':
            register2 = register_page(page,lambda: page.go('/auth/login'))
            page.views.append(register2)

        if page.route == '/home/home':
            home = home_page(page, lambda: page.go('/auth/login'))
            page.views.append(home)

        page.update()
        
    # Función para manejar el pop de las vistas
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # Configurar el manejador de cambios de ruta
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Inicia en la ruta de login
    page.go('/auth/login')

ft.app(target=main)