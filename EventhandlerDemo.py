from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyWidget(BoxLayout):

    #mytextinput = TextInput()
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.orientation='vertical'

        #nested widgets
        self.mylabel = Label(text = 'layout demo', size_hint_y=1, font_size = 40,
                        color=(209, 18, 66), italic=True)
        self.mytextinput = TextInput(size_hint=(1,0.4) ,text = '')
        mybutton = Button(text = 'click')
        mybutton.bind(on_release=self.on_press_change)

        self.add_widget(self.mylabel )
        self.add_widget(self.mytextinput)
        self.add_widget(mybutton)
        #self.register_event_type('on_press_change')

    def on_press_change(self, mybutton):
        if self.mytextinput.text != '':
            self.mylabel.text = self.mytextinput.text
            self.mytextinput.text = ''

class EventhandlerDemoApp(App):

    def build(self):

        #self.layoutdemo = layoutdemo = MyWidget()
        return MyWidget()

EventhandlerDemoApp().run()
