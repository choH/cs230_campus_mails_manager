from kivy.config import Config
Config.set('graphics', 'width', '563')
Config.set('graphics', 'height', '1218')


from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.clock import mainthread
from kivy.uix.screenmanager import Screen

import json, requests


NUMBER_OF_ENTRIES = 100


class LogScreen(Screen):

    @mainthread
    def on_enter(self):
        for i in range(NUMBER_OF_ENTRIES):
            a_spinner = Spinner(text="Entry #" + str(i),
                                values = ('Edit', 'Delete'),
                                sync_height = True)
            self.ids.entry_layout.add_widget(a_spinner)


class logApp(App):
    pass

if __name__ == '__main__':
    logApp().run()