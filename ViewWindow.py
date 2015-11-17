"""
  _____               _     _____ _            ____
 |_   _| __ _   _ ___| |_  |_   _| |__   ___  / ___|  ___  _   _ _ __ ___ ___
   | || '__| | | / __| __|   | | | '_ \ / _ \ \___ \ / _ \| | | | '__/ __/ _ \
   | || |  | |_| \__ \ |_    | | | | | |  __/  ___) | (_) | |_| | | | (_|  __/
   |_||_|   \__,_|___/\__|   |_| |_| |_|\___| |____/ \___/ \__,_|_|  \___\___|

Created by Daniel Slobben, Michael van der Veen & Margot Verleg

Creation Date:
    17-11-2015_12:51
Class:
    ViewWindow
Contributors:
    Michael van der Veen
Description:
    Main window for the user interface
ChangeLog:
    17-11-2015_12:51: Creation of the Class
"""
import wx

class ViewWindow(wx.Frame):
    def __init__(self):
        #creating App object for using wx
        self.app = wx.App()

        #setting main window
        wx.Frame.__init__(self,
                          parent=None,
                          title='Trust the Source',
                          size=(1600,900))

    def run(self):
        #run the app
        self.Show()
        self.app.MainLoop()

app = ViewWindow()
app.run()