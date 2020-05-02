from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color,Line
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class MyPaintWidget(Widget):
    def on_touch_down(self,touch):
        with self.canvas:
            Color(255,0,0)
            d = 35
            touch.ud['line']= Line(points=(touch.x,touch.y))


    def on_touch_move(self,touch):
        touch.ud['line'].points +=[touch.x,touch.y]

class MyPaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        clearbtn = Button(text='Очистить',
                          background_color=(0, 0, 1, 1))
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self,obj):
        self.painter.canvas.clear()

Config.set('graphics', 'fullscreen', 'auto')

if __name__== '__main__':
    MyPaintApp().run()
