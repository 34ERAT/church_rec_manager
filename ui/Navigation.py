import customtkinter as ctk
class Naviagation(ctk.CTkFrame):
    def __init__(self,master,width,height):
        super().__init__(master,width=width,height=height)
        # self.grid_propagate(False)
        # self.grid_columnconfigure((0,1,2), weight=1)

        #dropdown menu
        options = ["DEATH","MARRIAGE","BAPTISIM"]
        self.option_menu = ctk.CTkOptionMenu(master=self,values=options,)
        self.option_menu.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="ew")
        self.option_menu.set("Select recorde") 

        # Add new record button
        self.Add_record_btn = ctk.CTkButton(master=self,text="Add Record",command=self.New_record)
        self.Add_record_btn.grid(row=0, column=1, padx=10, pady=(10, 10), sticky="ew")

        #Search for a record
        self.search_input = ctk.CTkEntry(master=self,placeholder_text= "search records")
        self.search_input.bind('<Return>',self.get_data)
        self.search_input.grid(row=0, column=2, padx=10,pady=(10, 10),sticky="ew")

    def get_select(self):
        return self.option_menu.get()

    def get_data(self,event):
        print("not in the some of the ",self.search_input.get())

    def New_record(self):
        print("ready_for the new record")


