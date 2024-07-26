import customtkinter as ctk 
from PIL import Image
class Preview(ctk.CTkFrame):
    def __init__(self,master,width):
        super().__init__(master,width=width,)
        self.grid_propagate(False)
        self.configure(fg_color="transparent" )
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=2)
        self.label= ctk.CTkLabel(self,text="")
        self.label.grid(row=0,column=0, pady=(10,0), sticky="nsew")
        self.image_path =None

        # self.set_image("/home/huble/mpv-shot0001.jpg")
        self.REc_Frame = ctk.CTkFrame(self)
        self.REc_Frame.grid(row=1,column=0 , pady=(10,0), sticky="nsew")
        # ctk.CTkButton(self.REc_Frame,text="heell you allj<").grid(sticky="nsew")


    def set_image(self,path):
        self.image_path = path
        self.image= ctk.CTkImage(
            light_image=Image.open(self.image_path),
            dark_image=Image.open(self.image_path),
            size=(720, 400)
        )
        self.label.configure(image=self.image) 

    def set_editor(self,Frame):
        if Frame  is not None:
            self.REc_Frame.destroy()
            self.REc_Frame =Frame(self,self.set_image)
            self.REc_Frame.grid_propagate(False)
            # self.REc_Frame.Set_image_path(self.image_path)
            self.REc_Frame.grid(row=1,column=0 , pady=(10,0), sticky="nsew")


