import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_height=400
    page.window_width=400

    page.title = 'Counter'

btn = ft.ElevatedButton("Click me!")
page.add(btn)

   
ft.app(target=main)


