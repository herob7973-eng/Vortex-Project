from kivy.app import App
from kivy.uix.button import Button
class VortexApp(App):
    def build(self):
        return Button(text="Vortex Prime Active")
if __name__ == "__main__":
    VortexApp().run()
