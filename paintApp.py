import tkinter as tk
from tkinter import colorchooser

class PaintApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Paint Tool")

        # Initialize variables
        self.selected_color = "black"
        self.selected_shape = "line"
        self.start_x = None
        self.start_y = None

        # Create UI elements
        self.create_canvas()
        self.create_labelsandbuttons()
        self.create_shape_buttons()

    # def create_color_chooser_button(self):
        

    def create_labelsandbuttons(self):
        tk.Button(
            self.root,
            text="Choose Color",
            command=self.choose_color
        ).pack(side=tk.TOP, pady=10)
        
        tk.Label(self.root, text="Selected Color:").pack(side=tk.TOP, pady=(5, 0))
        self.color_label = tk.Label(self.root, text=self.selected_color)
        self.color_label.pack(side=tk.TOP, pady=5)

        tk.Label(self.root, text="Selected Shape:").pack(side=tk.TOP, pady=(10, 0))
        self.shape_label = tk.Label(self.root, text=self.selected_shape.capitalize())
        self.shape_label.pack(side=tk.TOP, pady=5)

    def create_shape_buttons(self):
        shape_frame = tk.Frame(self.root)
        shape_frame.pack(side=tk.TOP, pady=10)

        tk.Button(
            shape_frame,
            text="Line",
            command=lambda: self.set_shape("line")
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            shape_frame,
            text="Rectangle",
            command=lambda: self.set_shape("rectangle")
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            shape_frame,
            text="Oval",
            command=lambda: self.set_shape("oval")
        ).pack(side=tk.LEFT, padx=5)

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, width=400, height=300, bg="white")
        self.canvas.pack(side=tk.RIGHT, padx=10, pady=10)
        self.canvas.bind("<Button-1>", self.draw_shape)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.selected_color = color
            self.color_label.config(text=self.selected_color)

    def set_shape(self, shape):
        self.selected_shape = shape
        self.shape_label.config(text=self.selected_shape.capitalize())

    def draw_shape(self, event):
        if self.start_x is None:
            self.start_x, self.start_y = event.x, event.y
        else:
            if self.selected_shape == "line":
                self.canvas.create_line(
                    self.start_x, self.start_y, event.x, event.y,
                    fill=self.selected_color, width=2
                )
            elif self.selected_shape == "rectangle":
                self.canvas.create_rectangle(
                    self.start_x, self.start_y, event.x, event.y,
                    fill=self.selected_color, outline=self.selected_color, width=2
                )
            elif self.selected_shape == "oval":
                self.canvas.create_oval(
                    self.start_x, self.start_y, event.x, event.y,
                    fill=self.selected_color, outline=self.selected_color, width=2
                )
            self.start_x, self.start_y = None, None

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
