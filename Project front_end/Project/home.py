from turtle import color
import flet as ft
from flet_core.icons import EXPAND


class Home(ft.UserControl):
    def build(self):
        return ft.Row(
            [
                ft.Container(
                    
                    image_src=(f"https://abrakadabra.fun/uploads/posts/2022-01/1642992163_5-abrakadabra-fun-p-fon-dlya-vakansii-na-rabotu-5.jpg"),
                    height=1080,
                    width=1920,
                    
                    content=ft.Card(
                       
                        content=ft.Container(
                            
                            height=400,
                            content=ft.Column(
                                [
                                    ft.Row(
                                        [ft.Text("Реєстрація",weight=ft.FontWeight.BOLD, size=20)],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ), 

                                     ft.Row(
                                        [ft.TextField(label="І'мя", prefix_icon=ft.icons.PERSON)],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ), 
                                       
                                      ft.Row(
                                        [ft.TextField(label="Email", prefix_icon=ft.icons.EMAIL)],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ), 
                              
                                       ft.Row(
                                        [ft.TextField(label="Пароль", password=True, can_reveal_password=True, prefix_icon=ft.icons.LOCK)],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),

                                       ft.Row(
                                        [ft.Checkbox(label="Я погоджуюсь з умовами обробки\n перснальних данних", value=False, fill_color=ft.colors.GREEN)],
                                        
                                    ),

                                    ft.Row(
                                        [ft.ElevatedButton("Далі", width=120,style=ft.ButtonStyle(side=ft.BorderSide(2, ft.colors.BLUE)))],
                                        alignment=ft.MainAxisAlignment.END,
                                    ),
                                ]
                            ),
                            width=400,
                            padding=25,
                        )
                    ),
                    expand=True,
                    alignment=ft.alignment.center
                )
            ],
            alignment=ft.alignment.center
        )
        