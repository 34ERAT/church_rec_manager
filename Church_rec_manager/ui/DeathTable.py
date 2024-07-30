import customtkinter as ctk
from CTkTable import *
from Church_rec_manager.middleware.death import Death
from Church_rec_manager.ui.components.Table import Table
class search(ctk.CTkFrame):
    def __init__(self,master,command):
        self.command = command
        super().__init__(master)
        self.grid_columnconfigure((0,1),weight=2)
        self.grid_columnconfigure((1),weight=0)
        self.name = ctk.CTkEntry(master=self,placeholder_text= "Names")
        self.name.grid(row=0, column=0, padx=(10,10),pady=(10, 10),sticky="ew")

        self.Search= ctk.CTkButton(
            master=self,text="search", command=self.get)
        self.Search.grid(row=0, column=1, padx=(
            10, 10), pady=(10, 10), sticky="ew")

    def get(self):
        data = dict(Names=self.name.get())
        death = Death()
        result = death.get(data["Names"])
        self.command(result)
        return self.name.get()

class DeathTable(ctk.CTkFrame):
    def __init__(self,master,width,height,command=None):
        super().__init__(master,width=width,height=height)
        self.Command = command
        self.grid_columnconfigure((0), weight=1)
        self.search_input =  search(self,self.__ON_SEARCH)
        self.search_input.grid(row=0, column=0, padx=(10,10),pady=(10, 10),sticky="ew")
        self.record = Death()
        self.value = self.record.get_all()
        self.heading = ["death_id","name"]
        self.table = Table(
            master=self,
            heading=self.heading,
            columns=2,
            command=self.on_click)
        self.table.grid(row=1, column=0, padx=(10,10), pady=(10,10), sticky="ew")
        self.table.Add_rows(self.value)

    def update_values(self):
        self.table.update_table(self.record.get_all())

    def __ON_SEARCH(self,result):
        self.table.update_table(result)

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
