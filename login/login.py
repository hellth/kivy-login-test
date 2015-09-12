#!/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

class Login(Screen):

    def __init__(self, **kwargs):
        pass
        #super(LoginScreen, self).__init__(**kwargs)
        #print 'loginscreen init'
        #app = App()
        #return app.load_kv('containers/login.kv')
        #self.cols = 2
        #self.add_widget(Label(text='User:'))
        #self.username = TextInput(multiline=False)
        #self.add_widget(self.username)
        #self.add_widget(Label(text='Pwd:'))
        #self.password = TextInput(password=True, multiline=False)
        #self.add_widget(self.password)
        #self.button = Button(text="Login", size_hint=(2, 1))
        ##self.button.bind(on_press=LoginScreen.do_login(self.username, self.password))
        #self.add_widget(self.button)

    #
    #def do_login(self, loginText, passwordText):
    #    app = App.get_running_app()
    #
    #    app.username = loginText
    #    app.password = passwordText
    #
    #    self.manager.transition = SlideTransition(direction="left")
    #    self.manager.current = 'dashboard'
    #
    #    app.config.read(app.get_application_config())
    #    app.config.write()
    #
    #def resetForm(self):
    #    self.ids['login'].text = ""
    #    self.ids['password'].text = ""

