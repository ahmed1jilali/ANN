import tkinter as tk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from tkinter import filedialog

class RandomPlotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Number Plotter")
        self.data = []

        # Configure root window grid layout
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)  # Right column resizes

        # Left frame for buttons
        left_frame = tk.Frame(self.root)
        left_frame.grid(row=0, column=0, sticky='ns')

        # Close button
        self.close_button = tk.Button(left_frame, text="Close", command=self.root.quit)
        self.close_button.pack(padx=10, pady=10)

        # Save button
        self.save_button = tk.Button(left_frame, text="Save Plot", command=self.save_plot)
        self.save_button.pack(padx=10, pady=10)

        # Right frame for canvas
        right_frame = tk.Frame(self.root)
        right_frame.grid(row=0, column=1, sticky='nsew')
        right_frame.rowconfigure(0, weight=1)
        right_frame.columnconfigure(0, weight=1)

        # Set up matplotlib figure with fixed dimensions (e.g., 8x6 inches)
        self.fig, self.ax = plt.subplots(figsize=(8, 6))  # Fixed size for saved plot
        self.line, = self.ax.plot([], [], 'b-o')

        # Embed figure into Tkinter with fixed size for the canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=right_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=0, column=0, sticky='nsew')

        # Fix the canvas size (same size as the plot figure)
        self.canvas_widget.config(width=800, height=600)  # Fixed width & height in pixels

        # Start the animation
        self.ani = animation.FuncAnimation(self.fig, self.update_plot, interval=1000)

    def update_plot(self, frame):
        new_value = random.randint(1, 100)
        self.data.append(new_value)
        self.line.set_data(range(len(self.data)), self.data)
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

    def save_plot(self):
        # Ask user where to save the plot as PNG
        file_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                                filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")])
        if file_path:
            # Desired image size in pixels
            width_pixels = 1280
            height_pixels = 629
            dpi = 100  # Set DPI (dots per inch)

            # Calculate figure size in inches based on desired pixel size and DPI
            width_in_inches = width_pixels / dpi
            height_in_inches = height_pixels / dpi

            # Set the figure size (in inches) for the plot
            self.fig.set_size_inches(width_in_inches, height_in_inches)

            # Save the current plot as a PNG with fixed image dimensions
            self.fig.savefig(file_path, dpi=dpi, bbox_inches='tight')  # Save with the calculated dimensions
            print(f"Plot saved as {file_path}")



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x500")  # Optional: set a default size
    app = RandomPlotApp(root)
    root.mainloop()
