import tkinter as tk
import customtkinter as ctk

class FrameA(ctk.CTkFrame):
    def __init__(self, parent, shared_var):
        super().__init__(parent)
        self.shared_var = shared_var
        self.shared_var.trace("w", self.update_entry)

        # Entry widget to display and modify the shared variable
        self.entry = ctk.CTkEntry(self, textvariable=self.shared_var)
        self.entry.pack(pady=10)

        # Button to change the shared variable
        self.update_button = ctk.CTkButton(self, text="Update in Frame A", command=self.update_var)
        self.update_button.pack(pady=10)

    def update_entry(self, *args):
        # This method will be called whenever the shared_var is updated
        print("Frame A detected change:", self.shared_var.get())

    def update_var(self):
        # Update the shared variable
        self.shared_var.set("Updated by Frame A")

class FrameB(ctk.CTkFrame):
    def __init__(self, parent, shared_var):
        super().__init__(parent)
        self.shared_var = shared_var
        self.shared_var.trace("w", self.update_entry)

        # Entry widget to display and modify the shared variable
        self.entry = ctk.CTkEntry(self, textvariable=self.shared_var)
        self.entry.pack(pady=10)

        # Button to change the shared variable
        self.update_button = ctk.CTkButton(self, text="Update in Frame B", command=self.update_var)
        self.update_button.pack(pady=10)

    def update_entry(self, *args):
        # This method will be called whenever the shared_var is updated
        print("Frame B detected change:", self.shared_var.get())

    def update_var(self):
        # Update the shared variable
        self.shared_var.set("Updated by Frame B")

def main():
    root = ctk.CTk()
    root.title("Shared Variable Example")
    root.geometry("400x300")

    # Shared variable
    shared_var = ctk.StringVar()

    # Create frames and pass the shared variable
    frame_a = FrameA(root, shared_var)
    frame_a.pack(side="left", expand=True, fill="both", padx=10, pady=10)

    frame_b = FrameB(root, shared_var)
    frame_b.pack(side="right", expand=True, fill="both", padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

