from kivy.config import Config
Config.set("graphics","width",360)
Config.set("graphics","height",720)

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.list import TwoLineListItem
from kivy.clock import Clock

import json,os

with open("data.json") as data:
    notes = json.load(data)


class MainApp(MDApp):
    def notes_list(self):
        """Add list of all notes on home 
        """

        for num,data in notes.items():
            screenMGR.get_screen("home").ids.notes_list.add_widget(
                TwoLineListItem(
                    text= data["Title"],
                    secondary_text= data["Note"]
                )
            )

    def update_list(self,dt):
        screenMGR.get_screen("home").ids.notes_list.clear_widgets()
        self.notes_list()


    def save_note(self,title,note):
        """This menod get data from text box in title and note arguments

        Args:
            title (String): data from title box
            note (String): data from note box
        """
        notes[str(len(notes)+1)] = {"Title": title, "Note": note}
        os.remove("data.json")
        with open("data.json","w") as data:
            data.write(json.dumps(notes,indent=4))

        self.change_screen("home")

    def change_screen(self,name):
        """ Switch Screen by name

        Args:
            name (String): Screen name
        """
        screenMGR.current = name

    def build(self):
        Clock.schedule_interval(self.update_list, 1)
        global screenMGR
        screenMGR = ScreenManager()
        screenMGR.add_widget(Builder.load_file("UI//home.kv"))
        screenMGR.add_widget(Builder.load_file("UI//newnote.kv"))
        # screenMGR.current = "new_note"
        self.notes_list()
        return  screenMGR

if __name__ == "__main__":
    MainApp().run()

