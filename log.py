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



def get_next_entry():
    with open('registered.data') as json_file:
        json_data = json.load(json_file)
        for entry in json_data:
            yield entry

search_dict = {}
def get_matched_entry():
    # app = App.get_running_app()
    # search_dict = app.root.ids.current_log_screen.__class__.search_dict
    for entry in get_next_entry():
        holder_list = []
        for search_key in search_dict:
            if entry[search_key]:
                if search_dict[search_key] == entry[search_key] or search_dict[search_key] in entry[search_key]:
                    holder_list.append(entry['tracking_num'])
        if len(holder_list) == len(search_dict):
            yield entry

def search_all_entry():
    target_content = search_dict['everything']
    search_dict.pop('everything', None)
    for entry in get_next_entry():
        for k, v in entry.viewitems():
            if v != False:
                if v == target_content or target_content in v:
                    yield entry
                    break

def entry_to_str(entry):
    entry_str = ('Tracking #: ' + entry['tracking_num'] +
                '  |  ' + entry['recipient'].center(20) +
                '  |  ' + entry['registered_time'] +
                '  |  ' + entry['redeemed_status'].center(15))
    return entry_str


def entry_to_display(mode):
    entry_str = ''
    if mode == 1:
        for entry in get_next_entry():
            entry_str = entry_to_str(entry)
            yield entry_str
    elif mode == 2:
        for entry in get_matched_entry():
            entry_str = entry_to_str(entry)
            yield entry_str
    elif mode == 3:
        for entry in search_all_entry():
            entry_str = entry_to_str(entry)
            yield entry_str



filters_dict = {'filter_tracking_num': False,
                'filter_recipient': False,
                'filter_service': False,
                'filter_is_redeemed': False,
                'filter_registered_time': False,
                'filter_redeemed_time': False,
                'filter_registered_staff': False,
                'filter_redeemed_staff': False}

def filter_format_LUT(filter_id_str):
    filter_format_LUT = {'filter_tracking_num': 'Enter the last four digits as "XXXX"',
                          'filter_recipient': 'Enter as "Firstname Lastname"',
                          'filter_carrier': 'Specify: "UPS" "DHL" "FEDEX" "USPOSTAL" "CAMPUS"',
                          'filter_redeemed_status': 'Specify: "Redeemed" "Unredeemed"',
                          'filter_registered_time': 'Enter as "YYYY-MM-DD"',
                          'filter_redeemed_time': 'Enter as "YYYY-MM-DD"',
                          'filter_registered_staff': 'Enter the stuff ID',
                          'filter_redeemed_staff': 'Enter the stuff ID'}
    return filter_format_LUT[filter_id_str]


class InputScreen(Screen):
    pass

class DetailsScreen(Screen):
    pass

class LogScreen(Screen):

    # search_dict = {}

    def __int__(self, **kwargs):
        super(LogScreen, self).__init__(**kwargs)
        # self.triggered_filter_str = ''



    def filter_trigger(self, filter_id_str):
        self.filter_id_LUT = {'filter_tracking_num': self.ids.filter_tracking_num,
                              'filter_recipient': self.ids.filter_recipient,
                              'filter_carrier': self.ids.filter_carrier,
                              'filter_redeemed_status': self.ids.filter_redeemed_status,
                              'filter_registered_time': self.ids.filter_registered_time,
                              'filter_redeemed_time': self.ids.filter_redeemed_time,
                              'filter_registered_staff': self.ids.filter_registered_staff,
                              'filter_redeemed_staff': self.ids.filter_redeemed_staff}

        self.triggered_filter_id = self.filter_id_LUT[filter_id_str]


        if self.triggered_filter_id.state == 'down':
            self.ids.search_input.hint_text = filter_format_LUT(filter_id_str)
            if self.ids.search_submit.search_scope:
                if self.ids.search_submit.search_scope not in search_dict:
                    self.last_triggered_filter_id = self.filter_id_LUT['filter_' + self.ids.search_submit.search_scope]
                    self.last_triggered_filter_id.state = 'normal'

            self.ids.search_submit.search_scope = filter_id_str[7:]
            print('Current search scope is: {}'.format(self.ids.search_submit.search_scope))

        elif self.triggered_filter_id.state == 'normal':
            self.ids.search_input.hint_text = 'Enter search content or select a filter for advanced search'
            if self.ids.search_submit.search_scope == filter_id_str[7:]:

                search_dict.pop(filter_id_str[7:], None)

                self.ids.search_submit.search_scope = False



    def submit(self):
        user_search_input = self.ids.search_input.text

        if self.ids.search_submit.search_scope != False:
            search_dict[self.ids.search_submit.search_scope] = user_search_input
            self.on_enter(2)
        else:
            search_dict['everything'] = user_search_input
            self.on_enter(3)
        print('Current search_dict is: {}'.format(search_dict))

    def reset(self):
        search_dict = {}
        self.ids.search_input.text = ''
        self.ids.search_submit.search_scope = False
        button_tuple = (self.ids.filter_tracking_num,
                        self.ids.filter_recipient,
                        self.ids.filter_carrier,
                        self.ids.filter_redeemed_status,
                        self.ids.filter_registered_time,
                        self.ids.filter_redeemed_time,
                        self.ids.filter_registered_staff,
                        self.ids.filter_redeemed_staff)
        for button in button_tuple:
            if button.state != 'normal':
                button.state = 'normal'
        self.on_enter(1)

    def to_details(self, instance):
        print('Proceed to the details page of #{}'.format(instance.text[12:16]))



    @mainthread
    def on_enter(self, mode=1):
        self.ids.entry_layout.clear_widgets()
        for entry_str in entry_to_display(mode):
            a_button = Button(text = entry_str)
            # a_spinner = Spinner(text=entry_str,
            #                     values = ('Edit #'+entry_str[12:16], 'Delete #'+entry_str[12:16]),
            #                     sync_height = True)
            # self.ids.entry_layout.add_widget(a_spinner)
            a_button.bind(on_release = self.to_details)
            self.ids.entry_layout.add_widget(a_button)




class logApp(App):
    pass

if __name__ == '__main__':
    logApp().run()