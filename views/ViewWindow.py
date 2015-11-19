"""
  _____ _ _____ _ ____
 |_ _| __ _ _ ___| |_ |_ _| |__ ___ / ___| ___ _ _ _ __ ___ ___
   | || '__| | | / __| __| | | | '_ \ / _ \ \___ \ / _ \| | | | '__/ __/ _ \
   | || | | |_| \__ \ |_ | | | | | | __/ ___) | (_) | |_| | | | (_| __/
   |_||_| \__,_|___/\__| |_| |_| |_|\___| |____/ \___/ \__,_|_| \___\___|

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
import wx.grid as gridlib

from views import ViewGeneral


class ViewWindow(wx.Frame):

    def __init__(self):
        # creating App object for using wx
        self.app = wx.App()
        # setting main window
        wx.Frame.__init__(self,
                          parent=None,
                          id=1,
                          title='Trust the Source')

        # setting the window on maximized view
        # self.Maximize(True)
        # creating and setting status bar
        ViewWindow.create_status_bar(self)
        # creating and setting menuBar
        ViewWindow.create_menu_bar(self)
        # creating the inside of the frame layout
        ViewWindow.create_inside_frame(self)
        # adding general panel test
        #ViewWindow.create_general(self, 3)
        #ViewWindow.create_general(self, 4)

    def create_general(self, id):
        self.panelGeneral = ViewGeneral.ViewGeneral(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panelGeneral, id, wx.EXPAND)
        self.SetSizer(self.sizer)

    def create_status_bar(self):
        sb = wx.Frame.CreateStatusBar(self, name="statusBar")
        self.SetStatusBar(sb)

    # Creating menu bar
    def create_menu_bar(self):
        menu_bar = wx.MenuBar()
        # File menu
        file_menu = wx.Menu()
        file_new = file_menu.Append(wx.ID_NEW, 'New Search Window', 'new search window')
        file_exit = file_menu.Append(wx.ID_EXIT, 'Exit\tCtrl+Q', 'Exit application')
        menu_bar.Append(file_menu, '&File')
        # Help
        help_menu = wx.Menu()
        help_about = help_menu.Append(wx.ID_ABOUT, 'About', 'Show information about Trust The Source')
        help_help = help_menu.Append(wx.ID_HELP, 'Help', 'Show Help menu')
        menu_bar.Append(help_menu, '&Help')
        # setting final bar as menu bar
        self.SetMenuBar(menu_bar)

        # Action listeners
        # FileMenu listeners
        self.Bind(wx.EVT_MENU, self.menu_file_exit, file_exit)
        self.Bind(wx.EVT_MENU, self.menu_file_new_window, file_new)
        # HelpMenu listeners
        self.Bind(wx.EVT_MENU, self.menu_help_about, help_about)
        self.Bind(wx.EVT_MENU, self.menu_help_help, help_help)

    def menu_file_exit(self, e):
        print("exiting")
        self.Close()

    def menu_file_new_window(self, e):
        self.SetStatusText("New window clicked")

    def menu_help_about(self, e):
        self.SetStatusText("Show about menu")

    def menu_help_help(self, e):
        self.SetStatusText("Show Help menu")

    def create_inside_frame(self):

        splitter = wx.SplitterWindow(self)
        leftP = LeftPanel(splitter)
        rightP = ViewGeneral.ViewGeneral(splitter)

        # split the window
        splitter.SplitVertically(leftP, rightP)
        splitter.SetMinimumPaneSize(20)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(splitter, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def run(self):
        # run the app
        self.Centre()
        self.Show()
        self.app.MainLoop()

########################################################################
class LeftPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent, id=4)
        txt = wx.TextCtrl(self)



app = ViewWindow()
app.run()
