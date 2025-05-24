import tkinter as tk
from tkinter import filedialog, messagebox

class SimpleEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Tkinter App")
        self.root.geometry("600x400")

        # Create the menu bar
        menubar = tk.Menu(root)
        file_menu = tk.Menu(menubar, tearoff=0)

        # File menu items
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        menubar.add_cascade(label="File", menu=file_menu)

        # Attach the menu to the root window
        root.config(menu=menubar)

        # Add a text area
        self.text_area = tk.Text(root, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        self.current_file = None

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.root.title("New File - Simple Tkinter App")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)
            self.current_file = file_path
            self.root.title(f"{file_path} - Simple Tkinter App")

    def save_file(self):
        if self.current_file:
            with open(self.current_file, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.current_file = file_path
            self.root.title(f"{file_path} - Simple Tkinter App")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleEditorApp(root)
    root.mainloop()
