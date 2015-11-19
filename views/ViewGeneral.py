"""
  _____               _     _____ _            ____
 |_   _| __ _   _ ___| |_  |_   _| |__   ___  / ___|  ___  _   _ _ __ ___ ___
   | || '__| | | / __| __|   | | | '_ \ / _ \ \___ \ / _ \| | | | '__/ __/ _ \
   | || |  | |_| \__ \ |_    | | | | | |  __/  ___) | (_) | |_| | | | (_|  __/
   |_||_|   \__,_|___/\__|   |_| |_| |_|\___| |____/ \___/ \__,_|_|  \___\___|

Created by Daniel Slobben, Michael van der Veen & Margot Verleg

Creation Date:

Class:

Contributors:

Description:

ChangeLog:

"""
import wx

class ViewGeneral(wx.Panel):



    def initUI(self):
        # Setting the font for the text in this panel
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        # Making the vertical box for the BoxSizer
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Making the title
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        welcomeText = wx.StaticText(self, label='Welcome to the overview!')
        welcomeText.SetFont(font)
        hbox1.Add(welcomeText, flag=wx.ALL, border=12)
        vbox.Add(hbox1, flag=wx.LEFT|wx.RIGHT|wx.TOP|wx.ALIGN_CENTER, border=10)

        vbox.Add((-1, 10))

        # Making a static text
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        infoText = wx.StaticText(self, label='Information')
        infoText.SetFont(font)
        hbox2.Add(infoText, flag=wx.LEFT, border=10)
        vbox.Add(hbox2, flag=wx.ALL | wx.TOP, border=12)

        vbox.Add((-1, 10))

        # Making the buttons
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        buttonForm = wx.Button(self, label='Select a twitter message', size=(200, 50))
        buttonForm.Bind(wx.EVT_BUTTON, self.listenerForm)
        hbox3.Add(buttonForm, proportion=10)
        buttonHistory = wx.Button(self, label='View your search history', size=(200, 50))
        buttonHistory.Bind(wx.EVT_BUTTON, self.listenerHistory)
        hbox3.Add(buttonHistory, proportion=9, flag=wx.LEFT, border=12)

        vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT,
            border=10)

        vbox.Add((-1, 25))

        # Setting the sizer for this panel
        self.SetSizer(vbox)
    # This function gets called when the button gets clicked
    def listenerForm(self, event):
        print "form"

    # This function gets called when the button gets clicked
    def listenerHistory(self, event):
        print "history"

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        self.initUI()
        self.Centre()
        self.Show()
