import customtkinter as ctk 
from PIL import Image
class Preview(ctk.CTkFrame):
    def __init__(self,master,width,height):
        super().__init__(master,width=width,height=height)
        # self.grid_propagate(False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=3)
        self.label= ctk.CTkLabel(self,text="")
        self.label.grid(row=0,column=0, padx=(2,2), pady=(10,10), sticky="nsew")

        # self.set_image("/home/huble/mpv-shot0001.jpg")
        self.EditFrame = ctk.CTkFrame(self)
        self.EditFrame.grid(row=1,column=0 ,padx=(2,2), pady=(10,10), sticky="nsew")
        ctk.CTkButton(self.EditFrame,text="heell you allj<").grid(sticky="nsew")


    def set_image(self,path):
        self.image= ctk.CTkImage(
            light_image=Image.open(path),
            dark_image=Image.open(path),
            size=(720, 400)
        )
        self.label.configure(image=self.image) 

    def set_editor(self,Frame):
        if Frame  is not None:
            self.EditFrame.destroy()
            self.EditFrame =Frame(self)
            self.EditFrame.grid(row=1,column=0 ,padx=(2,2), pady=(10,10), sticky="nsew")


