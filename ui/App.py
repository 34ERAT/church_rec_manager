import customtkinter as ctk
from ui.Navigation import Naviagation
from ui.Preview import Preview
from ui.BaptismTable import BaptismTable
from ui.DeathTable import DeathTable 
from ui.MarriageTable import  MarriageTable
from ui.RecordManagers.Baptism_ import Add_Baptism, Edit_Baptism
from ui.RecordManagers.Death_ import Add_Death, Edit_Death
from ui.RecordManagers.Marriage_ import Add_Marriage, Edit_Marriage
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
        self.leftFrame = ctk.CTkFrame(self,width=570)
        self.leftFrame.grid_propagate(False)
        self.leftFrame.configure(fg_color="transparent" )
        self.leftFrame.grid(row=0, column=0, padx=0, pady=(10,0), sticky="nsew" ,rowspan=2,columnspan=1)
        self.leftFrame.grid_columnconfigure((0,1),weight=1)
        self.leftFrame.grid_rowconfigure((1),weight=1)
        self.navigate = Naviagation(self.leftFrame,width=700,height=100,OPtions_callback=self.window_selected,Mode_callback=self.mode)
        self.navigate.grid(row=0, column=0, padx=10, pady=(0), sticky="nsew" ,columnspan =2)

        #Default selection
        self.recordlist = BaptismTable(self.leftFrame,width=700,height=590)
        self.recordlist.grid(row=1, column=0, padx=10, pady=(10,10), sticky="nsew",columnspan=2)

        self.preview= Preview(self,width=720) 
        self.preview.grid(row=0, column=1, padx=(10,10), pady=(10,10), sticky="nsew",columnspan=2,rowspan=2)
        self.preview.set_image('/home/huble/new.jpg')
        self.preview.set_editor(Edit_Baptism)


    def mode(self,value):
        choice= self.navigate.selected_option()
        if choice == "BAPTISIM":
            if value == "Add Record":
                self.preview.set_editor(Add_Baptism)
            else:
                self.preview.set_editor(Edit_Baptism)

        if choice == "MARRIAGE":
            if value == "Add Record":
                self.preview.set_editor(Add_Marriage)
            else:
                self.preview.set_editor(Edit_Marriage)

        if choice == "DEATH":
            if value == "Add Record":
                self.preview.set_editor(Add_Death)
            else:
                self.preview.set_editor(Edit_Death)

    def window_selected(self,choice):
        if choice == "BAPTISIM":
            self.preview.set_editor(Edit_Baptism)
            self.__NEW_TABLE(BaptismTable)

        if choice == "MARRIAGE":
            self.preview.set_editor(Edit_Marriage)
            self.__NEW_TABLE(MarriageTable)
            # NotificationLabel(self,message="Added:-]",notification_type="success")

        if choice == "DEATH":
            self.preview.set_editor(Edit_Death)
            self.__NEW_TABLE(DeathTable)

    def __NEW_TABLE(self,Table):
        self.recordlist.destroy()
        self.recordlist = Table(self.leftFrame,width=700,height=590)
        self.recordlist.grid(row=1, column=0, padx=10, pady=(10,10), sticky="nsew",columnspan=2)

