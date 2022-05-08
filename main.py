import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("ContactBook")
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.place(x=10, y= 25, width=200, height=250)

        self.contact_frame = ctk.CTkFrame(self.root)
        self.contact_frame.place(x=215, y= 25, width=265, height=250)


if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()