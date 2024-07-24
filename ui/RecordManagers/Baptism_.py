import customtkinter as ctk
from components.Table import Table

class Baptism_rec(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.columnconfigure(0, weight=0)
        self.columnconfigure((1,2), weight=2)
        self.rowconfigure((0, 1, 2,3), weight=1)
        # baptism
        self.bptlabel=ctk.CTkLabel(self,text="baptism_no")
        self.bptlabel.grid(row=0, column=0, padx=(
            10,0 ), pady=(10, 0), sticky="ew")

        self.baptism_no = ctk.CTkEntry(self,placeholder_text="baptism_no")
        self.baptism_no.grid(row=0, column=1, padx=(
            10,0 ), pady=(10, 0), sticky="ew")
        #god_child
        self.Label(1,"god child")
        self.godchild = ctk.CTkEntry(self, placeholder_text="god child")
        self.godchild.grid(row=1, column=1, padx=(
            10, 0), pady=(10, 0), sticky="ew")

        self.Label(2,'Father name')
        self.father_names = ctk.CTkEntry(self,placeholder_text= "father_names")
        self.father_names.grid(row=2, column=1, padx=(
            10, 0), pady=(10, 0), sticky="ew")

        self.Label(3,'Mother names')
        self.mother_names = ctk.CTkEntry(self,placeholder_text="mother_names")
        self.mother_names.grid(row=3, column=1, padx=(
            10, 0), pady=(10, 0), sticky="ew")

        #choose file
        self.filepick= ctk.CTkButton(self,text="choose a file ...",command=self.import_file)
        self.filepick.grid(row=1, column=2, padx=(
            10, 0), pady=(0, 0), sticky="ew")
        # #Edit 
        # self.Edit = ctk.CTkButton(self, text="Edit")
        # self.Edit.grid(row=3, column=2, padx=(
        #     10, 0), pady=(10, 0), sticky="ew")
        


    def import_file(self):
        file_path =ctk.filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        print(f"file_path{file_path}")


    def Label(self, row, text):
        label = ctk.CTkLabel(self, text=text)
        label.grid(row=row, column=0, padx=(
            10,0 ), pady=(10, 0), sticky="ew")
        return label

class Edit_rec(Baptism_rec):
    def __init__(self, master):
        super().__init__(master)

        self.Edit = ctk.CTkButton(self, text="Edit")
        self.Edit.grid(row=3, column=2, padx=(
            10, 0), pady=(10, 0), sticky="ew")

class Add_rec(Baptism_rec):
    def __init__(self, master):
        super().__init__(master)

        self.Edit = ctk.CTkButton(self, text="Edit")
        self.Edit.grid(row=3, column=2, padx=(
            10, 0), pady=(10, 0), sticky="ew")

