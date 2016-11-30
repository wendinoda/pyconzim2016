from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, BooleanProperty
from kivy.lang import Builder

class InitScreen(ScreenManager):
    pass

class BoxLayoutScreen(Screen):
    def __init__(self, **kwargs):
        super(BoxLayoutScreen, self).__init__(**kwargs)

    def on_press_change(self):
        if self.ids.mytxtinput.text != '':
            tommorow = self.ids.mytxtinput.text
            self.ids.mytxtinput.text
            self.ids.lbl = 'PyconZim ends on:' + tommorow

class SecondScreen(Screen):
    male = StringProperty()
    female = StringProperty()

    is_active = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        #self.male = 'Male'
        #self.female = 'female'

    def validate(self):
        if self.ids.passwd == 'mypassword' and self.ids.fname == 'wendinoda':
            InitScreen().current = 'FirstScreen'
        else:
            self.ids.validatelbl.text = 'Login failure'


pres = Builder.load_file("Kvdemo.kv")
class KvDemoApp(App):
    def build(self):
        return pres

if __name__=='__main__':
    KvDemoApp().run()
