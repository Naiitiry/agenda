import flet as ft
from components.user_card import get_full_user_data,get_logout_button,get_user_info
from components.theme import get_theme_button

def create_appbar(page: ft.Page, username: str, email: str, on_logout: callable)->ft.AppBar:
    theme_button = get_theme_button(page)

    def dialog_close(e):
        modal.open = False
        page.update()

    def show_user_info(e):
        modal.open = True
        page.overlay.append(modal)
        page.update()

    modal = ft.AlertDialog(
        title=ft.Text(value='Información del usuario'),
        modal=True,
        content=get_full_user_data(username,email),
        actions=[
            ft.TextButton(text='Cerrar',on_click=lambda e:dialog_close(e))
        ]
    )

    user_avatar_button = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(text=username, on_click=show_user_info),
            ft.PopupMenuItem(text="Logout", on_click=lambda e:on_logout)
        ],
        icon=ft.icons.ACCOUNT_CIRCLE
    )

    # Menú desplegable
    app_bar = ft.AppBar(
        title=ft.Text(value='Home'),
        bgcolor=ft.colors.TRANSPARENT,
        actions=[
            theme_button,
            user_avatar_button
        ]
    )

    return app_bar