import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 
from tkinter import filedialog
import os
import SortingFiles

def OriginalRefresh(app,appData):
    app.__init__(appData)

class WindowData:
    ''' Adresses '''
    UserProf = os.environ['USERPROFILE']
    GenAdr = UserProf+r'\Desktop'
    if(os.path.exists(GenAdr)):
        pass
    else:
        GenAdr = UserProf+'\OneDrive\Desktop'
    DirAdrList = {'Audio':GenAdr+r'\AutomaticSortedFiles\Audio',
    'Video': GenAdr+r'\AutomaticSortedFiles\Video',
    'Documents':GenAdr+r'\AutomaticSortedFiles\Documents',
    'Images':GenAdr+r'\AutomaticSortedFiles\Images',
    'Code':GenAdr+r'\AutomaticSortedFiles\Code',
    'Folders':GenAdr+r'\AutomaticSortedFiles\Folders'}

    DirList = [f'{d}:' for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(f'{d}:')]
    DirList.remove('C:')

    RadioValue = None
    def DirAdrRefresh(self):
        if(self.RadioValue != '0'):
            for i in self.DirAdrList.keys():
                self.DirAdrList[i] = self.RadioValue + ':\AutomaticSortedFiles\\'+ i
            # print(v)
    def Finish(self):
        SortingFiles.RunProject(self.GenAdr,self.DirAdrList)

def EnteryWindow(RecieveAdr):
    root = tk.Tk()
    root.title("Welcome to Automatic File Sorter ")
    ''' Buttan '''
    global flag
    flag = 0
    def OK():
        global flag
        flag = 1
        root.destroy()
    def Sett():
        global flag
        flag = 2
        root.destroy()

    LabelGen = tk.Label(root,text='Current Genaral Folder : '+RecieveAdr.GenAdr,relief='sunken',bg='wheat',width=30)
    LabelGen.pack(padx=10,pady=15,fill='both')

    ButtonRun = tk.Button(root,bg='wheat',width = '15',padx=5,pady=5,text='RUN',height='1',command= OK)
    ButtonRun.pack(side='left',padx=15,pady=15)
    ButtonSet = tk.Button(root,bg='wheat',width = '15',padx=5,pady=5,text='Settings',height='1',command=Sett)
    ButtonSet.pack(side='right',padx=15,pady=15)
    root.mainloop()
    return flag

