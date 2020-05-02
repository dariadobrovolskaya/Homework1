from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, Line

Config.set('graphics', 'fullscreen', 'auto')
from random import random

from kivy.lang import Builder
Builder.load_string('''<Interface>:
    orientation: 'vertical'
    DrawingWidget:
    Slider:
        min: 0
        max: 1
        value: 0.5
        size_hint_y: None
        height: 50
    Slider:
        min: 0
        max: 1
        value: 0.5
        size_hint_y: None
        height: 50
    Slider:
        min: 0
        max: 1
        value: 0.5
        size_hint_y: None
        height: 50
    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: 50
        Label:
            text: 'output colour:'
        Widget:
''')
class DrawingWidget(Widget):
    def __init__(self):
        super(DrawingWidget, self).__init__()

        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size,
                                  pos=self.pos)
        self.bind(pos=self.update_rectangle,
                  size=self.update_rectangle)

    def update_rectangle(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_touch_down(self, touch):
        super(DrawingWidget, self).on_touch_down(touch)

        if not self.collide_point(*touch.pos):
            return

        with self.canvas:
            Color(random(), random(), random())
            self.line = Line(points=[touch.pos[0], touch.pos[1]], width=2)

    def on_touch_move(self, touch):
        if not self.collide_point(*touch.pos):
            return

        self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]


class Interface(BoxLayout):
    pass

class DrawingApp(App):

    def build(self):
        root_widget = Interface()
        return root_widget

DrawingApp().run()
