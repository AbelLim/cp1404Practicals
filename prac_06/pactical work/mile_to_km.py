"""
Convert miles to kilometer. Can type in value in text box or use up and down button to modify the speed (in miles).
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MileToKm(App):
    """Mile to km is a kivy app to convert distances"""
    def build(self):
        """Build kivy app"""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('mile_to_km.kv')
        return self.root

    def handle_increment(self, value, increment):
        """Increases input by value"""
        try:
            result = int(value) + increment
        except ValueError:
            result = increment
        self.root.ids.input_box.text = str(result)
        self.handle_conversion(result)

    def handle_conversion(self, value):
        try:
            result = int(value) * 1.60934
        except ValueError:
            result = "0.0"
        self.root.ids.output_box.text = str(result)


MileToKm().run()
