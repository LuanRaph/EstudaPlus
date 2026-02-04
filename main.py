import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.utils import platform as kivy_platform
import json
from kivy.app import App
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
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
from kivymd.uix.list import MDList, OneLineListItem, TwoLineIconListItem, TwoLineRightIconListItem, IconRightWidgetWithoutTouch
from kivymd.uix.list import IconRightWidget
from kivy.uix.scrollview import ScrollView
from kivymd.uix.chip import MDChip
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from random import sample, randint
from kivy.metrics import dp


# define o tamanho da tela da janela q vai abrir caso for em desktop
try:
	if kivy_platform in ('win', 'linux', 'macosx'):
		Window.size = (375, 667)
except Exception:
	pass



#codigo do kivy 


kv = r'''
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
			font_name: "Roboto"
			on_press: root.manager.current = 'profile'
		MDRoundFlatButton:
			text: 'Sign up'
			size_hint: None, None
			pos_hint: {'center_x': 0.5, 'top': 0.40}
			font_size: '25sp'
			on_press: 
				root.manager.current = 'sign'
				app.motivacion_text()
				app.tempo()
		



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
			font_name: "Roboto"
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
			on_release: app.login()
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
			font_name: "Roboto"
		MDTextField:
			id: user_name
			hint_text: 'Username'
			width: 300
			height: 50
			mode: "round"
			pos_hint: {'top': 0.64, 'center_x': 0.5}
			size_hint: None, None
		MDTextField:
			id: user_pass
			hint_text: 'Password'
			width: 300
			height: 50
			mode: "round"
			size_hint: None, None
			pos_hint: {'top': 0.57, 'center_x': 0.5}
		MDTextField:
			id: user_pass_2
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
			on_press: app.signup()
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
	FloatLayout:
		MDIconButton:
			id: btn_0
			icon: "book-clock"
			size: '80dp', '80dp'
			theme_text_color: "Custom"
			pos_hint: {'center_x': 0.2,'center_y': 0.45}
			text_color: 1, 1, 1, 1
			on_press: root.manager.current = 'Plan'
			canvas.before:
				Color:
					rgba: 0, 0, 0, 1
				Ellipse:
					size: self.size
					pos: self.pos
		MDLabel:
			id: text_1
			text: 'Planning'
			halign: 'center'
			pos_hint: {'center_x': 0.2,'center_y': 0.39}

		MDIconButton:
			id: btn_1
			icon: "list-box-outline"
			size: '80dp', '80dp'
			pos_hint: {'center_x': 0.5,'center_y': 0.45}
			theme_text_color: "Custom"
			text_color: 1, 1, 1, 1
			on_press:
				root.manager.current = 'task'
				app.random_task()
			canvas.before:
				Color:
					rgba: 0, 0, 0, 1
				Ellipse:
					size: self.size
					pos: self.pos

		MDLabel:
			id: text_2
			text: 'Tasks'
			halign: 'center'
			pos_hint: {'center_x': 0.5,'center_y': 0.39}

		MDIconButton:
			id: btn_2
			icon: "cards"
			size: '80dp', '80dp'
			pos_hint: {'center_x': 0.8,'center_y': 0.45}
			theme_text_color: "Custom"
			text_color: 1, 1, 1, 1
			on_press: root.manager.current = 'cards'
			canvas.before:
				Color:
					rgba: 0, 0, 0, 1
				Ellipse:
					size: self.size
					pos: self.pos
		MDLabel:
			id: text_3
			text: 'Flash Card'
			halign: 'center'
			pos_hint: {'center_x': 0.8,'center_y': 0.39}

		MDIconButton:
			id: btn_3
			icon: "trending-up"
			size: '80dp', '80dp'
			pos_hint: {'center_x': 0.2,'center_y': 0.3}
			theme_text_color: "Custom"
			text_color: 1, 1, 1, 1
			on_press:
				app.progress()
				root.manager.current = 'progress'
			canvas.before:
				Color:
					rgba: 0, 0, 0, 1
				Ellipse:
					size: self.size
					pos: self.pos
		MDLabel:
			id: text_4
			text: 'Progress'
			halign: 'center'
			pos_hint: {'center_x': 0.2,'center_y': 0.24}

		MDIconButton:
			id: btn_4
			icon: "bullseye-arrow"
			size: '80dp', '80dp'
			pos_hint: {'center_x': 0.5,'center_y': 0.3}
			theme_text_color: "Custom"
			text_color: 1, 1, 1, 1
			on_press:
				app.challenge()
				root.manager.current = 'challenge'
			canvas.before:
				Color:
					rgba: 0, 0, 0, 1
				Ellipse:
					size: self.size
					pos: self.pos
		MDLabel:
			id: text_5
			text: 'Challenges'
			halign: 'center'
			pos_hint: {'center_x': 0.5,'center_y': 0.24}

		MDIconButton:
			id: btn_5
			icon: "cog"
			size: '80dp', '80dp'
			pos_hint: {'center_x': 0.8,'center_y': 0.3}
			theme_text_color: "Custom"
			text_color: 1, 1, 1, 1
			on_press: root.manager.current = 'question-sc'
			canvas.before:
				Color:
					rgba: 0, 0, 0, 1
				Ellipse:
					size: self.size
					pos: self.pos

		MDLabel:
			id: text_6
			text: 'Settings'
			halign: 'center'
			pos_hint: {'center_x': 0.8,'center_y': 0.24}


		MDBoxLayout:
			id: menu_t
			size_hint: None, None
			size: "340dp", "100dp"
			pos_hint: {"center_y": 0.7, "center_x": 0.5}
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
		MDIconButton:
			id: arrow_task
			icon: "arrow-left"
			size_hint: None, None
			size: "56dp", "56dp"
			theme_text_color: "Custom"
			pos_hint: {'x': 0.02, 'top': 0.98}
			on_press: root.manager.current = 'function-menu'

		MDLabel:
			id: title_task
			text: "Lista de Tarefas"
			pos_hint: {'center_x': 0.8, 'top': 1.4}
			font_size: '22sp'

		ScrollView:
			pos_hint: {'center_x': 0.5, 'center_y': 0.45}
			size_hint: 0.92, 0.78
			MDList:
				theme_text_color: "Primary"
				id: list_2
				radius: [20, 20, 20, 20]
		
		
			

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
		MDIconButton:
			id: arrow_flash
			icon: "arrow-left"
			theme_text_color: "Custom"
			size: "56dp", "56dp"
			pos_hint: {'x': 0.02, 'top': 0.98}
			on_press: root.manager.current = 'function-menu'

		ScrollView:
			pos_hint: {'center_x': 0.5, 'center_y': 0.5}
			size_hint: 0.92, 0.82
			MDList:
				id: list_card

		MDIconButton:
			id: plus_flash
			icon: "plus"
			theme_text_color: "Custom"
			text_color: 1, 0, 0, 1
			size: "56dp", "56dp"
			pos_hint: {'right': 0.96, 'y': 0.04}
			on_press: root.manager.current = 'criar-cards'
			canvas.before:
				Color:
					rgba: 0, 0, 0, 1
				Ellipse:
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
		MDIconButton:
			id: arrow_progress
			theme_text_color: "Custom"
			icon: "arrow-left"
			size: "80dp", "80dp"
			pos_hint: {'center_x': 0.09, 'center_y': 0.91}
			on_press: root.manager.current = 'function-menu'
		MDLabel:
			id: text_progress
			theme_text_color: "Custom"
			text: 'Progresso'
			font_size: '24sp'
			text_size: None, None
			pos_hint: {'center_x': 0.86, 'center_y': 0.87}
		MDLabel:
			id: text_progress1
			theme_text_color: "Custom"
			text: 'Tarefas concluidas hoje'
			font_size: '18sp'
			pos_hint: {'center_x': 0.77, 'center_y': 0.75}
			text_size: None, None
		MDLabel:
			id: text_progress2
			theme_text_color: "Custom"
			text: 'Tempo de estudo'
			font_size: '18sp'
			text_size: None, None
			pos_hint: {'center_x': 0.82, 'center_y': 0.58}
		MDLabel:
			id: text_progress3
			theme_text_color: "Custom"
			text: 'Desafio diario'
			font_size: '18sp'
			text_size: None, None
			pos_hint: {'center_x': 0.86, 'center_y': 0.43}

		

			

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
		MDIconButton:
			id: challenge_arrow
			theme_text_color: "Custom"
			icon: "arrow-left"
			size: "56dp", "56dp"
			pos_hint: {'x': 0.02, 'top': 0.98}
			on_press: root.manager.current = 'function-menu'

		MDLabel:
			id: text_chl
			text: 'Desafios'
			pos_hint: {'center_x': 0.89, 'top': 1.4}
			font_size: '22sp'

		ScrollView:
			pos_hint: {'center_x': 0.5, 'center_y': 0.45}
			size_hint: 0.92, 0.82
			MDList:
				radius: [20, 20, 20, 20]
				theme_text_color: "Primary"
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
		MDIconButton:
			id: arrow_settings
			theme_text_color: "Custom"
			icon: "arrow-left"
			size: "56dp", "56dp"
			pos_hint: {'x': 0.02, 'top': 0.98}
			on_press: root.manager.current = 'function-menu'

		ScrollView:
			pos_hint: {'center_x': 0.5, 'center_y': 0.5}
			size_hint: 0.92, 0.9
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

sign = JsonStore('sign.json')


class MyApp(MDApp):
	def build(self):
		# inicializa store de flashcards e carrega em memória
		self.flash_store = JsonStore('flashcards.json')
		self.flashcards = self.load_flashcards()
		return Builder.load_string(kv)

	def on_start(self):
		try:
			if sign.exists('current_user'):
				cur = sign.get('current_user')
				user = cur.get('username') if isinstance(cur, dict) else None
				if user and sign.exists(f'user_{user}'):
					try:
						self.root.current = 'function-menu'
					except Exception:
						pass
		except Exception:
			pass
		try:
			self.populate_flashcards_ui()
		except Exception:
			pass
		try:
			self.motivacion_text()
		except Exception:
			pass
	
	

	def username(self):
		text = self.root.get_screen('profile').ids.user_text.text
		passw = self.root.get_screen('profile').ids.pass_text.text
		print(f"username: {text}")
		print(f"password: {passw}")
	

	def signup(self):
		user = self.root.get_screen('sign').ids.user_name.text.strip()
		pass1 = self.root.get_screen('sign').ids.user_pass.text
		pass2 = self.root.get_screen('sign').ids.user_pass_2.text
		if not user or pass1 != pass2:
			print('signup failed: empty user or passwords do not match')
			return
		# salva credenciais por usuário
		sign.put(f'user_{user}', username=user, password=pass1)
		# cria sessão
		sign.put('current_user', username=user)
		try:
			self.root.current = 'function-menu'
		except Exception:
			pass

	def login(self):
		user = self.root.get_screen('profile').ids.user_text.text.strip()
		pw = self.root.get_screen('profile').ids.pass_text.text
		key = f'user_{user}'
		if user and sign.exists(key):
			data = sign.get(key)
			if data.get('password') == pw:
				sign.put('current_user', username=user)
				try:
					self.root.current = 'function-menu'
				except Exception:
					pass
				return True
		print('login failed')
		return False

	def logout(self):
		try:
			if sign.exists('current_user'):
				sign.delete('current_user')
		except Exception:
			pass
		try:
			self.root.current = 'home'
		except Exception:
			pass

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
		tempo = int(hour3) - int(hour4)
		if (tempo * 60) <= 60:
			minutos = int(hour2[2:4]) - int(hour[2:4])
		else:
			minutos = tempo * 60

		sign.put('time', qtempo=tempo, min=minutos)

	def add_matery(self):
		texto = self.root.get_screen('Plan').ids.text_matery.text.strip()
		if texto:
			self.root.get_screen('Plan').ids.lista.add_widget(
				OneLineListItem(text=texto)
			)
			self.root.get_screen('Plan').ids.text_matery.text = ""



	#colocar na inicialização
	def random_task(self):
		conclusao_tarefas = 0 
		nums = 10, 20, 30, 40
		r = sample(nums, 1)[0]
		sign.put('tarefas_t', tarefa=f"Estude {r} minutos".replace("[", ""), tempo=r)
		dados = sign.get('tarefas_t')
		if sign.exists('time'):
			dados_t = sign.get('time')
		else:
			dados_t = {'min': 0, 'qtempo': 0}
		item = TwoLineRightIconListItem(
			text=f"Tarefa 1", 
			secondary_text=dados['tarefa'],
		)
		if dados_t['min'] >= dados['tempo']:
			icon = IconRightWidget(icon="check-bold", text_color="#1EFF00", theme_text_color="Custom")
			conclusao_tarefas += 1
		else: 
			icon = IconRightWidget(icon="check-bold", text_color="#000000", theme_text_color="Custom")
		item.add_widget(icon)
		self.root.get_screen('task').ids.list_2.clear_widgets()
		self.root.get_screen('task').ids.list_2.add_widget(item)
		nums2 = [1, 2, 3, 5]
		sorteio_num = sample(nums2, 1)[0]
		sign.put('tarefas_f', tarefa=f"Faça {sorteio_num} flash cards".replace("[", ""), quant=int(sorteio_num))
		dados2 = sign.get('tarefas_f')
		item2 = TwoLineRightIconListItem(text="Tarefa 2", secondary_text=dados2['tarefa'].replace("]", ""), theme_text_color='Custom')
		try:
			current_count = len(self.flashcards)
		except Exception:
			current_count = 0
		self.current_task2_required = int(dados2['quant']) if 'quant' in dados2 else int(sorteio_num)
		if current_count >= self.current_task2_required:
			icon2 = IconRightWidget(icon="check-bold", theme_text_color="Custom", text_color=(0, 1, 0, 1))
			conclusao_tarefas += 1
		else:
			icon2 = IconRightWidget(icon="check-bold", theme_text_color="Custom", text_color=(0, 0, 0, 1))
		item2.add_widget(icon2)
		self._task2_item = item2
		self.root.get_screen('task').ids.list_2.add_widget(item2)
		#terceira tarefa
		nums3 = [1, 2, 3]
		sorteio_num2 = sample(nums3, 1)[0]
		sign.put('tarefas_n', tarefa=f"Faça {sorteio_num2} tarefas".replace("[", ""), quant=int(sorteio_num2))
		dados3 = sign.get('tarefas_n')
		item3 = TwoLineRightIconListItem(text="Tarefa 3", secondary_text=dados3['tarefa'].replace("]", ""))
		if conclusao_tarefas == 2 or conclusao_tarefas == sorteio_num2:
			icon3 = IconRightWidget(icon="check-bold", theme_text_color="Custom", text_color=(0, 1, 0, 1))
		else:
			icon3 = IconRightWidget(icon="check-bold", theme_text_color="Custom", text_color=(0, 0, 0, 1))
		self.root.get_screen('task').ids.list_2.add_widget(item3)
		item3.add_widget(icon3)
			
		

			
	def motivacion_text(self):
		lista = ["Um passo de cada vez.",
				 "Disciplina gera resultado.",
				 "Seu esforço vale a pena.\n"]
		random = randint(0, len(lista) - 1)
		texto = MDLabel(
			padding=[dp(15), dp(15)],
			text=f" \"{lista[random]}\"",
			pos_hint={'center_x': 0.5, 'center_y': 0.5},
			)
		self.root.get_screen('function-menu').ids.menu_t.add_widget(texto)


	def challenge(self):
		def toggle(alvo, *args):
			alvo.icon = "checkbox-marked-circle"
			alvo.text_color = (0, 1, 0, 1)
		desc = ["Acerte 5 questões", "Acerte 10 questões", "Resolva 3 questões"]
		txt_random = sample(desc, k=3)
		self.root.get_screen('challenge').ids.list3.clear_widgets()
		for i, txt_desc in enumerate(txt_random, 1):
			text_t = TwoLineRightIconListItem(text=f"Desafio {i}", secondary_text=txt_desc)
			icon = IconRightWidgetWithoutTouch(icon="checkbox-blank-circle-outline", theme_text_color="Custom")
			self.root.get_screen('challenge').ids.list3.add_widget(text_t)
			icon.bind(on_release=toggle)
			text_t.add_widget(icon)





	def flash_card(self):
		frente = self.root.get_screen('criar-cards').ids.frente_card.text
		verso = self.root.get_screen('criar-cards').ids.verso_card.text
		print(f"Frente = {frente}, verso = {verso}")
		if not hasattr(self, 'flashcards') or self.flashcards is None:
			self.flashcards = []
		if not (frente.strip() or verso.strip()):
			return
		self.flashcards.append({'frente': frente, 'verso': verso})
		self.save_flashcards()
		self.root.get_screen('criar-cards').ids.frente_card.text = ''
		self.root.get_screen('criar-cards').ids.verso_card.text = ''
		self.populate_flashcards_ui()
		try:
			self.root.manager.current = 'cards'
		except Exception:
			pass

	def _create_flashcard_widget(self, frente, verso, index):
		box = MDBoxLayout(
			orientation="vertical",
			size_hint_y=None,
			spacing=dp(8),
			padding=dp(12),
			size=(dp(340), dp(400)),
			md_bg_color=(1, 0, 0, 1),
			radius=[12, 12, 12, 12],
		)
		box.add_widget(MDLabel(text=frente, halign="center", font_style="H6", size_hint_y=None, height=dp(160)))
		box.add_widget(MDLabel(text=verso, halign="center", size_hint_y=None, height=dp(160)))
		controls = MDBoxLayout(size_hint_y=None, height=dp(60), padding=dp(8))
		rem = MDFillRoundFlatButton(text="Remover", pos_hint={"center_x": 0.5})
		rem.bind(on_release=lambda *_: self.remove_flashcard(index))
		controls.add_widget(rem)
		box.add_widget(controls)
		return box

	def populate_flashcards_ui(self):
		try:
			lista = self.root.get_screen('cards').ids.list_card
		except Exception:
			return
		lista.clear_widgets()
		for i, card in enumerate(self.flashcards):
			widget = self._create_flashcard_widget(card.get('frente', ''), card.get('verso', ''), i)
			lista.add_widget(widget)
			lista.add_widget(MDBoxLayout(size=(dp(200), dp(8)), size_hint_y=None))

	def remove_flashcard(self, index):
		if 0 <= index < len(self.flashcards):
			self.flashcards.pop(index)
			self.save_flashcards()
			self.populate_flashcards_ui()

	def load_flashcards(self):
		if JsonStore and hasattr(self, 'flash_store') and self.flash_store.exists('flashcards'):
			data = self.flash_store.get('flashcards')
			return data.get('items', [])
		try:
			with open('flashcards.json', 'r', encoding='utf-8') as f:
				data = json.load(f)
				return data.get('items', [])
		except Exception:
			return []

	def save_flashcards(self):
		try:
			self.flash_store.put('flashcards', items=self.flashcards)
		except Exception:
			try:
				with open('flashcards.json', 'w', encoding='utf-8') as f:
					json.dump({'items': self.flashcards}, f, ensure_ascii=False, indent=2)
			except Exception:
				pass
		try:
			self._update_task2_icon()
		except Exception:
			pass

	def _update_task2_icon(self):
		if not hasattr(self, '_task2_item') or self._task2_item is None:
			return
		required = getattr(self, 'current_task2_required', None)
		if required is None:
			return
		current = len(self.flashcards) if hasattr(self, 'flashcards') else 0
		for child in list(self._task2_item.children):
			if isinstance(child, IconRightWidget):
				try:
					self._task2_item.remove_widget(child)
				except Exception:
					pass
		if current >= required:
			icon = IconRightWidget(icon="check-bold", theme_text_color="Custom", text_color=(0, 1, 0, 1))
		else:
			icon = IconRightWidget(icon="checkbox-blank-outline", theme_text_color="Custom", text_color=(0, 0, 0, 1))
		self._task2_item.add_widget(icon)



	def progress(self):
		dados = sign.get('time')
		tarefas = ProgressBar(max=4, value=2,
							size_hint=(None, None),
							size=(dp(250), dp(50)),
							pos_hint={'center_x': 0.5, 'center_y': 0.7})
		self.root.get_screen('progress').add_widget(tarefas)
		tempo = ProgressBar(value=dados['min'], max=60,
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
		self.contador = 1
		while self.contador % 60 == 0:
			print(self.contador)


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
		#plano de fundo do modo dark
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
		self.root.get_screen('task').ids.arrow_task.text_color = (branco_icon)
		#listas de tarefas
		self.root.get_screen('cards').ids.plus_flash.md_bg_color = (branco_icon)
		self.root.get_screen('task').ids.list_2.md_bg_color = ("#131313FF")
		self.root.get_screen('challenge').ids.list3.md_bg_color = ("#0F0F0F")
		self.root.get_screen('question-sc').ids.list4.md_bg_color = ("#0F0F0F")
		#textos da tela de funções do modo dark
		self.root.get_screen('progress').ids.text_progress.color = (branco_icon)
		self.root.get_screen('progress').ids.text_progress1.color = (branco_icon)
		self.root.get_screen('progress').ids.text_progress2.color = (branco_icon)
		self.root.get_screen('progress').ids.text_progress3.color = (branco_icon)
		self.root.get_screen('task').ids.title_task.color = (branco_icon)
		self.root.get_screen('challenge').ids.text_chl.color = (branco_icon)
		self.root.get_screen('function-menu').ids.text_1.color = (branco_icon)
		self.root.get_screen('function-menu').ids.text_2.color = (branco_icon)
		self.root.get_screen('function-menu').ids.text_3.color = (branco_icon)
		self.root.get_screen('function-menu').ids.text_4.color = (branco_icon)
		self.root.get_screen('function-menu').ids.text_5.color = (branco_icon)
		self.root.get_screen('function-menu').ids.text_6.color = (branco_icon)
	
		

		

	

if __name__ == '__main__':
	MyApp().run()