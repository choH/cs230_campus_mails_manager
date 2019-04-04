from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.config import Config
# Config.set('graphics', 'width', '323')
# Config.set('graphics', 'height', '700')


class Input(Screen):
    def submission_func(self):
        for text_input in self.ids:
            pass


class InputApp(App):
    def build(self):
        return Input()


if __name__ == '__main__':
    InputApp().run()


