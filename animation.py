#import kivy
#from kivy.app import App
#from kivy.uix.label import Label

#class MyApp(App):

 #   def build(self):
  #      return Label(text = "Hello my name is Eric")

#if __name__ == "__main__":
 #   MyApp().run()

import requests
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock
from timeit import time

Window.size=(300,300)
Builder.load_file('animation.kv')


class MyLayout(Widget):
    pass


class LoopApp(App):
    def build(self):
        return MyLayout()

if __name__=='__main__':
    LoopApp().run()
