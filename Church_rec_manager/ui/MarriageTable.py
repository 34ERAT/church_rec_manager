import customtkinter as ctk
from CTkTable import *
from Church_rec_manager.middleware.marriage import Marriage
from Church_rec_manager.ui.components.Table import Table
class search(ctk.CTkFrame):
    def __init__(self,master,command):
        super().__init__(master)
        self.command =command
        self.grid_columnconfigure((0,1),weight=1)
        self.grid_columnconfigure((2), weight=0)
        self.husband = ctk.CTkEntry(master=self,placeholder_text= "Husband")
        self.husband.grid(row=0, column=0, padx=(10,10),pady=(10, 10),sticky="ew")
        self.wife= ctk.CTkEntry(master=self,placeholder_text= "wife")
        self.wife.grid(row=0, column=1, padx=(10,10),pady=(10, 10),sticky="ew")

        self.Search= ctk.CTkButton(
            master=self,text="search", command=self.get)
        self.Search.grid(row=0, column=2, padx=(
            10, 10), pady=(10, 10), sticky="ew")

    def get(self):
        data = dict(husband= self.husband.get(),wife=self.wife.get())
        bapt = Marriage()
        result = bapt.get(h_name=data["husband"],w_name=data['wife'])
        self.command(result)


class MarriageTable(ctk.CTkFrame):
    def __init__(self,master,width,height,command=None):
        super().__init__(master,width=width,height=height)
        self.Command = command
        self.grid_columnconfigure((0), weight=1)
        self.search_input =  search(self,self.__ON_SEARCH)
        self.search_input.grid(row=0, column=0, padx=(10,10),pady=(10, 10),sticky="ew")
        self.record = Marriage()
        self.value = self.record.get_all()
        self.heading =["id","husband","wife"]

        self.table = Table(
            master=self,
            heading=self.heading,
            columns=3,
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
        marriage_rec = list(self.record.get_by_id(rec_id)[0])
        data= {
             "marriage_id":marriage_rec[0],
             "h_name":marriage_rec[1],
             "w_name":marriage_rec[2],
             "file_url":marriage_rec[3] 
         } 
        if self.Command is not None:
            self.Command(data)
