import tkinter as tk
import customtkinter as ctk
import json

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("ContactBook")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        self.data = []
        self.current_contact = None

        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.place(x=10, y=25, width=200, height=250)

        self.contact_frame = ctk.CTkFrame(self.root)
        self.contact_frame.place(x=215, y=25, width=265, height=250)

        ctk.CTkLabel(
            self.main_frame,
            text="ContactBook",
            text_font=("Comic Sans MS", 23),
            justify="center",
        ).place(x=0, y=5)

        self.contact_list = tk.Listbox(self.main_frame)
        self.contact_list.place(x=10, y=50, width=180, height=150)
        self.contact_list.bind("<<ListboxSelect>>", self.open_contact)

        ctk.CTkButton(
            self.main_frame,
            text="Add",
            command=self.add_contact,
            text_font=("Comic Sans MS", 18),
        ).place(x=10, y=205, width=180, height=35)

        ctk.CTkLabel(
            self.contact_frame,
            text="Name",
            text_font=("Comic Sans MS", 15),
            justify="center",
        ).place(x=0, y=25, width=85, height=25)
        ctk.CTkLabel(
            self.contact_frame,
            text="Phone",
            text_font=("Comic Sans MS", 15),
            justify="center",
        ).place(x=0, y=60, width=85, height=25)
        ctk.CTkLabel(
            self.contact_frame,
            text="Email",
            text_font=("Comic Sans MS", 15),
            justify="center",
        ).place(x=0, y=95, width=85, height=25)
        ctk.CTkLabel(
            self.contact_frame,
            text="Address",
            text_font=("Comic Sans MS", 12),
            justify="center",
        ).place(x=0, y=130, width=85, height=70)

        self.name_entry = ctk.CTkEntry(
            self.contact_frame, text_font=("Comic Sans MS", 12)
        )
        self.name_entry.place(x=85, y=25, width=165, height=25)
        self.phone_entry = ctk.CTkEntry(
            self.contact_frame, text_font=("Comic Sans MS", 12)
        )
        self.phone_entry.place(x=85, y=60, width=165, height=25)
        self.email_entry = ctk.CTkEntry(
            self.contact_frame, text_font=("Comic Sans MS", 12)
        )
        self.email_entry.place(x=85, y=95, width=165, height=25)
        self.address_entry = tk.Text(
            self.contact_frame,
            bg="gray24",
            relief="flat",
            borderwidth=0,
            font=("Comic Sans MS", 12),
            fg="white",
        )
        self.address_entry.place(x=85, y=130, width=165, height=70)

        ctk.CTkButton(
            self.contact_frame,
            text="Save",
            command=self.save_contact,
            text_font=("Comic Sans MS", 13),
        ).place(x=15, y=205, width=115, height=35)
        ctk.CTkButton(
            self.contact_frame,
            text="Delete",
            command=self.delete_contact,
            text_font=("Comic Sans MS", 13),
            fg_color="#C11818",
            hover_color="#A80B0B",
        ).place(x=135, y=205, width=115, height=35)

        self.load_data()

    def add_contact(self):
        prompt = ctk.CTkToplevel(self.root)
        prompt.title("Add Contact")
        prompt.geometry("265x250")
        prompt.resizable(False, False)

        ctk.CTkLabel(
            prompt, text="Name", text_font=("Comic Sans MS", 15), justify="center"
        ).place(x=0, y=25, width=85, height=25)
        ctk.CTkLabel(
            prompt, text="Phone", text_font=("Comic Sans MS", 15), justify="center"
        ).place(x=0, y=60, width=85, height=25)
        ctk.CTkLabel(
            prompt, text="Email", text_font=("Comic Sans MS", 15), justify="center"
        ).place(x=0, y=95, width=85, height=25)
        ctk.CTkLabel(
            prompt, text="Address", text_font=("Comic Sans MS", 12), justify="center"
        ).place(x=0, y=130, width=85, height=70)

        name_entry = ctk.CTkEntry(prompt, text_font=("Comic Sans MS", 12))
        name_entry.place(x=85, y=25, width=165, height=25)
        phone_entry = ctk.CTkEntry(prompt, text_font=("Comic Sans MS", 12))
        phone_entry.place(x=85, y=60, width=165, height=25)
        email_entry = ctk.CTkEntry(prompt, text_font=("Comic Sans MS", 12))
        email_entry.place(x=85, y=95, width=165, height=25)
        address_entry = tk.Text(
            prompt,
            bg="gray24",
            relief="flat",
            borderwidth=0,
            font=("Comic Sans MS", 12),
            fg="white",
        )
        address_entry.place(x=85, y=130, width=165, height=70)

        def add_contact_logic():
            name = name_entry.get()
            phone = phone_entry.get()
            email = email_entry.get()
            address = address_entry.get("1.0", tk.END)
            self.data.append(
                {"name": name, "phone": phone, "email": email, "address": address}
            )
            json.dump(self.data, open("data.json", "w"))
            self.load_data()
            self.contact_list.selection_set(-1)
            self.load_data()
            prompt.destroy()

        ctk.CTkButton(
            prompt,
            text="Save",
            command=add_contact_logic,
            text_font=("Comic Sans MS", 13),
        ).place(x=85, y=205, width=165, height=35)

    def save_contact(self):
        if type(self.current_contact) is tuple:
            current_contact = self.data[self.current_contact[0]]
            current_contact["name"] = self.name_entry.get()
            current_contact["phone"] = self.phone_entry.get()
            current_contact["email"] = self.email_entry.get()
            current_contact["address"] = self.address_entry.get("1.0", tk.END)
            json.dump(self.data, open("data.json", "w"))
            self.load_data()

    def load_data(self):
        data = json.load(open("data.json"))
        self.contact_list.delete(0, tk.END)
        for contact in data:
            self.contact_list.insert(tk.END, contact["name"])
        self.data = data

    def open_contact(self, args):
        selection = self.contact_list.curselection()
        if selection:
            self.current_contact = selection
            selected = self.contact_list.get(selection)
            for contact in self.data:
                if contact["name"] == selected:
                    self.name_entry.delete(0, tk.END)
                    self.name_entry.insert(0, contact["name"])
                    self.phone_entry.delete(0, tk.END)
                    self.phone_entry.insert(0, contact["phone"])
                    self.email_entry.delete(0, tk.END)
                    self.email_entry.insert(0, contact["email"])
                    self.address_entry.delete("1.0", tk.END)
                    self.address_entry.insert("1.0", contact["address"])
                    break

    def delete_contact(self):
        if type(self.current_contact) is tuple:
            self.data.pop(self.current_contact[0])
            json.dump(self.data, open("data.json", "w"))
            self.load_data()
            self.current_contact = None
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.address_entry.delete("1.0", tk.END)


if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
