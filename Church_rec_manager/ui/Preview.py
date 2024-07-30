import customtkinter as ctk 
from PIL import Image

from Church_rec_manager.ui.RecordManagers.Baptism_ import Add_Baptism, Edit_Baptism
from Church_rec_manager.ui.RecordManagers.Death_ import Add_Death, Edit_Death
from Church_rec_manager.ui.RecordManagers.Marriage_ import Add_Marriage, Edit_Marriage
class Preview(ctk.CTkFrame):
    def __init__(self,master,width,default_editor,command):
        super().__init__(master,width=width,)
        self.Command= command
        self.grid_propagate(False)
        self.configure(fg_color="transparent" )
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=2)
        self.label= ctk.CTkLabel(self,text="No Record Selected" ,height=400)
        self.label.grid_propagate(False)
        self.label.grid(row=0,column=0, pady=(10,0), sticky="nsew")
        self.image_path =None
        self.data_to_edit = None

        self.editor_Frame = ctk.CTkFrame(self)
        self.editor_Frame.grid(row=1,column=0 , pady=(10,0), sticky="nsew")

        self.editor = default_editor
        self.__EDIT_EDITOR()
        self.__ADD_EDITOR()

    def set_data(self,data):
        self.data_to_edit=data 
        self.__EDIT_EDITOR()


    def __EDIT_EDITOR(self):
        if self.editor == "EDIT_BAPTISIM":
            self.editor_Frame.destroy()
            self.editor_Frame= Edit_Baptism(self,command=self.set_image,On_Edit=self.Command)
            self.editor_Frame.grid_propagate(False)
            self.editor_Frame.grid(row=1,column=0 , pady=(10,0), sticky="nsew")
            if self.data_to_edit is not None:
                # print(self.data_to_edit)
                self.editor_Frame.set_entries(self.data_to_edit)
                self.data_to_edit = None

        if self.editor == "EDIT_MARRIAGE":
            self.editor_Frame.destroy()
            self.editor_Frame= Edit_Marriage(self,command=self.set_image,On_Edit=self.Command)
            self.editor_Frame.grid_propagate(False)
            self.editor_Frame.grid(row=1,column=0 , pady=(10,0), sticky="nsew")
            if self.data_to_edit is not None:
                # print(self.data_to_edit)
                self.editor_Frame.set_entries(self.data_to_edit)
                self.data_to_edit = None


        if self.editor == "EDIT_DEATH":
            self.editor_Frame.destroy()
            self.editor_Frame= Edit_Death(self,command=self.set_image,On_Edit=self.Command)
            self.editor_Frame.grid_propagate(False)
            self.editor_Frame.grid(row=1,column=0 , pady=(10,0), sticky="nsew")
            if self.data_to_edit is not None:
                # print(self.data_to_edit)
                self.editor_Frame.set_entries(self.data_to_edit)
                self.editor_Frame.set_death_id(self.data_to_edit['death_id'])
                self.data_to_edit = None

    def __ADD_EDITOR(self):
        if self.editor == "ADD_BAPTISIM":
            self.__EDITOR(Add_Baptism,self.Command)

        if self.editor == "ADD_MARRIAGE":
            self.__EDITOR(Add_Marriage,self.Command)

        if self.editor == "ADD_DEATH":
           self.__EDITOR(Add_Death,self.Command)


    def set_image(self,path):
        self.image_path = path
        self.image= ctk.CTkImage(
            light_image=Image.open(self.image_path),
            dark_image=Image.open(self.image_path),
            size=(720, 400)
        )
        self.label.configure(image=self.image ,text="") 

    def __EDITOR(self,Frame,on_add=None):
        if Frame  is not None:
            self.editor_Frame.destroy()
            if on_add is not None:
                self.editor_Frame =Frame(self,self.set_image,on_add)
            else:
                self.editor_Frame =Frame(self,self.set_image)
            self.editor_Frame.grid_propagate(False)
            self.editor_Frame.grid(row=1,column=0 , pady=(10,0), sticky="nsew")

    def update_editor(self,New_editor):
        self.editor = New_editor
        self.__EDIT_EDITOR()
        self.__ADD_EDITOR()



