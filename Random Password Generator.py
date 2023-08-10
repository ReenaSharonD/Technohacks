import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())
        except ValueError:
            self.result_label.config(text="Please enter a valid length")
            return

        if password_length <= 0:
            self.result_label.config(text="Password length must be greater than 0")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))

        self.result_label.config(text="Generated Password: " + password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
