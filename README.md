# Homework1
Задание:
Напишите небольшой графический редактор с использованием kivy (https://github.com/kivy/kivy).
Сделайте один инструмент - круглую кисть с изменением размера и цвета.


У меня были проблемы с разрешением всплывающего окна, когда я работала в спайдере/джупитере, но потом перешла в атом и все наладилось. проблему с разрешением можно решить, выводя на полный экран:

from kivy.config import Config

Config.set('graphics', 'fullscreen', 'auto')


Также добавила кнопку "clear", которая очищает холст.
