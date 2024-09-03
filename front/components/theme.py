import flet as ft

def themes_change(page: ft.Page):
    # Iniciar en modo claro
    page.theme_mode = ft.ThemeMode.LIGHT

    # Alternar entre claro y oscuro
    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            button_change_theme.icon = ft.icons.LIGHT_MODE
            button_change_theme.style = ft.ButtonStyle(
                color=ft.colors.WHITE
            )
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            button_change_theme.icon = ft.icons.DARK_MODE
            button_change_theme.style = ft.ButtonStyle(
                color=ft.colors.BLACK
            )
        page.update()

    # Cambiar iconos de botón claro y oscuro
    button_change_theme = ft.IconButton(
        on_click=change_theme,
        icon=ft.icons.DARK_MODE if page.theme_mode == ft.ThemeMode.LIGHT else ft.icons.LIGHT_MODE,
        style=ft.ButtonStyle(
            # Cambiar de color
            color=ft.colors.BLACK
        )
    )
    # Barra de navegaci+on para el botón
    nav_bar = ft.AppBar(
        title=ft.Text("Agenda"),
        bgcolor=ft.colors.TRANSPARENT,
        actions=[
            button_change_theme
        ]
    )

    return nav_bar