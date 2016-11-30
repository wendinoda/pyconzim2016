from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        myboxlayout = BoxLayout(orientation='horizontal')
        mylabel = Label(text = 'layout demo', size_hint_y=1, font_size = 40,
                   color=(209, 18, 66), italic=True)
        mytextinput = TextInput(size_hint=(0.3,0.1))
        mybutton = Button(text = 'click')
        myboxlayout.add_widget(mylabel )
        myboxlayout.add_widget(mytextinput)
        myboxlayout.add_widget(mybutton)

class LayoutDemoApp(App):
    def build(self):
        myboxlayout = BoxLayout(orientation='vertical')
        mylabel = Label(text = 'layout demo', size_hint_y=1, font_size = 40,
                    color=(209, 18, 66), italic=True)
        mytextinput = TextInput(size_hint=(1,0.4))
        mybutton = Button(text = 'click')
        myboxlayout.add_widget(mylabel )
        myboxlayout.add_widget(mytextinput)
        myboxlayout.add_widget(mybutton)
        #self.layoutdemo = layoutdemo = MyWidget()
        return myboxlayout

LayoutDemoApp().run()
