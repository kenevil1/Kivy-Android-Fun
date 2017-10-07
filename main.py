from kivy.app import App
from kivy.core.window import Window
#kivy.require("1.10.0")

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

'''
class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label())
        self.provider = TextInput(multiline=False)
        self.add_widget(self.provider)

        self.add_widget(Label(text="Purchased: "))
        self.purchased = TextInput(multiline=False)
        self.add_widget(self.purchased)
'''

class Widgets(Widget):
    def on_touch_move(self, touch):
        print('The touch is at position', touch.pos)
        if 'angle' in touch.profile:
            print('The touch angle is', touch.a)

    pass

class SimpleKivy(App):
    def build(self):
        return Widgets()

if __name__ == "__main__":
    SimpleKivy().run()
