import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import json
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.button import MDIconButton
from kivy.graphics import Color
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivymd.uix.list import MDList, OneLineListItem, TwoLineIconListItem, TwoLineRightIconListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.chip import MDChip
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivymd.uix.boxlayout import MDBoxLayout
from random import sample, randint
from kivy.metrics import dp


# define o tamanho da tela da janela q vai abrir
Window.size = (375, 667)



#todo o codigo o kivy com kivymd


kv = '''
ScreenManager:
    Screen:
    Screen2:
    signup:
    functions:
    Plan_screen:
    task_screen:
    flash_card_screen:
    criacao_cards
    progress_screen:
    challenge_screen:
    settings_screen:
        

<Screen>:
    name: 'home'
    Image:
        source: "images/background.jpg"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
    FloatLayout:
        MDFillRoundFlatButton:
            text: 'Login'
            size_hint: None, None
            pos_hint: {'center_x': 0.5, 'top': 0.30}
            font_size: '30sp'
            font_name: "C:/Users/luanp/Estuda-/fonts/Roboto-Medium.ttf"
            on_press: root.manager.current = 'profile'
        MDRoundFlatButton:
            text: 'Sign up'
            size_hint: None, None
            pos_hint: {'center_x': 0.5, 'top': 0.40}
            font_size: '25sp'
            on_press: 
                root.manager.current = 'sign'
                app.motivacion_text()
        



<Screen2>:
    name: 'profile'
    Image:
        source: "images/background2.jpg"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    FloatLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Login'
            halign: 'center'
            font_style: 'H2'
            pos_hint: {'top': 1.35}
            font_name: "fonts\Roboto-Medium.ttf"
        MDTextField:
            id: user_text
            hint_text: "Username"
            mode: "round"
            size_hint: None, None
            width: 300
            height: 50
            pos_hint: {'center_x': 0.5, 'top': 0.53}
        MDTextField:
            id: pass_text
            hint_text: "Password"
            password: True
            mode: "round"
            size_hint: None, None
            width: 300
            height: 50
            pos_hint: {'center_x': 0.5, 'top': 0.45}
        MDRaisedButton:
            text: 'Confirm'
            pos_hint: {'center_x': 0.5, 'top': 0.35}
            font_size: '15sp'
            on_release: 
                app.username()
                root.manager.current = 'function-menu'
        MDIconButton:
            icon: "arrow-left"
            size_hint: None, None
            user_font_size: "88sp"
            pos_hint: {"left": 1, 'top': 0.95}
            on_press: root.manager.current = 'home'
            
            
            
<signup>:
    name: 'sign'
    Image:
        source: "images/background2.jpg"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    FloatLayout:
        MDLabel:
            text: 'Register'
            halign: 'center'
            font_style: 'H2'
            pos_hint: {'top': 1.35}
            font_name: "fonts\Roboto-Medium.ttf"
        MDTextField:
            hint_text: 'Username'
            width: 300
            height: 50
            mode: "round"
            pos_hint: {'top': 0.64, 'center_x': 0.5}
            size_hint: None, None
        MDTextField:
            hint_text: 'Password'
            width: 300
            height: 50
            mode: "round"
            size_hint: None, None
            pos_hint: {'top': 0.57, 'center_x': 0.5}
        MDTextField:
            hint_text: 'Password'
            mode: "round"
            width: 300
            height: 50
            pos_hint: {'top': 0.50, 'center_x': 0.5}
            size_hint: None, None
        MDRaisedButton:
            text: 'Confirm'
            size_hint: None, None
            pos_hint: {'top': 0.40, 'center_x': 0.5}
            on_press: root.manager.current = 'function-menu'
        MDIconButton:
            icon: "arrow-left"
            size_hint: None, None
            size: "80dp", "80dp"
            user_font_size: "94sp"
            pos_hint: {"left": 1, 'top': 0.95}
            on_press: root.manager.current = 'home'
            
            
<functions>:
    name: 'function-menu'
    Image:
        id: function_image
        source: "images/background5.jpg"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    BoxLayout:
        orientation: 'vertical'
        padding: '10dp'
        spacing: '10dp'
        FloatLayout:
            size_hint: None, None
            MDIconButton:
                id: btn_0
                icon: "book-clock"
                theme_width: 'Custom'
                theme_height: 'Custom'
                user_font_size: "174sp"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos_hint: {"center_x": 0.5, "center_y": 3}
                font_size: '25sp'
                on_press: root.manager.current = 'Plan'
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1 
                    Ellipse:
                        size: self.size
                        pos: self.pos

            MDIconButton:
                id: btn_1
                icon: "list-box-outline"
                text_color: 1, 1, 1, 1
                theme_text_color: "Custom"
                pos_hint: {"center_x": 1.78, "center_y": 3}
                on_press: 
                    root.manager.current = 'task' 
                    app.random_task()
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Ellipse:
                        size: self.size
                        pos: self.pos

            MDIconButton:
                id: btn_2
                icon: "cards"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos_hint: {"center_x": 3.0, "center_y": 3}
                font_size: '25sp'
                on_press: root.manager.current = 'cards'
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Ellipse:
                        size: self.size
                        pos: self.pos

            MDIconButton:
                id: btn_3
                icon: "trending-up"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos_hint: {"center_x": 0.5, "center_y": 2}
                on_press: 
                    app.progress()
                    root.manager.current = 'progress'
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Ellipse:
                        size: self.size
                        pos: self.pos
                

            MDIconButton:
                id: btn_4
                icon: "bullseye-arrow"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos_hint: {"center_x": 1.78, "center_y": 2}
                on_press: 
                    app.challenge()
                    root.manager.current = 'challenge'
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Ellipse:
                        size: self.size
                        pos: self.pos

            MDIconButton:
                id: btn_5
                icon: "settings-helper"
                text_color: 1, 1, 1, 1
                theme_text_color: "Custom"
                pos_hint: {"center_x": 3.0, "center_y": 2}
                on_press: root.manager.current = 'question-sc'
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Ellipse:
                        size: self.size
                        pos: self.pos

            MDLabel:
                id: text_1
                theme_text_color: "Custom"
                text: "Planning"
                pos_hint: {"center_x": 0.68, "center_y": 2.6}

            MDLabel:
                id: text_2
                text: "Tasks"
                theme_text_color: "Custom"
                pos_hint: {"center_x": 2.073, "center_y": 2.6}

            MDLabel:
                id: text_3
                text: "Flash Card"
                theme_text_color: "Custom"
                pos_hint: {"center_x": 3.14, "center_y": 2.6}

            MDLabel:
                id: text_4
                text: "Progress"
                theme_text_color: "Custom"
                pos_hint: {"center_x": 0.68, "center_y": 1.6}

            MDLabel:
                id: text_5
                text: "Challenges"
                pos_hint: {"center_x": 1.9, "center_y": 1.6}

            MDLabel:
                id: text_6 
                text: "Settings"
                theme_text_color: "Custom"
                pos_hint: {"center_x": 3.20, "center_y": 1.6}
            MDBoxLayout:
                id: menu_t
                size_hint: None, None
                size: "340dp", "100dp"
                pos_hint: {"center_y": 5, "center_x": 1.77}
                md_bg_color: 1, 0, 0, 1
                radius: [20, 20, 20, 20]


                
<Plan_screen>:
    name: 'Plan'
    Image:
        id: plan_image
        source: "images/background5.jpg"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
    FloatLayout:
        MDBoxLayout:
            size_hint: None, None
            size: '340dp', '100dp'
            md_bg_color: 1, 0, 0, 1
            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            radius: [20, 20, 20, 20]
        MDLabel:
            text: 'De'
            font_size: '18sp'
            pos_hint: {'center_x': 0.69, 'center_y': 0.81}
        MDTextButton:
            id: time_selected
            text: "__:__"
            theme_text_color: "Custom"
            text_color: "black"
            font_size: '12sp'
            pos_hint: {'center_x': 0.33, 'center_y': 0.81}
            on_press: app.selector()
        MDLabel:
            text: 'Até'
            font_size: '18sp'
            pos_hint: {'center_x': 0.95, 'center_y': 0.81}
        MDTextButton:
            id: time_selected2
            text: "__:__"
            theme_text_color: "Custom"
            text_color: "black"
            font_size: '12sp'
            pos_hint: {'center_x': 0.63, 'center_y': 0.81}
            on_press: app.selector2()
        MDLabel:
            text: 'Fim'
            font_size: '18sp'
            pos_hint: {'center_x': 1.23, 'center_y': 0.81}
        MDTextButton: 
            text: '+ Select'
            pos_hint: {'center_x': 0.83, 'center_y': 0.75}
            on_press: app.text_hours()
        MDIconButton:
            id: arrow_plan
            icon: "arrow-left"
            theme_text_color: "Custom"
            size_hint: None, None
            size: "80dp", "80dp"
            user_font_size: "94sp"
            pos_hint: {"left": 1, 'top': 0.97}
            on_press: root.manager.current = 'function-menu'
        MDTextField:
            id: text_matery
            hint_text: 'Task'
            width: 300
            height: 50
            mode: "round"
            pos_hint: {'top': 0.64, 'center_x': 0.5}
            size_hint: None, None
            on_text_validate: app.add_matery()
        MDIconButton:
            id: add_matery
            icon: "plus"
            size_hint: None, None
            size: "80dp", "80dp"
            user_font_size: "94sp"
            pos_hint: {"right": 1, 'top': 0.653}
            on_release: app.add_matery()
        
        MDBoxLayout:
            size_hint: None, None
            size: '340dp', '340dp'
            md_bg_color: 1, 0, 0, 1
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            radius: [20, 20, 20, 20]

        ScrollView:
            pos_hint: {'center_x': 0.55, 'center_y': 0.30}
            size_hint: 1, 0.5
            MDList:
                id: lista
        MDBoxLayout:
            size_hint: None, None
            pos_hint: {'center_x': 0.5, 'center_y': 0.68}
            size: '150dp', '50dp'
            md_bg_color: 1, 0, 0, 1
            radius: [12, 12, 12, 12]
            MDLabel:
                id: cronometro
                text: "00:00"
                halign: "left"
            MDIconButton:
                icon: "play"
                on_release: app.start_cronometro()
                halign: "right"
            MDIconButton:
                icon: "pause"
                on_release: app.stop_cronometro()
                halign: "right"




<task_screen>:
    name: 'task'
    Image:
        id: task_image
        source: "images/background5.jpg"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    FloatLayout:
        size_hint: None, None
        MDIconButton:
            id: arrow_task
            icon: "arrow-left"
            size_hint: None, None
            size: "80dp", "80dp"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 100
            pos_hint: {'center_x': 0.3, 'center_y': 6.2}
            on_press: root.manager.current = 'function-menu'

        ScrollView:
            pos_hint: {'center_x': 1.9, 'center_y': 2.5}
            size_hint: 3, 6
            MDList:
                theme_text_color: "Custom"
                id: list_2
                radius: {20, 20, 20, 20}

        MDLabel:
            id: title_task
            text: "Lista de Tarefas"
            pos_hint: {'center_y': 5.9, 'center_x': 1.9}
            font_size: '24sp'
            text_size: None, None
        
        
            

<flash_card_screen>:
    name: 'cards'
    Image:
        id: flash_img
        source: "images/background5.jpg"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    FloatLayout:
        size_hint: None, None
        MDIconButton:
            id: arrow_flash
            icon: "arrow-left"
            theme_text_color: "Custom"
            size: "80dp", "80dp"
            pos_hint: {'center_x': 0.3, 'center_y': 6.2}
            on_press: root.manager.current = 'function-menu'
        ScrollView:
            pos_hint: {'center_x': 1.87, 'center_y': 3}
            size_hint: 3, 6
            MDList:
                id: list_card
        MDIconButton:
            id: plus_flash
            icon: "plus"
            theme_text_color: "Custom"
            text_color: 1, 0, 0, 1
            pos_hint: {'center_x': 3.3, 'center_y': 0.7}
            on_press: root.manager.current = 'criar-cards'
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1
                Ellipse
                    size: self.size
                    pos: self.pos
                    

<criacao_cards>:
    name: 'criar-cards'
    Image:
        id: criar_img
        source: "images/background5.jpg"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    MDFloatLayout:
        orientation: 'vertical'
        size_hint: None, None
        md_bg_color: 1, 0, 0, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size: '340dp', '400dp'
        radius: [20, 20, 20, 20]
        MDLabel:
            text: 'Texto da frente'
            pos_hint: {'center_x': 0.52, 'center_y': 0.89}
        MDLabel:
            text: 'Texto do verso'
            pos_hint: {'center_x': 0.52, 'center_y': 0.59}
        MDTextField:
            id: frente_card
            mode: "round"
            size: '200dp', '100dp'
            pos_hint: {'center_y': 0.8, 'center_x': 0.499}
        MDTextField:
            id: verso_card
            mode: "round"
            size: '200dp', '100dp'
            pos_hint: {'center_y': 0.5, 'center_x': 0.499}
        MDRoundFlatButton:
            text: 'Confirmar'
            on_press: 
                app.flash_card()
                root.manager.current = 'cards'
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        MDLabel:
            text: 'Criação de flash cards'
            pos_hint: {'center_y': 3}
            font_size: '22dp'
            size_hint: None, None
            text_size: None, None

            




<progress_screen>:
    name: 'progress'
    Image:
        id: progress_img
        source: "images/background5.jpg"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    FloatLayout:
        orientation: 'vertical'
        size_hint: None, None
        MDIconButton:
            id: arrow_progress
            theme_text_color: "Custom"
            icon: "arrow-left"
            size: "80dp", "80dp"
            pos_hint: {'center_x': 0.3, 'center_y': 6.2}
            on_press: root.manager.current = 'function-menu'
        MDLabel:
            id: text_progress
            theme_text_color: "Custom"
            text: 'Progresso'
            font_size: '24sp'
            text_size: None, None
            pos_hint: {'center_x': 1.95, 'center_y': 6}
        MDLabel:
            id: text_progress1
            theme_text_color: "Custom"
            text: 'Tarefas concluidas hoje'
            font_size: '18sp'
            pos_hint: {'center_x': 1.9, 'center_y': 5}
            text_size: None, None
        MDLabel:
            id: text_progress2
            theme_text_color: "Custom"
            text: 'Tempo de estudo'
            font_size: '18sp'
            text_size: None, None
            pos_hint: {'center_x': 1.8, 'center_y': 4}
        MDLabel:
            id: text_progress3
            theme_text_color: "Custom"
            text: 'Desafio diario'
            font_size: '18sp'
            text_size: None, None
            pos_hint: {'center_x': 1.77, 'center_y': 3}

        

            

<challenge_screen>:
    name: 'challenge'
    Image:
        id: challenge_img
        source: "images/background5.jpg"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    FloatLayout:
        size_hint: None, None
        MDIconButton:
            id: challenge_arrow
            theme_text_color: "Custom"
            icon: "arrow-left"
            size: "80dp", "80dp"
            pos_hint: {'center_x': 0.3, 'center_y': 6.2}
            on_press: root.manager.current = 'function-menu'
        MDLabel:
            id: text_chl
            text: 'Desafios'
            pos_hint: {'center_y': 6, 'center_x': 1.95}
            font_size: '24sp'
        ScrollView: 
            pos_hint: {'center_x': 1.9, 'center_y': 2.5}
            size_hint: 3, 6
            MDList:
                radius: [20, 20, 20, 20]
                theme_text_color: "Custom"
                id: list3



<settings_screen>:
    name: 'question-sc'
    Image:
        id: settings_img
        source: "images/background5.jpg"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    FloatLayout:
        orientation: 'vertical'
        size_hint: None, None
        MDIconButton:
            id: arrow_settings
            theme_text_color: "Custom"
            icon: "arrow-left"
            pos_hint: {'center_x': 0.3, 'center_y': 6.2}
            size: "80dp", "80dp"
            on_press: root.manager.current = 'function-menu'
        ScrollView:
            pos_hint: {'center_x': 1.9, 'center_y': 3}
            size_hint: 3, 6
            MDList:
                radius: [20, 20, 20, 20]
                id: list4
                TwoLineRightIconListItem:
                    text: 'Tema Claro/Escuro'
                    on_press: app.escuro()
                    IconRightWidget:
                        icon: "theme-light-dark"
                        pos_hint: {'center_y': 0.4}
'''

