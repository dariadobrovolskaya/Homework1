from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.colorpicker import ColorPicker
from kivy.app import App
from kivy.properties import ListProperty, NumericProperty
from kivy.graphics import Rectangle, Color, Line
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (600, 600)
col = [0,0,1,1]



class ColPckr(ColorPicker):
    pass

class ColPopup(Popup):
    pass

class MyPaintApp(Widget):
    selected_color = ListProperty(col)
    selected_thickness = 1
    objects = []

    def select_ColPckr(self,*args):
        ColPopup().open()

    def on_touch_down(self, touch):
        super(MyPaintApp, self).on_touch_down(touch)
        if not self.collide_point(*touch.pos) or touch.pos[1] < 150:
            return
        with self.canvas:
            Color(*self.selected_color)
            self.objects.append(Line(points=[touch.pos[0], touch.pos[1]], width=self.selected_thickness))

    def select_thickness(self,value):
        self.selected_thickness = value

    def on_touch_move(self, touch):
        if not self.collide_point(*touch.pos) or touch.pos[1] < 150:
            return

        self.objects[-1].points += [touch.pos[0], touch.pos[1]]

    def my_clear(self):
        for i in self.objects:
            self.canvas.remove(i)

class MyApp(App):
    def build(self):
        return MyPaintApp()

if __name__=='__main__':
    MyApp().run()
