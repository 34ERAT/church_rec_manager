import customtkinter as ctk
from ui.Left_Frame import Left_Frame
from ui.Preview import Preview
ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Church Record Management system")
        self.geometry("400x150")
        # self.grid_columnconfigure((0,1), weight=1)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.attributes('-fullscreen',True)
        #leftFRame
        self.leftFRame = Left_Frame(self, command=self.change_editor,syc_preview_window=self.syc_editor_table)
        self.leftFRame.grid(row=0, column=0, padx=0, pady=(10,0), sticky="nsew" ,rowspan=2,columnspan=1)

        self.preview= Preview(self,width=720,default_editor="EDIT_BAPTISIM") 
        self.preview.grid(row=0, column=1, padx=(10,10), pady=(10,10), sticky="nsew",columnspan=2,rowspan=2)

        self.preview.set_image('/home/huble/new.jpg')

    def change_editor(self,editor):
        self.preview.update_editor(editor)
    def syc_editor_table(self,data):
        self.preview.set_image(data['file_url'])
        self.preview.set_data(data)





