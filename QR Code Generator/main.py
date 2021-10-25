import tkinter as tk
import tkinter.font as tkFont 
from tkinter import filedialog
from pyqrcode import QRCode
import pyqrcode 
import os
from PIL import Image

class App:
    def __init__(self, root):
        root.title("QR Code Generator")
        width=350
        height=200
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        ft = tkFont.Font(family='Acme',size=28)
        self.root = root

        self.AppName=tk.Label(root)
        self.AppName["font"] = ft
        self.AppName["fg"] = "#333333"
        self.AppName["justify"] = "center"
        self.AppName["text"] = "QR Code Generator"
        self.AppName.place(x=0,y=15,width=350,height=45)

        ft = tkFont.Font(family='Acme',size=10)
        self.LinkInput=tk.Entry(root)
        self.LinkInput["bg"] = "#efefef"
        self.LinkInput["font"] = ft
        self.LinkInput["fg"] = "#000000"
        self.LinkInput["justify"] = "center"
        self.LinkInput["text"] = "Button"
        self.LinkInput.place(x=25,y=75,width=300,height=35)

        self.GenerateButton=tk.Button(root)
        self.GenerateButton["bg"] = "#efefef"
        self.GenerateButton["font"] = ft
        self.GenerateButton["fg"] = "#000000"
        self.GenerateButton["justify"] = "center"
        self.GenerateButton["text"] = "Generate"
        self.GenerateButton.place(x=65,y=130,width=100,height=35)
        self.GenerateButton["command"] = self.GenerateButton_command

        self.SaveQR=tk.Button(root)
        self.SaveQR["bg"] = "#efefef"
        self.SaveQR["font"] = ft
        self.SaveQR["fg"] = "#000000"
        self.SaveQR["justify"] = "center"
        self.SaveQR["text"] = "Save"
        self.SaveQR.place(x=185,y=130,width=100,height=35)
        self.SaveQR["command"] = self.SaveQR_command

    def GenerateButton_command(self):
        path = os.path.join("QR Code Generator", "result", "QRCode.png")
        url = pyqrcode.create(self.LinkInput.get()).png(path, scale = 7)
        Image.open(path).show()
        
    
    def SaveQR_command(self):
        path = filedialog.askdirectory()
        path = os.path.join(path , "QRCode.png")
        url = pyqrcode.create(self.LinkInput.get()).png(path, scale = 7)
        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
