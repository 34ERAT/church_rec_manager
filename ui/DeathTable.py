import customtkinter as ctk
from CTkTable import *
from components.Table import Table
class search(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.grid_columnconfigure((0,1),weight=1)
        self.god_child = ctk.CTkEntry(master=self,placeholder_text= "Names")
        self.god_child.grid(row=0, column=0, padx=(10,10),pady=(10, 10),sticky="ew")
        # self.Parent= ctk.CTkEntry(master=self,placeholder_text= "Parent names")
        # self.Parent.grid(row=0, column=1, padx=(10,10),pady=(10, 10),sticky="ew")

    def get(self):
        return self.god_child.get()





class DeathTable(ctk.CTkFrame):
    def __init__(self,master,width,height):
        super().__init__(master,width=width,height=height)
        # self.grid_propagate(False)
        self.grid_columnconfigure((0), weight=1)
        self.search_input =  search(self)
        self.search_input.grid(row=0, column=0, padx=(10,10),pady=(10, 10),sticky="ew")
        self.value = [
            [1, 2, 3, 4 ],
            [1, 2, 3, 4 ],
            [1, 2, 3, 4 ],
            [1, 2, 3, 4 ],
            [1, 2, 3, 4 ]
            ]
        self.table = Table(
            master=self,
            heading=["death_id","name"],
            columns=2,
            command=self.on_click)
        self.table.grid(row=1, column=0, padx=(10,10), pady=(10,10), sticky="ew")
        self.table.Add_rows(self.value)

    def on_click(self,value):
        print("not in the some of the ",value["row"])
        self.table.select_clicked_row(value["row"])
