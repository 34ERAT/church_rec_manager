from CTkTable import *
class Table(CTkTable):
    def __init__(self,columns,heading,master,command):
        super().__init__(
            master=master,
            values=[heading],
            column=columns,
            header_color="#692c91",
            hover_color="#2b334f",
            command=command
        )

    def select_clicked_row(self,row):
        selected_row =self.get_selected_row()["row_index"]
        if selected_row is not None:
            self.deselect_row(selected_row)
        self.select_row(row)

    def Add_rows(self,Rows):
        if Rows is not None:
            for  i,row in enumerate(Rows):
                self.add_row(index=i+1,values=row)

    def clean_table(self):
        for i in range(len(self.get())):
            if i != 0 :
                self.delete_row(i)

    def update_table(self,new_value):
        self.clean_table()
        self.Add_rows(new_value)
