from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import time
from kivy.utils import escape_markup
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
#from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
#from datetime import datetime
#from kivy.graphics import Color
from kivy.uix.popup import Popup
#from kivy.core.text.markup import MarkupLabel
#from kivy.core.text import LabelBase
from kivy.properties import StringProperty, ObjectProperty
from kivy.graphics import Line
import forecastio

api_key = "9ca514decbdf7d7055ba9de5228cfa77"
lat = 52.3782080
lng = -1.7578900

forecast = forecastio.load_forecast(api_key, lat, lng)

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

class Alarm(Popup):
    def close_alarm(self):
        self.dismiss()
# Declare both screens

class Forecast(Widget):
    pass

class MenuScreen(Screen):
    pass

class AlarmScreen(Screen):
    def open_alarm(self):
        a = Alarm()
        a.open()

class ForecastScreen(Screen):
    def open_forecast(self):
        forecast

class ScreenManagement(ScreenManager):
    pass
# Create the screen manager

presentation = Builder.load_file("testscreen.kv")

class TestApp(App):

    def build(self):
        return presentation

if __name__ == '__main__':
    TestApp().run()
