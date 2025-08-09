class MyApp:
    def __init__(self):
        self.root = None  # Initialize root or UI framework here

    def time_select2(self, instance, time):
        self.root.get_screen('Plan').ids.time_selected2.text = str(time)

    def text_hours(self):
        hour = self.root.get_screen('Plan').ids.time_selected.text.replace(":", "")
        hour2 = self.root.get_screen('Plan').ids.time_selected2.text.replace(":", "")
        hour3 = hour.replace("0", "")
        hour4 = hour2.replace("0", "")
        print(f"Horario de inicio: {hour3} horario final {hour4} e tempo estimativo: horas {int(hour4) - int(hour3)}")

if __name__ == '__main__':
    MyApp().run()