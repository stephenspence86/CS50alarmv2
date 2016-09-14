from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import time
from kivy.utils import escape_markup
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from datetime import datetime
from kivy.graphics import Color
from kivy.uix.popup import Popup
from kivy.core.text.markup import MarkupLabel
from kivy.core.text import LabelBase
from kivy.properties import *
from kivy.graphics import Line
from kivy.base import runTouchApp
from kivy.garden import roulette, roulettescroll, tickline
import forecastio

api_key = "9ca514decbdf7d7055ba9de5228cfa77"
lat = 52.3782080
lng = -1.7578900

forecast = forecastio.load_forecast(api_key, lat, lng)
AppisRunning = True

# while AppisRunning == True:
#     AlarmSound = False
#     alarmtime = StringProperty()
#     now = datetime.now()
#
#     if alarmtime == now:
#         AlarmSound = True

class CurrentForecast(Screen):
    def current_forecast(self):
        hourly= forecast.currently()
        cf = hourly.summary
        return str(cf)

class DisplayTime(Widget):
    pass

class MenuScreen(Screen):
    def get_time(self, *args):
        return time.strftime("%H:%M:%S")


class AlarmScreen(Screen):
    pass
    # def open_alarm(self):
    #     content = BoxLayout(orientation='vertical')
    #     label = Label(
    #             text=('[color=#59c6ff] hello World [/color]'), markup=True)
    #     btn3 = Button(text='close me!', background_normal='',
    #                       background_color=(0.349, 0.776, 1.0, 1.0))
    #     content.add_widget(label)
    #     content.add_widget(btn3)
    #
    #     popup = Popup(content=content,
    #                   title='Alarm?',
    #                       size_hint=(None, None), size=(400, 400),
    #                       auto_dismiss=False,
    #                       background='',
    #                      )
    #     popup.open()
    #     btn3.bind(on_release=popup.dismiss)

class ForecastScreen(Screen):
    pass

class QuitScreen(Screen):
    pass

class SetAlarm(Screen):
    pass

class ViewAlarm(Screen):
    pass

class RadioScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class TestApp(App):
    time = StringProperty()

    def showTime(self, *args):
        self.time = time.strftime('%H:%M:%S')

    def build(self):
        presentation = Builder.load_file("testscreen.kv")
        Clock.schedule_interval(self.showTime, 1)
        return presentation

if __name__ == '__main__':
    TestApp().run()
