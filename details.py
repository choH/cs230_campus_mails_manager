from kivy.app import App
from kivy.uix.screenmanager import Screen
import json




def get_entry(num):
    with open('registered.data') as json_file:
        json_data = json.load(json_file)
        for entry in json_data:
            if entry['tracking_num'] == num:
                return entry

num = '1234'
# app = App.get_running_app()
# app.root.ids.current_layout.last_entry()



class DetailsScreen(Screen):
    #
    # def __init__(self):
    #     super(DetailsScreen, self).__init__(**kwargs)
    #
    # # def set_label_text(self):
    #
    #
    def on_enter(self):
        self.ids.output_label.text = 'something'
        # entry = get_entry(num)




    def process_submit(self):
        json_list = ['tracking_num', 'recipient', 'box_num',
                     'registered_staff', 'registered_time', 'bin_num',
                     'note', 'redeemed_staff', 'redeemed time', 'carrier']
        for i in range(0, 10):
            if self.ids.spin.values == self.ids.spin.values[i]:
                entry = get_entry('1234')
                entry[json_list[i]] = self.ids.edit.text
        self.last_entry(num)

    def process_redeem(self):
        entry = get_entry(num)
        entry['is_redeemed'] = 'false'


class detailsApp(App):
    pass


if __name__ == '__main__':
    detailsApp().run()
