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

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(11)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label='Welcome to the homepage.')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(self, label='Ok', size=(70, 30))
        hbox5.Add(btn1)
        btn2 = wx.Button(self, label='Close', size=(70, 30))
        hbox5.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

        self.SetSizer(vbox)

        self.Centre()
        self.Show()
