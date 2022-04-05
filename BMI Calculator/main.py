import tkinter as tk


class App:
    def __init__(self, root):
        root.title("BMI Calculator")
        width=350
        height=250
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.App_label = tk.Label(root, text="BMI Calculator", font=("Acme", 24))
        self.App_label.place(x=0, y=15, height=45, width=350)
        self.height_label = tk.Label(root, text="Height (cm)", font=("Acme", 18))
        self.height_label.place(x=5, y=60, height=30, width=132)
        self.weight_label = tk.Label(root, text="Weight (kg)", font=("Acme", 18))
        self.weight_label.place(x=5, y=94, height=30, width=132)
        self.height_entry = tk.Entry(root, font=("Acme", 18))
        self.height_entry.place(x=138, y=60, height=30, width=200)
        self.weight_entry = tk.Entry(root, font=("Acme", 18))
        self.weight_entry.place(x=138, y=95, height=30, width=200)
        self.calculate_button = tk.Button(root, text="Calculate", font=("Acme", 13), command=self.calculate)
        self.calculate_button.place(x=125, y=140, height=25, width=100)
        self.bmi_value = tk.Label(root, text="BMI:        ", font=("Acme", 18))
        self.bmi_value.place(x=15, y=180, height=30, width=350)
        self.comment = tk.Label(root, text="", font=("Acme", 18))
        self.comment.place(x=0, y=210, height=30, width=350)
        
    def calculate(self):
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            bmi = round(weight / (height / 100) ** 2)
            self.bmi_value.config(text=f"BMI: {str(bmi)}")

            if(bmi<=16):
                self.comment.config(text="you are severely underweight")
            elif(bmi<=18.5):
                self.comment.config(text="you are underweight")
            elif(bmi<=25):
                self.comment.config(text="you are Healthy")
            elif(bmi<=30):
                self.comment.config(text="you are overweight")
            else:
                self.comment.config(text="you are severely overweight")

        except:
            self.bmi_value.config(text="Invalid Input")
        
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()