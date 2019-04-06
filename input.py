from kivy.app import App
import kivy
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.config import Config
#Config.set('graphics', 'width', '323')
#Config.set('graphics', 'height', '700')


class Input(Screen):
    def submission_func(self):
        list_of_inputs = [self.ids.tracking_number, self.ids.student_name,
                          self.ids.description, self.ids.bin_number,
                          self.ids.box_number, self.ids.staff_id,
                          self.ids.date_received]

        filename = "registered.data"
        try:
            open(filename, "w")
        except:
            print("File failed to open")


        for text_input in list_of_inputs:
            pass

    def carrier_func(self, carrier_id):
        carrier_dict = {1: self.ids.USPS, 2: self.ids.Fedex, 3: self.ids.UPS,
                        4: self.ids.DHL, 5: self.ids.Other}
        id = carrier_dict[carrier_id]
        id.background_color = (0, 1, 0, 1)



class InputApp(App):
    def build(self):
        return Input()


if __name__ == '__main__':
    InputApp().run()


