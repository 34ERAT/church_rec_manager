import customtkinter as ctk
from Navigation import Naviagation
from Preview import Preview
from BaptismTable import BaptismTable
from DeathTable import DeathTable 
from MarriageTable import  MarriageTable
from RecordManagers.Baptism_ import Edit_rec
ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Church Record Management system")
        self.geometry("400x150")
        # self.grid_columnconfigure((0,1), weight=1)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=2)
        self.grid_rowconfigure((0, 1), weight=1)
        self.attributes('-fullscreen',True)
        self.leftFrame = ctk.CTkFrame(self)
        self.leftFrame.configure(fg_color="transparent")
        self.leftFrame.grid(row=0, column=0, padx=0, pady=(10,0), sticky="nsew" ,rowspan=2,columnspan=1)
        self.leftFrame.grid_columnconfigure((0,1),weight=1)
        self.leftFrame.grid_rowconfigure((1),weight=1)
        self.navigate = Naviagation(self.leftFrame,width=700,height=100,command=self.window_selected)
        self.navigate.grid(row=0, column=0, padx=10, pady=(0), sticky="nsew" ,columnspan =2)

        #Default selection
        self.recordlist = BaptismTable(self.leftFrame,width=700,height=590)
        self.recordlist.grid(row=1, column=0, padx=10, pady=(10,10), sticky="nsew",columnspan=2)

        self.preview= Preview(self,width=600,height=00) 
        self.preview.grid(row=0, column=1, padx=(10,10), pady=(10,10), sticky="nsew",columnspan=2,rowspan=2)
        self.preview.set_image('/home/huble/new.jpg')
        self.preview.set_editor(Edit_rec)

    def window_selected(self,choice):
        if choice == "BAPTISIM":
            self.recordlist.destroy()
            self.recordlist = BaptismTable(self.leftFrame,width=700,height=590)
            self.recordlist.grid(row=1, column=0, padx=10, pady=(10,10), sticky="nsew",columnspan=2)
        elif choice == "MARRIAGE":
            self.recordlist.destroy()
            self.recordlist = MarriageTable(self.leftFrame,width=700,height=590)
            self.recordlist.grid(row=1, column=0, padx=10, pady=(10,10), sticky="nsew",columnspan=2)
        elif choice == "DEATH":
            self.recordlist.destroy()
            self.recordlist = DeathTable(self.leftFrame,width=700,height=590)
            self.recordlist.grid(row=1, column=0, padx=10, pady=(10,10), sticky="nsew",columnspan=2)
        else:
            self.recordlist.destroy()
            self.recordlist = BaptismTable(self.leftFrame,width=700,height=590)
            self.recordlist.grid(row=1, column=0, padx=10, pady=(10,10), sticky="nsew",columnspan=2)

app = App()
app.mainloop()
