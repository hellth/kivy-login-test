#!/bin/python
# -*- coding: utf-8 -*-

__version__ = "0.1"

import kivy
import os
import sys

kivy.require('1.9.0')
from kivy.app import App
from kivy.config import Config
from kivy.factory import Factory
from kivy.lang import Builder, Parser, ParserException
from kivy.properties import ObjectProperty
#from kivy.compat import PY2
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.codeinput import CodeInput
#from kivy.animation import Animation
#from kivy.clock import Clock

from kivy.uix.screenmanager import ScreenManager, Screen
from csdent.csdent import Csdent
from login.login import Login
#from dashboard.dashboard import Dashboard


''' List of classes that need to be instantiated in the factory from .kv files. '''
CSDENT_ROOT = os.path.dirname(__file__)
CONTAINER_KVS = os.path.join(CSDENT_ROOT, 'containers')
CONTAINER_CLASSES = [c[:-3] for c in os.listdir(CONTAINER_KVS)
    if c.endswith('.kv')]

print(os.listdir(CONTAINER_KVS))

class Container(BoxLayout):
    '''A container is essentially a class that loads its root from a known
    .kv file.
    The name of the .kv file is taken from the Container's class.
    We can't just use kv rules because the class may be edited
    in the interface and reloaded by the user.
    See :meth: change_kv where this happens.
    '''

    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        self.previous_text = open(self.kv_file).read()
        parser = Parser(content=self.previous_text)
        widget = Factory.get(parser.root.name)()
        Builder._apply_rule(widget, parser.root, parser.root)
        self.add_widget(widget)

    @property
    def kv_file(self):
        '''Get the name of the kv file, a lowercase version of the class
        name.
        '''
        return os.path.join(CONTAINER_KVS, self.__class__.__name__ + '.kv')

for class_name in CONTAINER_CLASSES:
    globals()[class_name] = type(class_name, (Container,), {})

class CsdentApp(App):
    Window.clearcolor = get_color_from_hex('#1d202f')

    Config.set('graphics', 'width', '1024')
    Config.set('graphics', 'height', '768')

    language_box = ObjectProperty()
    screen_manager = ObjectProperty()

    def build(self):
        try:
            return Csdent()

        except:
            pass

if __name__ == '__main__':


    CsdentApp().run()