import wx, os, shutil

def removeDir(identifier):
    target = os.path.join(os.path.expanduser('~'),identifier)
    files = 0
    folders = 0
    for the_file in os.listdir(target):
        if the_file[0] != "_":
            file_path = os.path.join(target, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    files += 1
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    folders += 1
            except Exception as e:
                print(e)
    return files, folders

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        pnl = wx.Panel(self)
        self.SetTitle('Nuke PII')
        self.a0 = wx.StaticBox(pnl, label='Locations', pos=(5, 5), size=(240, 400))
        self.a1 = wx.CheckBox(pnl, label='Documents', pos=(15, 30))
        self.a2 = wx.CheckBox(pnl, label='Pictures', pos=(15, 55))
        self.a3 = wx.CheckBox(pnl, label='Desktop', pos=(15, 80))
        self.a4 = wx.CheckBox(pnl, label='Downloads', pos=(105, 55))
        self.a5 = wx.CheckBox(pnl, label='Temp', pos=(105, 30))
        self.result = wx.StaticText(pnl, label="", pos=(50,105), size=(120, -1))
        self.btn = wx.Button(pnl, label='Delete PII', pos=(50, 170), size=(60, -1))
        self.btn2 = wx.Button(pnl, label='Close', pos=(140, 170), size=(60, -1))
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.a1.SetValue(True)
        self.a2.SetValue(True)
        self.a3.SetValue(True)
        self.a4.SetValue(True)
        self.a5.SetValue(True)
        self.Show(True)
        self.btn.Bind(wx.EVT_BUTTON, self.onbtn)
        self.btn2.Bind(wx.EVT_BUTTON, self.onbtn2)

    def onbtn(self, evt):
        data = dict(
            Documents=self.a1.GetValue(),
            Pictures=self.a2.GetValue(),
            Desktop=self.a3.GetValue(),
            Downloads=self.a4.GetValue(),
            Temp=self.a5.GetValue()
        )
        self.removeAll(data)
    
    def removeAll(self, data):
        files, folders = 0, 0
        if data["Documents"]:
            f, fo = removeDir("documents")
            files += f
            folders += fo
        if data["Pictures"]:
            f, fo = removeDir("pictures")
            files += f
            folders += fo
        if data["Desktop"]:
            f, fo = removeDir("desktop")
            files += f
            folders += fo
        if data["Downloads"]:
            f, fo = removeDir("downloads")
            files += f
            folders += fo
        if data["Temp"]:
            f, fo = removeDir("AppData/local/temp")
            files += f
            folders += fo
        self.result.SetLabel(str(files) +' files removed\n\n'+str(folders)+' folders removed')
        


    def onbtn2(self, evt):
        self.Close(True)


if __name__ == "__main__":
    app = wx.App()
    MyFrame(None)
    app.MainLoop()