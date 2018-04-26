"""
Create a series of widgets for a list of names
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.core.window import Window


class NameListApp(App):
    """Main program. Create a series of labels for a list of names."""
    _names = ["Adam", "Bill", "Charlie", "David"]

    def build(self):
        Window.size = (600, 400)
        self.title = "Name List"
        self.root = Builder.load_file('name_list.kv')
        self.create_widget()
        return self.root

    def create_widget(self):
        # Create label for each person
        for name in self._names:
            temp_label = Label(text=name, id=name)
            self.root.ids.entity_container.add_widget(temp_label)



NameListApp().run()
