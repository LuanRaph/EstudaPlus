import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import json
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.button import MDIconButton
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.chip import MDChip
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivymd.uix.boxlayout import MDBoxLayout
from random import sample, randint
from kivy.metrics import dp


Window.size = (375, 667)


KV = '''
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
            font_name: "fonts\Roboto-Medium.ttf"
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
                icon: "trending-up"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos_hint: {"center_x": 0.5, "center_y": 2}
                on_press: root.manager.current = 'progress'
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Ellipse:
                        size: self.size
                        pos: self.pos

            MDIconButton:
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
                text: "Planning"
                pos_hint: {"center_x": 0.68, "center_y": 2.6}

            MDLabel:
                text: "Tasks"
                pos_hint: {"center_x": 2.073, "center_y": 2.6}

            MDLabel:
                text: "Flash Card"
                pos_hint: {"center_x": 3.14, "center_y": 2.6}

            MDLabel:
                text: "Progress"
                pos_hint: {"center_x": 0.68, "center_y": 1.6}

            MDLabel:
                text: "Challenges"
                pos_hint: {"center_x": 1.9, "center_y": 1.6}

            MDLabel: 
                text: "Settings"
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
            icon: "arrow-left"
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
        source: "images/background5.jpg"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    FloatLayout:
        size_hint: None, None
        MDIconButton:
            icon: "arrow-left"
            size_hint: None, None
            size: "80dp", "80dp"
            pos_hint: {'center_x': 0.3, 'center_y': 6.2}
            on_press: root.manager.current = 'function-menu'

        ScrollView:
            pos_hint: {'center_x': 1.9, 'center_y': 2.5}
            size_hint: 3, 6
            MDList:
                id: list_2

        MDLabel:
            text: "Lista de"
            pos_hint: {'center_y': 5.9, 'center_x': 1.5}
            font_size: '24sp'
        
        MDLabel:
            text: "Tarefas"
            pos_hint: {'center_x': 2.4, 'center_y': 5.9}
            font_size: '24sp'
            

<flash_card_screen>:
    name: 'cards'
    Image:
        source: "images/background5.jpg"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    FloatLayout:
        size_hint: None, None
        MDIconButton:
            icon: "arrow-left"
            size: "80dp", "80dp"
            pos_hint: {'center_x': 0.3, 'center_y': 6.2}
            on_press: root.manager.current = 'function-menu'
        ScrollView:
            pos_hint: {'center_x': 1.87, 'center_y': 3}
            size_hint: 3, 6
            MDList:
                id: list_card
        MDIconButton:
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
        source: "images/background5.jpg"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    FloatLayout:
        orientation: 'vertical'
        size_hint: None, None
        MDIconButton:
            icon: "arrow-left"
            size: "80dp", "80dp"
            pos_hint: {'center_x': 0.3, 'center_y': 6.2}
            on_press: root.manager.current = 'function-menu'
        MDLabel:
            text: 'Progresso'
            font_size: '24sp'
            text_size: None, None
            pos_hint: {'center_x': 1.95, 'center_y': 6}
        MDLabel:
            text: 'Tarefas concluidas hoje'
            font_size: '18sp'
            pos_hint: {'center_x': 1.9, 'center_y': 5}
            text_size: None, None
        

            

<challenge_screen>:
    name: 'challenge'
    Image:
        source: "images/background5.jpg"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    FloatLayout:
        size_hint: None, None
        MDIconButton:
            icon: "arrow-left"
            size: "80dp", "80dp"
            pos_hint: {'center_x': 0.3, 'center_y': 6.2}
            on_press: root.manager.current = 'function-menu'
        MDLabel:
            text: 'Desafios'
            pos_hint: {'center_y': 6, 'center_x': 1.95}
            font_size: '24sp'
        ScrollView: 
            pos_hint: {'center_x': 1.9, 'center_y': 2.5}
            size_hint: 3, 6
            MDList:
                id: list3



<settings_screen>:
    name: 'question-sc'
    Image:
        source: "images/background5.jpg"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    FloatLayout
        size_hint: None, None
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {'center_x': 0.3, 'center_y': 6.2}
            size: "80dp", "80dp"
            on_press: root.manager.current = 'function-menu'


    
            

            
            
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
        return Builder.load_string(KV)
    
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
            TwoLineListItem(text=f"Tarefa {i}", secondary_text=txt_desc),
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
            TwoLineListItem(text=f"Desafio {i}", secondary_text=txt_desc)
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
        tempo = ProgressBar(max=4, value=8)
        


        
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

        

    










    

if __name__ == '__main__':
    MyApp().run()