class Window:
    def __init__(self,appData):
        self.root = tk.Tk()
        self.root.title("Hello")
        self.root.geometry('720x550')
        self.root.config(bg='sky blue')

        ''' Functions '''

        def Refresh():
            appData.RadioValue = RadioVar.get()
            appData.DirAdrRefresh()
            self.root.destroy()
            OriginalRefresh(A,appData)

        def ScGenAdr():
            appData.GenAdr = filedialog.askdirectory()
            for key in appData.DirAdrList.keys():
                appData.DirAdrList[key] = appData.GenAdr + '\AutomaticSortedFiles\\'+key
            Refresh()
        def ScAudAdr():
            appData.DirAdrList['Audio'] = filedialog.askdirectory()
            Refresh()
        def ScVidAdr():
            appData.DirAdrList['Video'] = filedialog.askdirectory()
            Refresh()
        def ScImgAdr():
            appData.DirAdrList['Images'] = filedialog.askdirectory()
            Refresh()
        def ScDocAdr():
            appData.DirAdrList['Documents'] = filedialog.askdirectory()
            Refresh()
        def ScCodeAdr():
            appData.DirAdrList['Code'] = filedialog.askdirectory()
            Refresh()
        def ScFoldAdr():
            appData.DirAdrList['Folders'] = filedialog.askdirectory()
            Refresh()

        def SaveExit():
            self.root.destroy()
            appData.Finish()


        ''' Varibales '''
        GenVar = tk.StringVar()
        GenVar.set(appData.GenAdr)
        AudVar = tk.StringVar()
        AudVar.set(appData.DirAdrList['Audio'])
        VidVar = tk.StringVar()
        VidVar.set(appData.DirAdrList['Video'])
        ImgVar = tk.StringVar()
        ImgVar.set(appData.DirAdrList['Images'])
        DocVar = tk.StringVar()
        DocVar.set(appData.DirAdrList['Documents'])
        CodeVar = tk.StringVar()
        CodeVar.set(appData.DirAdrList['Code'])
        FoldVar = tk.StringVar()
        FoldVar.set(appData.DirAdrList['Folders'])

        RadioVar = tk.StringVar()
        RadioVar.set(0)

        ''' Frames '''
        GenFrame = tk.Frame(self.root,bg='sky blue',height='10',width='400',borderwidth=5,relief='sunken')
        GenFrame.pack(fill='both',pady=1)
        # BlackFrame = tk.Frame(self.root,bg='sky blue',height='10',width='400')
        # BlackFrame.pack(fill='both')
        DriveFrame = tk.Frame(self.root,bg='sky blue',height='20',width='400',borderwidth=3,relief='sunken')
        DriveFrame.pack(fill='both')
        MainFrame = tk.Frame(self.root,bg='sky blue',height='150',width='400',borderwidth=3,relief='sunken')
        MainFrame.pack(fill='both')

        ''' Labels '''
        LabelAdrGen = tk.Label(GenFrame,text = 'Choose General Folder  :  ')
        LabelAdrGen.grid(padx=10,pady=10,row=0,column=0)

        LabelBlank = tk.Label(MainFrame,bg='sky blue',height=3)
        LabelBlank.grid(row=0,column=0)
        LabelDestText = tk.Label(MainFrame,bg='sky blue',height=3,text='Choose Folder For Sorted Files :')
        LabelDestText.grid(row=0,column=0)

        LabelText = tk.Label(DriveFrame,text='Choose Destination Drive : ',bg='sky blue',font=('aerial',14,'bold'))
        LabelText.pack(anchor='nw',pady=13)
        LabelAdrAud = tk.Label(MainFrame,text = 'Choose Folder For Audio  :  ')
        LabelAdrAud.grid(padx=10,pady=10,row=1,column=0)
        LabelAdrVid = tk.Label(MainFrame,text = 'Choose Folder For Video :  ')
        LabelAdrVid.grid(padx=10,pady=10,row=2,column=0)
        LabelAdrImg = tk.Label(MainFrame,text = 'Choose Folder For Images :  ')
        LabelAdrImg.grid(padx=10,pady=10,row=3,column=0)
        LabelAdrDoc = tk.Label(MainFrame,text = 'Choose Folder For Documents :  ')
        LabelAdrDoc.grid(padx=10,pady=10,row=4,column=0)
        LabelAdrCode = tk.Label(MainFrame,text = 'Choose Folder For Code :  ')
        LabelAdrCode.grid(padx=10,pady=10,row=5,column=0)
        LabelAdrCode = tk.Label(MainFrame,text = 'Choose Folder For Folders:  ')
        LabelAdrCode.grid(padx=10,pady=10,row=6,column=0)


        ''' Entry '''

        # GenVar = tk.StringVar()
        # GenVar.set("Hello")
        EntryGen = tk.Entry(GenFrame,textvariable=GenVar,width=50)
        EntryGen.grid(row=0,column=1,padx=10,pady=10)
        EntryAud = tk.Entry(MainFrame,textvariable=AudVar,width=50)
        EntryAud.grid(row=1,column=1,padx=10,pady=10)
        EntryVid = tk.Entry(MainFrame,textvariable=VidVar,width=50)
        EntryVid.grid(row=2,column=1,padx=10,pady=10)
        EntryImg = tk.Entry(MainFrame,textvariable=ImgVar,width=50)
        EntryImg.grid(row=3,column=1,padx=10,pady=10)        
        EntryDoc = tk.Entry(MainFrame,textvariable=DocVar,width=50)
        EntryDoc.grid(row=4,column=1,padx=10,pady=10)
        EntryCode = tk.Entry(MainFrame,textvariable=CodeVar,width=50)
        EntryCode.grid(row=5,column=1,padx=10,pady=10)
        EntryCode = tk.Entry(MainFrame,textvariable=FoldVar,width=50)
        EntryCode.grid(row=6,column=1,padx=10,pady=10)

        ''' Buttons '''
        BtGenBrow = tk.Button(GenFrame,text = 'Browse',command = ScGenAdr)
        BtGenBrow.grid(row=0,column=2)
        BtAudBrow = tk.Button(MainFrame,text = 'Browse',command = ScAudAdr)
        BtAudBrow.grid(row=1,column=2)
        BtVidBrow = tk.Button(MainFrame,text = 'Browse',command = ScVidAdr)
        BtVidBrow.grid(row=2,column=2)
        BtImgBrow = tk.Button(MainFrame,text = 'Browse',command = ScImgAdr)
        BtImgBrow.grid(row=3,column=2)
        BtDocBrow = tk.Button(MainFrame,text = 'Browse',command = ScDocAdr)
        BtDocBrow.grid(row=4,column=2)
        BtCodeBrow = tk.Button(MainFrame,text = 'Browse',command = ScCodeAdr)
        BtCodeBrow.grid(row=5,column=2)
        BtCodeBrow = tk.Button(MainFrame,text = 'Browse',command = ScFoldAdr)
        BtCodeBrow.grid(row=6,column=2)

        BtSaveNExit = tk.Button(MainFrame,text='Save & Exit',width=15,command=SaveExit,bg='wheat',relief='sunken')
        BtSaveNExit.grid(row=7,column=5,padx=15,pady=30)

        for i in range(len(appData.DirList)):
            BtnRadio = 'BtnRadio' + str(i)
            BtnRadio = tk.Radiobutton(DriveFrame,text='Drive = '+appData.DirList[i][0],relief='sunken',value = appData.DirList[i][0],variable=RadioVar)
            BtnRadio.pack(side='left',padx=10,pady=10)


        btnApply = tk.Button(DriveFrame,text='Apply',command=Refresh)
        btnApply.pack(side='right')
    def PrintRadio(self):
        for i in appData.DirAdrList.values():
            print(i)

if __name__ == '__main__':
    appData = WindowData()
    ans = EnteryWindow(appData)
    if(ans == 2):
        A = Window(appData)
        A.root.mainloop()
    elif( ans==1):
        appData.Finish()
