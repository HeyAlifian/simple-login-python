from customtkinter import CTk, CTkButton, CTkEntry, CTkCheckBox

class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self._set_appearance_mode("Dark".lower())
        self.title("Sign Up System")
        self.resizable(False, False)

        self.username = CTkEntry(self, placeholder_text="Enter your username")
        self.username.pack(padx=20,pady=10)

        self.password = CTkEntry(self, placeholder_text="Enter your password")
        self.password.pack(padx=20, pady=10)

        self.verify = CTkCheckBox(self, text="Are you a human?")
        self.verify.pack(padx=20, pady=10)

        self.button = CTkButton(self, text="Sign Up", command=self.button_sign_up)
        self.button.pack(padx=20, pady=10)

    def button_sign_up(self):
        if not self.username.get().strip() or not self.password.get().strip():
            print("Either username or password is incorrect.")
        else:
            if self.verify.get() == 0:
                print("Please verify that you are a human.")
            else:
                print(f"Signed up as {self.username.get()}")
                self.verify.deselect()
                self.username.delete(0, 'end')  # This clears the entry field
                self.password.delete(0, 'end')  # This clears the entry field
    
app = App()
app.mainloop()
