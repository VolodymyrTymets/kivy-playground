import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

# class LoginScreen(GridLayout):

#     def __init__(self, **kwargs):
#         super(LoginScreen, self).__init__(**kwargs)
#         self.cols = 2
#         self.add_widget(Label(text='User Name'))
#         self.username = TextInput(multiline=False)
#         self.add_widget(self.username)
#         self.add_widget(Label(text='password'))
#         self.password = TextInput(password=True, multiline=False)
#         self.add_widget(self.password)

class MyRootWidget(Widget):
    def lbl(self):
        print("-----> Label:", self.name.text)



class MyApp(App):
    def build(self):
        return MyRootWidget()


if __name__ == '__main__':
    MyApp().run()