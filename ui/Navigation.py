import customtkinter as ctk
class Naviagation(ctk.CTkFrame):
    def __init__(self,master,width,height,command):
        super().__init__(master,width=width,height=height)
        # self.grid_propagate(False)
        self.grid_columnconfigure((0,1), weight=0)
        #dropdown menu
        self.command = command
        options = ["DEATH","MARRIAGE","BAPTISIM"]
        self.option_menu = ctk.CTkOptionMenu(master=self,values=options,command=self.command)
        self.option_menu.grid(row=0, column=0, padx=10,pady=(10, 10), sticky="ew" )
        self.option_menu.set(options[2]) 

        # Add new record button
        self.Add_record_btn = ctk.CTkButton(master=self,text="Add Record",command=self.New_record)
        self.Add_record_btn.grid(row=0, column=1, padx=10, pady=(10, 10), sticky="ew")


    def New_record(self):
        print("ready_for the new record")


