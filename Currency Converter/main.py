import tkinter as tk
import requests
import csv


class App:
    def __init__(self, root):
        root.title("Currency Converter")
        width=350
        height=250
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.API_KEY = ''

        self.codes = []
        with open('codes.csv', 'r') as file:
            reader = csv.reader(file)
            self.codes.extend(row[2] for row in reader)
        self.AppLabel = tk.Label(root, text="Currency Converter", font=("Acme", 18))
        self.AppLabel.place(x=80, y=20, width=195, height=30)
        self.fromCur = tk.StringVar()
        self.fromCur.set(self.codes[0])
        self.toCur = tk.StringVar()
        self.toCur.set(self.codes[0])
        self.fromCurLabel = tk.Label(root, text="From:", font=("Acme", 13))
        self.fromCurLabel.place(x=20, y=70, width=40, height=30)
        self.fromCurMenu = tk.OptionMenu(root, self.fromCur, *self.codes)
        self.fromCurMenu.place(x=60, y=70, width=100, height=30)
        self.toCurLabel = tk.Label(root, text="To:", font=("Acme", 13))
        self.toCurLabel.place(x=200, y=70, width=40, height=30)
        self.toCurMenu = tk.OptionMenu(root, self.toCur, *self.codes)
        self.toCurMenu.place(x=240, y=70, width=100, height=30)
        self.amountLabel = tk.Label(root, text="Amount:", font=("Acme", 13))
        self.amountLabel.place(x=20, y=120, width=70, height=30)
        self.amountEntry = tk.Entry(root, width=30)
        self.amountEntry.place(x=100, y=120, width=100, height=30)
        self.convertButton = tk.Button(root, text="Convert", command=self.convert)
        self.convertButton.place(x=210, y=120, width=100, height=30)
        self.resultLabel = tk.Label(root, text="Result:", font=("Acme", 13))
        self.resultLabel.place(x=20, y=170, width=70, height=30)
        self.resultEntry = tk.Label(root, width=30, text="", font=("Acme", 13))
        self.resultEntry.place(x=95, y=170, width=100, height=30)
    
    def convert(self):
        amount = self.amountEntry.get()
        fromCur = self.fromCur.get()
        toCur = self.toCur.get()
        url = f"https://v6.exchangerate-api.com/v6/{self.API_KEY}/latest/{fromCur}"
        response = requests.get(url)
        data = response.json()
        self.resultEntry.config(text= str(float(amount) * data['conversion_rates'][toCur])+ " " + toCur)
        
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()