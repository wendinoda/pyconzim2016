from kivy.app import App
from kivy.uix.button import Button

class Hello_pyconzimApp(App):
    def build(self):
        #btn = Button(text='Hello Pycon_Zim')
        return Button(text='Hello Pycon_Zim', font_size=40)

Hello_pyconzimApp().run()
