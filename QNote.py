from kivy.config import Config
Config.set("graphics","width",360)
Config.set("graphics","height",720)

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager

class MainApp(MDApp):
    def change_screen(self,name):
        screenMGR.current = name
    def build(self):
        global screenMGR
        screenMGR = ScreenManager()
        screenMGR.add_widget(Builder.load_file("UI//home.kv"))
        screenMGR.add_widget(Builder.load_file("UI//newnote.kv"))
        # screenMGR.current = "new_note"
        return  screenMGR

if __name__ == "__main__":
    MainApp().run()

