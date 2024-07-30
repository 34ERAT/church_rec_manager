from tkinter import END
import customtkinter as ctk
from Church_rec_manager.middleware.death import Death
from Church_rec_manager.ui.components.Btn_Notify import Btn_Notify
from CTkMessagebox import CTkMessagebox

class DEATH_rec(ctk.CTkFrame):
    def __init__(self, master,command):
        super().__init__(master)
        self.Command=command
        self.columnconfigure(0, weight=0)
        self.columnconfigure((1,2), weight=2)
        self.rowconfigure((0, 1, 2,3), weight=1)

        self.Label(0,'Names')

        self.Names = ctk.CTkEntry(self,placeholder_text="first_name  last_name ")
        self.Names.grid(row=0, column=1, padx=(
            10,0 ), pady=(10, 0), sticky="ew")
        self.image_path =None
        #choose file
        self.filepick= ctk.CTkButton(self,text="choose a file ...",command=self.selected_file)
        self.filepick.grid(row=1, column=2, padx=(
            10, 10), pady=(10, 0), sticky="ew")


    def set_entries(self,data):
        self.Names.insert(0,str(data["Names"]))
        self.set_image( data["file_url"])

    def set_image(self,path):
        self.image_path = path

    def selected_file(self):
        self._FILE_PATH =ctk.filedialog.askopenfilename(title="Select a file", filetypes=[("image files", "*.jpg"), ("All files", "*.*")])
        self.image_path= self._FILE_PATH
        self.Command(self._FILE_PATH)


    def Label(self, row, text):
        label = ctk.CTkLabel(self, text=text)
        label.grid(row=row, column=0, padx=(
            10,0 ), pady=(10, 0), sticky="ew")
        return label

    def get_entries(self):
       data= {
                "Names":self.Names.get(),
                "file_url":self.image_path 
            } 
       return data
    def clear_entries(self):
            self.Names.configure(state="normal")
            self.Names.delete(0,END)

class Edit_Death(DEATH_rec):
    def __init__(self, master,command,On_Edit=None):
        super().__init__(master,command=command)
        self.on_edit = On_Edit
        self.Delete = Btn_Notify(self, text="Delete",command=self.DELETE)
        self.Delete.grid(row=2, column=2, padx=(
            10,10), pady=(0, 0), sticky="ew")
        self.Edit = Btn_Notify(self, text="Edit",command=self.EDIT)
        self.Edit.grid(row=3, column=2, padx=(
            10,10), pady=(0, 0), sticky="ew")
        self.death_id = None
    def set_death_id(self,id):
        self.death_id = id

    def EDIT(self):
        try:
            if self.death_id is None:
                return self.Edit.set_message(success=False)
            self.death = Death()
            data = self.get_entries()
            data['death_id']=self.death_id
            self.death.update(data=data)
            if self.on_edit is not None :
                self.on_edit()
            self.Edit.set_message(success=True,msg_id=1)
        except:
            self.Edit.set_message(success=False)

    def DELETE(self):
        try:
            msg = CTkMessagebox(title="delete?", message="Are About to delete this Record",
                        icon="question", option_1="No", option_2="yes")
            if msg.get() == "yes":
                if self.death_id is None:
                    return self.Delete.set_message(success=False)
                self.death = Death()
                print(self.death_id)
                self.death.delete(self.death_id)
                if self.on_edit is not None :
                    self.on_edit()
                self.Delete.set_message(success=True,msg_id=1)
                self.clear_entries()
        except:
            self.Edit.set_message(success=False)
class Add_Death(DEATH_rec):

    def __init__(self, master,command,on_add=None):
        super().__init__(master,command=command)
        self.On_add =  on_add
        self.Add = Btn_Notify(self, text="Add",command=self.submit)
        self.Add.grid(row=3, column=2, padx=(
            10,10), pady=(0, 0), sticky="ew")

    def submit(self):
        try:
            self.death = Death()
            self.death.Add(self.get_entries())
            self.Add.set_message(success=True,msg_id=0)
            if self.On_add is not None :
                self.On_add()
            self.clear_entries()
        except:
            self.Add.set_message(success=False)

