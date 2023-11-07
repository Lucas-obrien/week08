import random
import json
from kivy.app import App
from kivy.app import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty


class ProductViewer(App):
    message = StringProperty()

    def build(self):

        self.title = "Box Layout Demo"
        self.root = Builder.load_file('product.kv')
        return self.root

    def handle_press(self):
        self.message = self.root.ids.user_input.text


ProductViewer().run()
