import pandas as pd
import numpy as np
import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        return Label(text = "Hello my name is Eric")

if __name__ == "__main__":
    MyApp().run()

