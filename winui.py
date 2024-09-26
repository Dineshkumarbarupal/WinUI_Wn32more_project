from win32more.xaml import XamlApplication
from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Xaml.Controls import Page, Button, Frame
from win32more.Microsoft.UI.Xaml.Markup import XamlReader

class MainPage(Page):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame 
        try:
           
            with open("page.xaml", "r") as file:
                self.Content = XamlReader.Load(file.read())
        except Exception as e:
            print("cann't load file...")
 
        get_started_button = self.FindName("GetStartedButton")
        if get_started_button:
            print("Button found!")
            get_started_button.Click += self.GetStartedButton_Click
        else:
            print("button not found")
    
    def GetStartedButton_Click(self, sender, e):
        
           
        second_page = SecondPage()
        self.frame.Navigate(second_page)
  
class SecondPage(Page):
    def __init__(self):
        super().__init__()
        
        with open("second_page.xaml", "r") as file:
            self.Content = XamlReader.Load(file.read())


class App(XamlApplication):
    def OnLaunched(self, args):
        win = Window()
        win.Title = ""        
        win.ExtendsContentIntoTitleBar = True
        win.SetTitleBar(None) 
        frame = Frame()

        main_page = MainPage(frame)
        frame.Content = main_page
        win.Content = frame

        win.Activate()

XamlApplication.Start(App)
