from tkinter import END
import customtkinter as ctk
from Church_rec_manager.middleware.marriage import Marriage
from Church_rec_manager.ui.components.Btn_Notify import Btn_Notify
from CTkMessagebox import CTkMessagebox


class Marriage_rec(ctk.CTkFrame):
    def __init__(self, master, command):
        super().__init__(master)
        self.Command = command
        self.columnconfigure(0, weight=0)
        self.columnconfigure((1, 2), weight=2)
        self.rowconfigure((0, 1, 2, 3), weight=1)

        self.Label(0, "marriage id")
        self.marriage_id = ctk.CTkEntry(self, placeholder_text="marriage id")
        self.marriage_id.grid(row=0, column=1, padx=(
            10, 0), pady=(10, 0), sticky="ew")
        self.Label(1, "husband Names")
        self.husband = ctk.CTkEntry(
            self, placeholder_text="first_name  last_name ")
        self.husband.grid(row=1, column=1, padx=(
            10, 0), pady=(10, 0), sticky="ew")

        self.Label(2, 'Wife name')
        self.wife = ctk.CTkEntry(
            self, placeholder_text="first_name  last_name ")
        self.wife.grid(row=2, column=1, padx=(
            10, 0), pady=(10, 0), sticky="ew")

        self.image_path = None

        # choose file
        self.filepick = ctk.CTkButton(
            self, text="choose a file ...", command=self.selected_file)
        self.filepick.grid(row=0, column=2, padx=(
            10, 10), pady=(10, 0), sticky="ew")

    def selected_file(self):
        self._FILE_PATH = ctk.filedialog.askopenfilename(
            title="Select a file", filetypes=[("image files", "*.jpg"), ("All files", "*.*")])
        self.image_path = self._FILE_PATH
        self.Command(self._FILE_PATH)

    def set_image(self, path):
        self.image_path = path

    def get_entries(self):
       data = {
           "marriage_id": self.marriage_id.get(),
           "h_name": self.husband.get(),
           "w_name": self.wife.get(),
           "file_url": self.image_path
       }
       return data

    def set_entries(self, data):
        self.marriage_id.insert(0, data["marriage_id"])
        self.husband.insert(0, data["h_name"])
        self.wife.insert(0, data["w_name"])
        self.set_image(data["file_url"])

    def clear_entries(self):
        self.marriage_id.configure(state="normal")
        self.marriage_id.delete(0, END)
        self.husband.configure(state="normal")
        self.husband.delete(0, END)
        self.wife.configure(state="normal")
        self.wife.delete(0, END)
        self.set_image(None)

    def Label(self, row, text):
        label = ctk.CTkLabel(self, text=text)
        label.grid(row=row, column=0, padx=(
            10, 0), pady=(10, 0), sticky="ew")
        return label


class Edit_Marriage(Marriage_rec):

    def __init__(self, master, command, On_Edit=None):
        super().__init__(master, command=command)
        self.on_edit = On_Edit
        self.Delete = Btn_Notify(self, text="Delete",command=self.DELETE)
        self.Delete.grid(row=1, column=2, padx=(
            10,10), pady=(0, 0), sticky="ew")
        self.Edit = Btn_Notify(self, text="Edit", command=self.EDIT)
        self.Edit.grid(row=2, column=2, padx=(
            10, 10), pady=(0, 0), sticky="ew")

    def EDIT(self):
        try:
            self.marriage = Marriage()
            self.marriage.update(self.get_entries())
            self.Edit.set_message(success=True, msg_id=1)
            if self.on_edit is not None:
                self.on_edit()
        except:
            self.Edit.set_message(success=False,)

    def DELETE(self):
        try:
            msg = CTkMessagebox(title="delete?", message="Are About to delete this Record",
                        icon="question", option_1="No", option_2="yes")
            if msg.get() == "yes":
                self.marriage = Marriage()
                self.marriage.delete(self.marriage_id.get())
                self.Delete.set_message(success=True, msg_id=1)
                if self.on_edit is not None:
                    self.on_edit()
                self.clear_entries()
        except:
            self.Delete.set_message(success=False,)

class Add_Marriage(Marriage_rec,):

    def __init__(self, master, command, on_add=None):
        super().__init__(master, command=command)
        self.On_add = on_add
        self.Add = Btn_Notify(self, text="Add", command=self.submit)
        self.Add.grid(row=2, column=2, padx=(
            10, 10), pady=(0, 0), sticky="ew")

    def submit(self):
        try:
            self.baptims = Marriage()
            self.baptims.Add(self.get_entries())
            self.Add.set_message(success=True, msg_id=0)
            if self.On_add is not None:
                self.On_add()
            self.clear_entries()
        except:
            self.Add.set_message(success=False,)
