import customtkinter as ctk
class Preview(ctk.CTkFrame):
    def __init__(self,master,title,width,height):
        super().__init__(master,width=width,height=height)
        # self.grid_propagate(False)
        self.title = title
        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
