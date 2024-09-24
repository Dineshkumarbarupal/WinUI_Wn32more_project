using System.Windows;
using System.Windows.Controls;
using System.Windows.Navigation;

namespace WINUI_WIN32MORE
{
    public partial class MainPage : Page
    {
        public MainPage()
        {
            InitializeComponent();
        }

        private void GetStartedButton_Click(object sender, RoutedEventArgs e)
        {
            NavigationService.Navigate(new NextPage());
        }
    }
}
