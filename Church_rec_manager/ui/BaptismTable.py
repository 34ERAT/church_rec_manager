import customtkinter as ctk
from Church_rec_manager.middleware.Baptism import BAPTISM
from Church_rec_manager.ui.components.Table import Table
class search(ctk.CTkFrame):
    def __init__(self, master ,command):
        super().__init__(master)
        self.command= command
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_columnconfigure((2), weight=0)
        self.god_child = ctk.CTkEntry(
            master=self, placeholder_text="god child names")
        self.god_child.grid(row=0, column=0, padx=(
            10, 10), pady=(10, 10), sticky="ew")
        self.Parent = ctk.CTkEntry(
            master=self, placeholder_text="Parent names")
        self.Parent.grid(row=0, column=1, padx=(
            10, 10), pady=(10, 10), sticky="ew")

        self.Search= ctk.CTkButton(
            master=self,text="search", command=self.get)
        self.Search.grid(row=0, column=2, padx=(
            10, 10), pady=(10, 10), sticky="ew")

    def get(self):
        data = dict(god_child=self.god_child.get(), parent=self.Parent.get())
        bapt = BAPTISM()
        result = bapt.get(data["god_child"],data['parent'])
        self.command(result)


class BaptismTable(ctk.CTkFrame):
    def __init__(self, master, width, height,command=None):
        super().__init__(master, width=width, height=height)
        self.Command = command
        self.grid_columnconfigure((0), weight=1)
        self.search_input = search(self,self.__ON_SEARCH)
        self.search_input.grid(row=0, column=0, padx=(
            10, 10), pady=(10, 10), sticky="ew")

        self.record = BAPTISM()
        self.value =self.record.get_all()
        self.heading = ["id", "god_child", "mother_name" ,"Father_name"]
        self.table = Table(
            master=self,
            heading=self.heading,
            columns=4,
            command=self.on_click)
        self.table.grid(row=1, column=0, padx=(
            10, 10), pady=(10, 10), sticky="ew")
        self.table.Add_rows(self.value)

    def update_values(self):
        self.table.update_table(self.record.get_all())
    def __ON_SEARCH(self,result):
        self.table.update_table(result)


    def on_click(self, value):
        # print("not in the some of the ", value["row"])
        self.table.select_clicked_row(value["row"])
        rec_id = self.value[value["row"]-1][0]
        Btp_rec = list(self.record.get_by_no(rec_id)[0])

        data= {
             "baptism_no":Btp_rec[0],
             "godchild":Btp_rec[1],
             "mother":Btp_rec[2],
             "father": Btp_rec[3],
             "file_url":Btp_rec[4] 
         } 
        if self.Command is not None:
            self.Command(data)



