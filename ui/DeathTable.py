import customtkinter as ctk
from CTkTable import *
from middleware.death import Death
from ui.components.Table import Table
class search(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.grid_columnconfigure((0,1),weight=1)
        self.god_child = ctk.CTkEntry(master=self,placeholder_text= "Names")
        self.god_child.grid(row=0, column=0, padx=(10,10),pady=(10, 10),sticky="ew")

    def get(self):
        return self.god_child.get()





class DeathTable(ctk.CTkFrame):
    def __init__(self,master,width,height,command=None):
        super().__init__(master,width=width,height=height)
        self.Command = command
        self.grid_columnconfigure((0), weight=1)
        self.search_input =  search(self)
        self.search_input.grid(row=0, column=0, padx=(10,10),pady=(10, 10),sticky="ew")
        self.record = Death()
        self.value = self.record.get_all()
        self.table = Table(
            master=self,
            heading=["death_id","name"],
            columns=2,
            command=self.on_click)
        self.table.grid(row=1, column=0, padx=(10,10), pady=(10,10), sticky="ew")
        self.table.Add_rows(self.value)

    def on_click(self,value):
        self.table.select_clicked_row(value["row"])
        rec_id = self.value[value["row"]-1][0]
        death_rec = list(self.record.get_by_id(rec_id)[0])
        data= {
             "death_id":death_rec[0],
             "Names":death_rec[1],
             "file_url":death_rec[2],
         } 
        if self.Command is not None:
            self.Command(data)
