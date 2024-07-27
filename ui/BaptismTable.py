import customtkinter as ctk
from middleware.Baptism import BAPTISM
from ui.components.Table import Table

class search(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure((0, 1), weight=1)
        self.god_child = ctk.CTkEntry(
            master=self, placeholder_text="god child names")
        self.god_child.grid(row=0, column=0, padx=(
            10, 10), pady=(10, 10), sticky="ew")
        self.Parent = ctk.CTkEntry(
            master=self, placeholder_text="Parent names")
        self.Parent.grid(row=0, column=1, padx=(
            10, 10), pady=(10, 10), sticky="ew")

    def get(self):
        return dict(god_child=self.god_child.get(), parent=self.Parent.get())


class BaptismTable(ctk.CTkFrame):
    def __init__(self, master, width, height,command=None):
        super().__init__(master, width=width, height=height)
        # self.grid_propagate(False)
        self.Command = command
        self.grid_columnconfigure((0), weight=1)
        self.search_input = search(self)
        self.search_input.grid(row=0, column=0, padx=(
            10, 10), pady=(10, 10), sticky="ew")

        self.record = BAPTISM()
        self.value =self.record.get_all()

        self.table = Table(
            master=self,
            heading=["id", "god_child", "Father_name", "mother_name"],
            columns=4,
            command=self.on_click)
        self.table.grid(row=1, column=0, padx=(
            10, 10), pady=(10, 10), sticky="ew")
        self.table.Add_rows(self.value)

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



