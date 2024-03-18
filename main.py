import wx

from windows.MainWindow import MainWindow


def main():
    app = wx.App()

    window = MainWindow()
    window.Show()

    app.MainLoop()


if __name__ == "__main__":
    main()
