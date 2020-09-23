from kivy.config import Config
Config.set("graphics","width",360)
Config.set("graphics","height",720)

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.list import TwoLineListItem

notes= list()

class MainApp(MDApp):
    def notes_list(self):
        """Add list of all notes on home 
        """
        screenMGR.get_screen("home").ids.notes_list.add_widget(
            TwoLineListItem(
                text="qwerty",
                secondary_text="ajsbfpiabffbasf"
            )
        )

    def save_note(self,title,note):
        """This menod get data from text box in title and note arguments

        Args:
            title (String): data from title box
            note (String): data from note box
        """
        print(title,note)
        notes.append({"Title":title,"Note":note})
        print(notes)
        self.change_screen("home")

    def change_screen(self,name):
        """ Switch Screen by name

        Args:
            name (String): Screen name
        """
        screenMGR.current = name

    def build(self):
        global screenMGR
        screenMGR = ScreenManager()
        screenMGR.add_widget(Builder.load_file("UI//home.kv"))
        screenMGR.add_widget(Builder.load_file("UI//newnote.kv"))
        # screenMGR.current = "new_note"
        self.notes_list()
        return  screenMGR

if __name__ == "__main__":
    MainApp().run()

