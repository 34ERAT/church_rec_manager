from tkinter import END
import customtkinter as ctk

from middleware.marriage import Marriage
from ui.components.Btn_Notify import Btn_Notify

class Marriage_rec(ctk.CTkFrame):
    def __init__(self, master,command):
        super().__init__(master)
        self.Command = command
        self.columnconfigure(0, weight=0)
        self.columnconfigure((1,2), weight=2)
        self.rowconfigure((0, 1, 2,3), weight=1)

        self.Label(0,"marriage id")
        self.marriage_id = ctk.CTkEntry(self,placeholder_text="marriage id")
        self.marriage_id.grid(row=0, column=1, padx=(
            10,0 ), pady=(10, 0), sticky="ew")
        self.Label(1,"husband Names")
        self.husband = ctk.CTkEntry(self, placeholder_text="first_name  last_name ")
        self.husband.grid(row=1, column=1, padx=(
            10, 0), pady=(10, 0), sticky="ew")

        self.Label(2,'Wife name')
        self.wife = ctk.CTkEntry(self,placeholder_text= "first_name  last_name ")
        self.wife.grid(row=2, column=1, padx=(
            10, 0), pady=(10, 0), sticky="ew")


        self.image_path =None

        #choose file
        self.filepick= ctk.CTkButton(self,text="choose a file ...",command=self.selected_file)
        self.filepick.grid(row=1, column=2, padx=(
            10, 10), pady=(10, 0), sticky="ew")


    def selected_file(self):
        self._FILE_PATH =ctk.filedialog.askopenfilename(title="Select a file", filetypes=[("image files", "*.jpg"), ("All files", "*.*")])
        self.image_path= self._FILE_PATH
        self.Command(self._FILE_PATH)

    def set_image(self,path):
        self.image_path = path

    def get_entries(self):
       data = {
           "marriage_id":self.marriage_id.get(),
           "h_name": self.husband.get(),
           "w_name": self.wife.get(),
           "file_url": self.image_path
       }
       return data

    def clear_entries(self):
            self.marriage_id.configure(state="normal")
            self.marriage_id.delete(0,END)
            self.husband.configure(state="normal")
            self.husband.delete(0,END)
            self.wife.configure(state="normal")
            self.wife.delete(0,END)

    def Label(self, row, text):
        label = ctk.CTkLabel(self, text=text)
        label.grid(row=row, column=0, padx=(
            10,0 ), pady=(10, 0), sticky="ew")
        return label

class Edit_Marriage(Marriage_rec):
    def __init__(self, master,command):
        super().__init__(master,command=command)

        self.Edit = Btn_Notify(self, text="Edit",command=self.submit)
        self.Edit.grid(row=3, column=2, padx=(
            10,10), pady=(0, 0), sticky="ew")

    def submit(self):
        try:
            self.marriage = Marriage()
            self.marriage.update(self.get_entries())
            self.Edit.set_message(success=True,message="Edited")
        except:
            self.Edit.set_message(success=False,message="Error")
class Add_Marriage(Marriage_rec):
    def __init__(self, master,command):
        super().__init__(master,command=command)
        self.Add = Btn_Notify(self, text="Add",command=self.submit)
        self.Add.grid(row=3, column=2, padx=(
            10,10), pady=(0, 0), sticky="ew")

    def submit(self):
        try:
            self.baptims = Marriage()
            self.baptims.Add(self.get_entries())
            self.Add.set_message(success=True,message="Added:-]")
            self.clear_entries()
        except:
            self.Add.set_message(success=False,message="Error")


