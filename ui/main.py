import customtkinter as ctk
ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("blue") 
class MyCheckboxFrame(ctk.CTkScrollableFrame):
    def __init__(self, master,title,values):
        super().__init__(master)
        self.values = values
        self.checkboxes = []
        self.title= title
        self.title = ctk.CTkLabel(self,text=self.title,fg_color="grey30",corner_radius=6)
        self.title.grid(row=0,column=0,padx=10,pady=(10,0),sticky='ew')

        for i, value in enumerate(self.values):
            check_box = ctk.CTkCheckBox(self,text=value)
            check_box.grid(row=i+1,column=0,padx=10,pady=(10,0), sticky='w')
            self.checkboxes.append(check_box)

    def get(self):
        checked_boxes=[]
        for check_box in self.checkboxes:
            if check_box.get() == 1:
                checked_boxes.append(check_box.cget("text"))
        return checked_boxes


class MyRadiobuttonFrame(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = ctk.StringVar(value="")

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = ctk.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("i am a simple application")
        self.geometry("400x150")
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        

        self.checkbox_frame_1 = MyCheckboxFrame(self,title="data", values=["value 1", "value 2", "value 3"])
        self.checkbox_frame_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.radiobutton_frame = MyRadiobuttonFrame(self, "Options", values=["option 1", "option 2"])
        self.radiobutton_frame.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")
        # self.checkbox_frame_2.configure(fg_color="transparent")
        ctk.CTkButton(
            self,
            text="my first button",
            command=self.button_pressed
        ).grid(row=3, column=0, padx=10, pady=10, sticky='ew', columnspan=2)

    def button_pressed(self):
        print("checke box from frame one" ,self.checkbox_frame_1.get())

app = App()
app.mainloop()
