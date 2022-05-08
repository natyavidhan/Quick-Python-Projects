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

        ctk.CTkLabel(self.main_frame, text="ContactBook", text_font=("Comic Sans MS", 23), justify="center").place(x=0, y=5)

        self.contact_list = tk.Listbox(self.main_frame)
        self.contact_list.place(x=10, y=50, width=180, height=150)

        ctk.CTkButton(self.main_frame, text="Add", command=self.add_contact, text_font=("Comic Sans MS", 18)).place(x=10, y=205, width=180, height=35)

    def add_contact(self):
        pass


if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()