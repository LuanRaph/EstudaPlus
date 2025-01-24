from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.button import MDRoundFlatButton
from kivy.core.window import Window

# Define o layout das telas usando a linguagem KV

Window.size = (1080, 2200)

robot_m = '/storage/emulated/0/Estuda+/fonts/Roboto-Medium.ttf'

KV = '''
ScreenManager:
    Screen
    Screen2:
    signup:
    functions:
        
        

<Screen>:
    name: 'home'
    Image:
        source: '/storage/emulated/0/Estuda+/images/background.jpg'
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
    FloatLayout:
        MDFillRoundFlatButton:
            text: 'Login'
            size_hint: None, None
            pos_hint: {'center_x': 0.5, 'top': 0.30}
            font_size: '50sp'
            font_name: '/storage/emulated/0/Estuda+/fonts/Roboto-Medium.ttf'
            on_press: root.manager.current = 'profile'
        MDRoundFlatButton:
            text: 'Sign up'
            size_hint: None, None
            pos_hint: {'center_x': 0.5, 'top': 0.40}
            font_size: '41sp'
            on_press: root.manager.current = 'sign'
            
        



<Screen2>:
    name: 'profile'
    Image:
        source: '/storage/emulated/0/Estuda+/images/background2.jpg'
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    FloatLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Login'
            halign: 'center'
            font_style: 'H1'
            pos_hint: {'top': 1.35}
            font_name: '/storage/emulated/0/Estuda+/fonts/Roboto-Medium.ttf'
        MDRaisedButton:
            text: 'Confirm'
            pos_hint: {'center_x': 0.5, 'top': 0.40}
            font_size: '30sp'
        MDTextField:
            hint_text: "Username"
            mode: "round"
            size_hint: None, None
            width: 800
            height: 50
            pos_hint: {'center_x': 0.5, 'top': 0.5}
        MDTextField:
            hint_text: "Password"
            mode: "round"
            size_hint: None, None
            width: 800
            height: 50
            pos_hint: {'center_x': 0.5, 'top': 0.45}
        MDIconButton:
            icon: "arrow-left"
            size_hint: None, None
            size: "60dp", "60dp"
            pos_hint: {"left": 1, 'top': 0.95}
            on_press: root.manager.current = 'home'
            
            
            
<signup>:
    name: 'sign'
    Image:
        source: '/storage/emulated/0/Estuda+/images/background2.jpg'
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    FloatLayout:
        MDLabel:
            text: 'Register'
            halign: 'center'
            font_style: 'H1'
            pos_hint: {'top': 1.35}
            font_name: '/storage/emulated/0/Estuda+/fonts/Roboto-Medium.ttf'
        MDTextField:
            hint_text: 'Username'
            width: 800
            height: 50
            mode: "round"
            pos_hint: {'top': 0.60, 'center_x': 0.5}
            size_hint: None, None
        MDTextField:
            hint_text: 'Password'
            width: 800
            height: 50
            mode: "round"
            size_hint: None, None
            pos_hint: {'top': 0.55, 'center_x': 0.5}
        MDTextField:
            hint_text: 'Password'
            mode: "round"
            width: 800
            height: 50
            pos_hint: {'top': 0.50, 'center_x': 0.5}
            size_hint: None, None
        MDRaisedButton:
            text: 'Confirm'
            size_hint: None, None
            pos_hint: {'top': 0.40, 'center_x': 0.5}
            on_press: root.manager.current = 'fuction-menu'
        MDIconButton:
            icon: "arrow-left"
            size_hint: None, None
            size: "60dp", "60dp"
            pos_hint: {"left": 1, 'top': 0.95}
            on_press: root.manager.current = 'home'
            
            
<functions>:
    name: 'fuction-menu'
    Image:
        source: '/storage/emulated/0/Estuda+/images/background3.jpg'
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    FloatLayout:
        MDLabel:
            text: 'MENU'
            font_name: '/storage/emulated/0/Estuda+/fonts/Roboto-Medium.ttf'
            pos_hint: {'center_x': 0.5, 'top': 1.35}
            

            
            
'''

#telas
class Screen(Screen):
    pass

class Screen2(Screen):
    pass
    
class signup(Screen):
    pass
   
class functions(Screen):
    pass


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    MyApp().run()