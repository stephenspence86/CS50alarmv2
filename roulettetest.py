from kivy.base import runTouchApp
from kivy.garden import roulette, roulettescroll, tickline
from kivy.garden import DatetimePicker
from kivy.app import App


class TestApp(App):

    def build(self):
        #menuclock = MenuScreen()
        #Clock.schedule_interval(menuclock.get_time, 1)
        pass

if __name__ == '__main__':
    runTouchApp(DatetimePicker())
