import json
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config
from datetime import datetime
# datetime.utcnow()
# Config.set('graphics', 'width', '323')
# Config.set('graphics', 'height', '700')


class Input(Screen):
    def submission_func(self):
        self.ids.status.value = 0
        selected_carrier = ''
        carrier_list = [self.ids.USPS, self.ids.Fedex, self.ids.UPS,
                        self.ids.DHL, self.ids.Other]
        for carrier in carrier_list:
            if carrier.state == 'down':
                selected_carrier = carrier.text

        if selected_carrier == '':
            self.popup()
            return
        information = {'tracking_num': self.ids.tracking_num.text, 'recipient':
                       self.ids.recipient.text, 'note': self.ids.note.text,
                       'bin_number': self.ids.bin_number.text, 'box_number':
                       self.ids.box_number.text, 'registered_staff':
                       self.ids.registered_staff.text, 'delivered_time':
                       self.ids.delivered_time.text, 'is_redeemed': 'false',
                       'redeemed_time': 'false', 'service': selected_carrier}

        for json_name, text in information.items():
            if text == '':
                self.popup()
                return

        filename = "registered.data"
        with open(filename, "r") as copy_file:
            try:
                data = json.load(copy_file)
            except ValueError:
                data = []

            data.append(information)
        with open(filename, "w") as json_file:
            json.dump(data, json_file)
            json_file.close()

        self.ids.tracking_num.text = ''
        self.ids.recipient.text = ''
        self.ids.note.text = ''
        self.ids.bin_number.text = ''
        self.ids.box_number.text = ''
        self.ids.registered_staff.text = ''
        self.ids.delivered_time.text = ''


        for carrier in carrier_list:
            carrier.state = 'normal'


    def popup(self):
        """
        This function implements popup widget functionality, whereby should an
        exception be thrown, a popup will be created to alert the user the
        error. The user then must acknowledge the popup by clicking the 'Ok'
        button. This physical instantiation of this includes a general
        BoxLayout for the entire popup, a Label widget to display the error
        message, and an 'Ok' button to accept the error.

        :param error_message: The exceptions error message, which will be
        displayed by the popup.
        :return: None
        """
        content = BoxLayout(orientation='vertical')
        error_label = Label(text="Please fill all required fields")
        dismiss_button = Button(text='Ok')
        content.add_widget(error_label)
        content.add_widget(dismiss_button)
        popup = Popup(title='Error', content=content, size_hint=(.3, .25),
                      auto_dismiss=False)
        dismiss_button.bind(on_press=popup.dismiss)
        popup.open()




class InputApp(App):
    def build(self):
        return Input()


if __name__ == '__main__':
    InputApp().run()


