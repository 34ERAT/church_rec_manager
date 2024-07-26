import customtkinter as ctk
class Btn_Notify(ctk.CTkFrame):
    def __init__(self,master,text,command):
        super().__init__(master=master)
        self.columnconfigure(0,weight=2)
        self.columnconfigure(1,weight=2)
        self.configure(fg_color='transparent')
        self.btn = ctk.CTkButton(self, text=text,command=command)
        self.btn.grid_propagate(False)
        self.btn.grid(row=0, column=0, padx=(
            0,10), pady=(10, 0), sticky="nsew")

        self.NotificationLabel= ctk.CTkLabel(self,text="")
        self.NotificationLabel.grid(row=0, column=1, padx=(
            0,10), pady=(10, 0), sticky="nsew")

    def __CLRMSG(self):
        self.NotificationLabel.configure(fg_color="transparent",text="")
    def set_message(self,success,message):
        if success:
            self.NotificationLabel.configure(fg_color="#0b8a20",text=message, text_color="white")
        else:
            self.NotificationLabel.configure(fg_color="#cf4c3c",text=message, text_color="white")
        self.after(500, self.__CLRMSG)

