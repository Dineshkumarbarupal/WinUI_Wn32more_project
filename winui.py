from win32more.xaml import XamlApplication
from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Windowing import AppWindowTitleBar
from win32more.Microsoft.UI.Xaml.Media import MicaBackdrop
from win32more.Microsoft.UI.Xaml.Markup import XamlReader

class App(XamlApplication):
    def OnLaunched(self, args):
        win = Window()
        win.Title = ""  # Set this to an empty string to remove the title
        win.ExtendsContentIntoTitleBar = True
        win.SetTitleBar(None)  # Hides the default title bar completely
        win.SystemBackdrop = MicaBackdrop()
        
        # Verify the file path:
        print(f"Loading XAML file: ./page.xaml")  # Adjust the path if necessary

        try:
            with open("page.xaml", "r") as file:
                win.Content = XamlReader.Load(file.read())
        except Exception as e:
            print(f"Error loading XAML file: {e}")

        win.Activate()

XamlApplication.Start(App)
