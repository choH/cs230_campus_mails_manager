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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
import json, requests
from datetime import datetime








class InputScreen(Screen):
    def submission_func(self):
        self.ids.status.value = 0
        selected_carrier = ''
        carrier_list = [self.ids.USPS, self.ids.Fedex, self.ids.UPS,
                        self.ids.DHL, self.ids.CAMPUS]
        for carrier in carrier_list:
            if carrier.state == 'down':
                selected_carrier = carrier.text

        if selected_carrier == '':
            self.popup()
            return
        information = {'tracking_num': self.ids.tracking_num.text,
                        'recipient': self.ids.recipient.text,
                        'box_num': self.ids.box_number.text,
                        'registered_staff': self.ids.registered_staff.text,
                        'registered_time': self.ids.delivered_time.text,
                        'bin_num': self.ids.bin_number.text,
                        'note': self.ids.note.text,
                        'redeemed_status': 'Unredeemed',
                        'redeemed_staff': 'Unknown',
                        'redeemed_time': 'Unknown',
                        'carrier': selected_carrier}

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



class LogScreen(Screen):


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
                print('first lay')
                if self.ids.search_submit.search_scope not in search_dict:
                    print('first lay')
                    self.last_triggered_filter_id = self.filter_id_LUT['filter_' + self.ids.search_submit.search_scope]
                    self.last_triggered_filter_id.state = 'normal'
                    self.ids.search_submit.search_scope

            print('outer lay')
            self.ids.search_submit.search_scope = filter_id_str[7:]
            print('Current search scope is: {}'.format(self.ids.search_submit.search_scope))

        elif self.triggered_filter_id.state == 'normal':
            self.ids.search_input.hint_text = 'Enter search content or select a filter for advanced search'
            # if self.ids.search_submit.search_scope == filter_id_str[7:]:

            search_dict.pop(filter_id_str[7:], None)

            self.ids.search_submit.search_scope = False



    def submit(self):
        user_search_input = self.ids.search_input.text

        # if self.ids.search_submit.search_scope != False:
        if self.ids.search_submit.search_scope != False:
            search_dict[self.ids.search_submit.search_scope] = user_search_input
            self.on_enter(2)
        elif len(search_dict) >= 1:
            self.on_enter(2)
        else:
            search_dict['everything'] = user_search_input
            self.on_enter(3)
        print('Current search_dict is: {}'.format(search_dict))

    def reset(self):
        search_dict.clear()
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

    def entry_to_detail_str(self, entry):
        output_str = ''
        for k, v in entry.items():
            if k == 'tracking_num':
                continue
            output_str += (k + ': \n'
                            + '                                                '
                            + str(v) + '\n\n')
        return output_str


    def to_details(self, instance):
        print('Proceed to the details page of #{}'.format(instance.text[12:16]))
        entry_holder = False
        for entry in get_next_entry():
            if entry['tracking_num'] == instance.text[12:16]:
                entry_holder = entry
                break
        output_str = ('------------------------------------------------------------------------------------\n'
                        + 'Tracking #'+instance.text[12:16]
                        + '\n\n\n\n'
                        + self.entry_to_detail_str(entry)
                        + '------------------------------------------------------------------------------------\n')
        self.ids.details_trigger_button.hinding_text = output_str.center(25)
        self.ids.details_trigger_button.text = 'View #'+instance.text[12:16]+' in Details'






    @mainthread
    def on_enter(self, mode=1):
        self.ids.entry_layout.clear_widgets()
        for entry_str in entry_to_display(mode):
            a_button = Button(text = entry_str)
            a_button.bind(on_release = self.to_details)
            self.ids.entry_layout.add_widget(a_button)




class DetailsScreen(Screen):
    pass


class managerApp(App):
    pass

if __name__ == '__main__':
    managerApp().run()