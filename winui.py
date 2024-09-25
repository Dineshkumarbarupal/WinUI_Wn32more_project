from win32more.xaml import XamlApplication
from win32more.Microsoft.UI.Xaml import Window, Controls
from win32more.Microsoft.UI.Windowing import AppWindowTitleBar
from win32more.Microsoft.UI.Xaml.Markup import XamlReader

class MainPage(Controls.Page):
    def __init__(self, frame):
        super().__init__()
        # Load the XAML content for MainPage
        with open("page.xaml", "r") as file:
            self.Content = XamlReader.Load(file.read())

        # Find the 'Get Started' button by its name
        get_started_button = self.FindName("GetStartedButton")
        if get_started_button:
            # Bind the Click event to the GetStartedButton_Click method
            get_started_button.Click += self.GetStartedButton_Click

        self.frame = frame  # Store the frame to use for navigation

    def GetStartedButton_Click(self, sender, e):
        # Navigate to the second page when the button is clicked
        second_page = SecondPage()
        self.frame.Navigate(second_page)

class SecondPage(Controls.Page):
    def __init__(self):
        super().__init__()
        # Load the XAML content for SecondPage
        with open("second_page.xaml", "r") as file:
            self.Content = XamlReader.Load(file.read())

class App(XamlApplication):
    def OnLaunched(self, args):
        win = Window()

        # Set the title to an empty string (no window title)
        win.Title = ""  

        # Extend the content into the title bar and hide the title bar
        win.ExtendsContentIntoTitleBar = True
        win.SetTitleBar(None)  # Removes the system's default title bar

        # Create a Frame for navigation
        frame = Controls.Frame()

        # Set the main page to the frame
        main_page = MainPage(frame)
        frame.Content = main_page
        win.Content = frame

        win.Activate()

XamlApplication.Start(App)
