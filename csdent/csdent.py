import kivy
kivy.require('1.4.2')
import os
import sys
from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder, Parser, ParserException
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.compat import PY2

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy.animation import Animation
from kivy.clock import Clock

from login.login import Login
from dashboard.dashboard import Dashboard

class Csdent(BoxLayout):
    '''Csdent of widgets. This is the root widget of the app. It contains
    a tabbed pain of widgets that can be displayed and a textbox where .kv
    language files for widgets being demoed can be edited.
    The entire interface for the Csdent is defined in kivycatalog.kv,
    although individual containers are defined in the container_kvs
    directory.
    To add a container to the catalog,
    first create the .kv file in container_kvs
    The name of the file (sans .kv) will be the name of the widget available
    inside the kivycatalog.kv
    Finally modify kivycatalog.kv to add an AccordionItem
    to hold the new widget.
    Follow the examples in kivycatalog.kv to ensure the item
    has an appropriate id and the class has been referenced.
    You do not need to edit any python code, just .kv language files!
    '''

    def __init__(self, **kwargs):
        self._previously_parsed_text = ''
        super(Csdent, self).__init__(**kwargs)
        self.show_kv(None, 'login')
        self.carousel = None

    def show_kv(self, instance, value):
        '''Called when an a item is selected, we need to show the .kv language
        file associated with the newly revealed container.'''
        self.screen_manager.current = value

        child = self.screen_manager.current_screen.children[0]
        print(child.kv_file)
        with open(child.kv_file, 'rb') as file:
            self.language_box.text = file.read().decode('utf8')
        Clock.unschedule(self.change_kv)
        self.change_kv()
        # reset undo/redo history
        self.language_box.reset_undo()

    def schedule_reload(self):
        if self.auto_reload:
            txt = self.language_box.text
            child = self.screen_manager.current_screen.children[0]
            if txt == child.previous_text:
                return
            child.previous_text = txt
            Clock.unschedule(self.change_kv)
            Clock.schedule_once(self.change_kv, 2)

    def change_kv(self, *largs):
        '''Called when the update button is clicked. Needs to update the
        interface for the currently active kv widget, if there is one based
        on the kv file the user entered. If there is an error in their kv
        syntax, show a nice popup.'''

        txt = self.language_box.text
        kv_container = self.screen_manager.current_screen.children[0]
        try:
            parser = Parser(content=txt)
            kv_container.clear_widgets()
            widget = Factory.get(parser.root.name)()
            Builder._apply_rule(widget, parser.root, parser.root)
            kv_container.add_widget(widget)
        except (SyntaxError, ParserException) as e:
            self.show_error(e)
        except Exception as e:
            self.show_error(e)

    def show_error(self, e):
        self.info_label.text = str(e)
        self.anim = Animation(top=190.0, opacity=1, d=2, t='in_back') +\
            Animation(top=190.0, d=3) +\
            Animation(top=0, opacity=0, d=2)
        self.anim.start(self.info_label)
