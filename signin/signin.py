from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (1920, 1080)

class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
            super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        username = user.text
        password = pwd.text

        if username == '' or password == '':
            info.text = '[color=#FF0000]Username and/or password required[/color]'
        else:
            if username == 'admin' and password == 'admin':
                info.text = '[color=#00FF00]Logged In Successfully!!![/color]'
            else:
                info.text = '[color=#FF0000]Invalid Username and/or Password[/color]'

class SigninApp(App):
    def build(self):
        return SigninWindow()

if __name__=='__main__':
    SigninApp().run()