#telas

class task_screen(Screen): pass

class Screen2(Screen): pass
    
class signup(Screen): pass
   
class functions(Screen): pass

class Plan_screen(Screen): pass

class Screen(Screen): pass

class flash_card_screen(Screen): pass

class criacao_cards(Screen): pass

class progress_screen(Screen): pass 

class challenge_screen(Screen): pass

class settings_screen(Screen): pass





class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)
    
    def username(self):
        text = self.root.get_screen('profile').ids.user_text.text
        print(f"username: {text}")
        print(f"password: {self.root.get_screen('profile').ids.pass_text.text}")

    def selector(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.time_text)
        time_dialog.open()

    def selector2(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.time_select2)
        time_dialog.open()

    def time_text(self, instance, time):
        self.root.get_screen('Plan').ids.time_selected.text = str(time)

    def time_select2(self, instance, time):
        self.root.get_screen('Plan').ids.time_selected2.text = str(time)

    def text_hours(self):
        hour = self.root.get_screen('Plan').ids.time_selected.text.replace(":", "")
        hour2 = self.root.get_screen('Plan').ids.time_selected2.text.replace(":", "")
        hour3 = hour.replace("0", "")
        hour4 = hour2.replace("0", "")
        print(f"Real texto: {self.root.get_screen('Plan').ids.time_selected.text} Horario de inicio: {hour.replace("0", "")} horario final {hour2.replace("0", "")} e tempo estimativo: horas {int(hour4) - int(hour3)}")

    def add_matery(self):
        texto = self.root.get_screen('Plan').ids.text_matery.text.strip()
        if texto:
            self.root.get_screen('Plan').ids.lista.add_widget(
                OneLineListItem(text=texto)
            )
            self.root.get_screen('Plan').ids.text_matery.text = ""

    def random_task(self):
        desc = ["Fique 30 minutos no aplicativo", "Faça 10 questões", "Estude por 1 hora", "Faça 3 flash-cards do que estudou hoje", "Faça 5 Questões", "Conclua as três tarefas", "Faça 15 questões"]
        txt_num = sample(desc, k=3)
        self.root.get_screen('task').ids.list_2.clear_widgets()
        for i, txt_desc in enumerate(txt_num, 1):
            self.root.get_screen('task').ids.list_2.add_widget (
            TwoLineRightIconListItem(id="text_list",text=f"Tarefa {i}", secondary_text=txt_desc, theme_text_color="Custom", text_color="black")
            )
            

            
        

            
    def motivacion_text(self):
        lista = ["Um passo de cada vez.",
                 "Disciplina gera resultado.",
                 "Seu esforço vale a pena.\n"]
        random = randint(0, len(lista) - 1)
        texto = MDLabel(
            padding=15,
            text=f" \"{lista[random]}\"",
            pos_hint={'center_x': 3, 'center_y': 0.5},
            )
        self.root.get_screen('function-menu').ids.menu_t.add_widget(texto)


    def challenge(self): 
        desc = ["Acerte 5 questões", "Acerte 10 questões", "Resolva 3 questões"]
        txt_random = sample(desc, k=3)
        self.root.get_screen('challenge').ids.list3.clear_widgets()
        for i, txt_desc in enumerate(txt_random, 1):
            self.root.get_screen('challenge').ids.list3.add_widget (
            TwoLineIconListItem(text=f"Desafio {i}", secondary_text=txt_desc)
            )

    def flash_card(self):
        frente = self.root.get_screen('criar-cards').ids.frente_card.text
        verso = self.root.get_screen('criar-cards').ids.verso_card.text
        print(f"Frente = {frente}, verso = {verso}")
        box = MDBoxLayout(
            orientation="vertical",
            size_hint_y=None,
            spacing=dp(8),
            padding=dp(12),
            size=(dp(200), dp(400)),
            md_bg_color=(1, 0, 0, 1),
            radius=[12, 12, 12, 12],
        )
        espaco = MDBoxLayout(
            size=(dp(200), dp(30)),
            size_hint_y=None
        )
        inc = [1]
        box.add_widget(MDLabel(text=frente, halign="center", font_style="H6"))
        def mostrar_verso(*args):
            verso_text = box.add_widget(MDLabel(text=verso, halign="center"))
            box.remove_widget(btn)
        btn = MDFillRoundFlatButton(text="Mostrar verso", halign="center", valign="bottom", pos_hint={"center_x": 0.5}, size_hint_y=None)
        btn.bind(on_release=mostrar_verso)
        box.add_widget(btn)
        self.root.get_screen('cards').ids.list_card.add_widget(box)
        self.root.get_screen('cards').ids.list_card.add_widget(espaco)

    def progress(self):
        tarefas = ProgressBar(max=4, value=2,
                            size_hint=(None, None),
                            size=(dp(250), dp(50)),
                            pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.root.get_screen('progress').add_widget(tarefas)
        tempo = ProgressBar(value=3, max= 4,
                            size_hint=(None, None),
                            size=(dp(250), dp(50)),
                            pos_hint={'center_x': 0.5, 'center_y': 0.54} 
                             )
        self.root.get_screen('progress').add_widget(tempo)
        desafios = ProgressBar(value=2, max=5,
            size_hint=(None, None),
            size=(dp(250), dp(50)),
            pos_hint={'center_x': 0.5, 'center_y': 0.39}
        )
        self.root.get_screen('progress').add_widget(desafios)

        
        
    def tempo(self):
        self.contador = 0
        while self.contador:
            self.contador += 1
            self.root.get_screen('Plan').ids.cronometro.text = str(self.contador)


    def start_cronometro(self):
        if not getattr(self, "_cron_event", None):
            self._cron_event = Clock.schedule_interval(self._tick, 1)

    def stop_cronometro(self):
        if getattr(self, "_cron_event", None):
            self._cron_event.cancel()
            self._cron_event = None

    def _tick(self, dt):
        self.count = getattr(self, "count", 0) + 1
        m, s = divmod(self.count, 60)
        try:
            self.root.get_screen('Plan').ids.cronometro.text = f"{m:02d}:{s:02d}"
        except Exception:
            pass

    #modo dark
    def escuro(self):
        bkg1 = "images/background8.jpg"
        bkg2 = "images/background7.jpg"
        bkg3 = "images/background6.jpg"
        branco_bkg = "images/background3.jpg"
        preto_icon = 0, 0, 0, 1
        branco_icon = "#FFFFFF"
        self.root.get_screen('Plan').ids.plan_image.source = (bkg1)
        self.root.get_screen('task').ids.task_image.source = (bkg1)
        self.root.get_screen('cards').ids.flash_img.source = (bkg1)
        self.root.get_screen('criar-cards').ids.criar_img.source = (bkg1)
        self.root.get_screen('progress').ids.progress_img.source = (bkg1)
        self.root.get_screen('challenge').ids.challenge_img.source = (bkg1)
        self.root.get_screen('question-sc').ids.settings_img.source = (bkg1)
        #cores dos icones modo dark
        self.root.get_screen('function-menu').ids.function_image.source = (bkg1)
        self.root.get_screen('function-menu').ids.btn_0.text_color = (preto_icon); self.root.get_screen('function-menu').ids.btn_0.md_bg_color = (branco_icon)
        self.root.get_screen('function-menu').ids.btn_1.text_color = (preto_icon); self.root.get_screen('function-menu').ids.btn_1.md_bg_color = (branco_icon)
        self.root.get_screen('function-menu').ids.btn_2.text_color = (preto_icon); self.root.get_screen('function-menu').ids.btn_2.md_bg_color = (branco_icon)
        self.root.get_screen('function-menu').ids.btn_3.text_color = (preto_icon); self.root.get_screen('function-menu').ids.btn_3.md_bg_color = (branco_icon)
        self.root.get_screen('function-menu').ids.btn_4.text_color = (preto_icon); self.root.get_screen('function-menu').ids.btn_4.md_bg_color = (branco_icon)
        self.root.get_screen('function-menu').ids.btn_5.text_color = (preto_icon); self.root.get_screen('function-menu').ids.btn_5.md_bg_color = (branco_icon)
        self.root.get_screen('Plan').ids.arrow_plan.text_color = (branco_icon)
        self.root.get_screen('cards').ids.arrow_flash.text_color = (branco_icon)
        self.root.get_screen('progress').ids.arrow_progress.text_color = (branco_icon)
        self.root.get_screen('challenge').ids.challenge_arrow.text_color = (branco_icon)
        self.root.get_screen('question-sc').ids.arrow_settings.text_color = (branco_icon)
        self.root.get_screen('cards').ids.plus_flash.md_bg_color = (branco_icon)
        self.root.get_screen('task').ids.list_2.md_bg_color = ("#131313FF")
        self.root.get_screen('challenge').ids.list3.md_bg_color = ("#0F0F0F")
        self.root.get_screen('question-sc').ids.list4.md_bg_color = ("#0F0F0F")
        self.root.get_screen('task').ids.arrow_task.text_color = (branco_icon)
        self.root.get_screen('task').ids.title_task.color = (branco_icon)
        self.root.get_screen('progress').ids.text_progress.color = (branco_icon)
        self.root.get_screen('progress').ids.text_progress1.color = (branco_icon)
        self.root.get_screen('progress').ids.text_progress2.color = (branco_icon)
        self.root.get_screen('progress').ids.text_progress3.color = (branco_icon)
        
        #textos da tela de funções do modo dark
        self.root.get_screen('challenge').ids.text_chl.color = (branco_icon)
        self.root.get_screen('function-menu').ids.text_1.color = (branco_icon)
        self.root.get_screen('function-menu').ids.text_2.color = (branco_icon)
        self.root.get_screen('function-menu').ids.text_3.color = (branco_icon)
        self.root.get_screen('function-menu').ids.text_4.color = (branco_icon)
        self.root.get_screen('function-menu').ids.text_5.color = (branco_icon)
        self.root.get_screen('function-menu').ids.text_6.color = (branco_icon)
    
        

        

    

if __name__ == '__main__':
    MyApp().run()