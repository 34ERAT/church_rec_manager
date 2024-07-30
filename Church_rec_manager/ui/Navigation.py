import customtkinter as ctk
class Naviagation(ctk.CTkFrame):
    def __init__(self,master,width,height,OPtions_callback,Mode_callback):
        super().__init__(master,width=width,height=height)
        # self.grid_propagate(False)
        self.grid_columnconfigure((0,1), weight=0)
        options = ["DEATH","MARRIAGE","BAPTISIM"]
        self.option_menu = ctk.CTkOptionMenu(master=self,values=options,command=OPtions_callback)
        self.option_menu.grid(row=0, column=0, padx=10,pady=(10, 10), sticky="ew" )
        self.option_menu.set(options[2]) 

        # Add new record button
        self.mode_btn = ctk.CTkSegmentedButton(
            master=self,
            values=[
                "Add Record",
                "Edit Record"
            ], 
            border_width=0, 
            unselected_hover_color="#0c0b14",
            command=Mode_callback
        )
        self.mode_btn.grid(
            row=0, column=1, padx=10, pady=(10, 10), sticky="ew")
        self.mode_btn.set("Edit Record")
    def update_Mode(self,Mode):
       self.mode_btn.set(Mode)
        
    def selected_option(self):
        return self.option_menu.get()
    def get_Mode(self):
        return self.mode_btn.get()


