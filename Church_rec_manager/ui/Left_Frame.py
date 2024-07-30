import customtkinter as ctk
from Church_rec_manager.ui.BaptismTable import BaptismTable
from Church_rec_manager.ui.DeathTable import DeathTable
from Church_rec_manager.ui.MarriageTable import MarriageTable
from Church_rec_manager.ui.Navigation import Naviagation

class Left_Frame(ctk.CTkFrame):
    def __init__(self,master,command,syc_preview_window):
        super().__init__(master=master,width=570)
        self.Command = command
        self.Get_values = syc_preview_window
        self.grid_propagate(False)
        self.configure(fg_color="transparent" )
        self.grid_columnconfigure((0,1),weight=1)
        self.grid_rowconfigure((1),weight=1)
        self.navigate = Naviagation(self,width=700,height=100,OPtions_callback=self.window_selected,Mode_callback=self.mode)
        self.navigate.grid(row=0, column=0, padx=10, pady=(0), sticky="nsew" ,columnspan =2)

        #Default selection
        self.recordlist = BaptismTable(self,width=700,height=590,command=self.selected_data)
        self.recordlist.grid(row=1, column=0, padx=10, pady=(10,10), sticky="nsew",columnspan=2)

    def selected_data(self,data):
        self.Get_values(data) 
    def update_Table(self):
        self.recordlist.update_values()

    def mode(self,value):
        choice= self.navigate.selected_option()
        if choice == "BAPTISIM":
            if value == "Add Record":
                self.Command("ADD_BAPTISIM")
            else:
                self.Command("EDIT_BAPTISIM")

        if choice == "MARRIAGE":
            if value == "Add Record":
                self.Command("ADD_MARRIAGE")
            else:
                self.Command("EDIT_MARRIAGE")

        if choice == "DEATH":
            if value == "Add Record":
                self.Command("ADD_DEATH")
            else:
                self.Command("EDIT_DEATH")

    def window_selected(self, choice):
        if choice == "BAPTISIM":
            self.Command("EDIT_BAPTISIM")
            self.__NEW_TABLE(BaptismTable,self.selected_data)

        if choice == "MARRIAGE":
            self.Command("EDIT_MARRIAGE")
            self.__NEW_TABLE(MarriageTable,self.selected_data)

        if choice == "DEATH":
            self.Command("EDIT_DEATH")
            self.__NEW_TABLE(DeathTable,self.selected_data)

    def __NEW_TABLE(self,Table,command=None):
        self.recordlist.destroy()
        if command is not None:
            self.recordlist = Table(self,width=700,height=590,command=command)
        else:
            self.recordlist = Table(self,width=700,height=590)
        self.navigate.update_Mode("Edit Record")
        self.recordlist.grid(row=1, column=0, padx=10, pady=(10,10), sticky="nsew",columnspan=2)
