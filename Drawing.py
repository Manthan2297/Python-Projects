import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App with Pen Thickness")

        self.brush_color = "black"
        self.pen_thickness = 3  # Default pen thickness

        self.draw_history = []

        # Create color buttons for color selection
        color_buttons_frame = tk.Frame(self.root)
        color_buttons_frame.pack(side=tk.LEFT, padx=10)

        self.color_button_black = tk.Button(color_buttons_frame, text="Black", bg="black", command=lambda: self.set_color("black"))
        self.color_button_black.pack(side=tk.TOP, padx=5, pady=5)

        self.color_button_red = tk.Button(color_buttons_frame, text="Red", bg="red", command=lambda: self.set_color("red"))
        self.color_button_red.pack(side=tk.TOP, padx=5, pady=5)

        self.color_button_green = tk.Button(color_buttons_frame, text="Green", bg="green", command=lambda: self.set_color("green"))
        self.color_button_green.pack(side=tk.TOP, padx=5, pady=5)

        self.color_button_blue = tk.Button(color_buttons_frame, text="Blue", bg="blue", command=lambda: self.set_color("blue"))
        self.color_button_blue.pack(side=tk.TOP, padx=5, pady=5)

        # Create thickness control buttons
        thickness_frame = tk.Frame(self.root)
        thickness_frame.pack(side=tk.LEFT, padx=10)

        self.thickness_button_2 = tk.Button(thickness_frame, text="2px", command=lambda: self.set_thickness(2))
        self.thickness_button_2.pack(side=tk.TOP, padx=5, pady=5)

        self.thickness_button_5 = tk.Button(thickness_frame, text="5px", command=lambda: self.set_thickness(5))
        self.thickness_button_5.pack(side=tk.TOP, padx=5, pady=5)

        self.thickness_button_10 = tk.Button(thickness_frame, text="10px", command=lambda: self.set_thickness(10))
        self.thickness_button_10.pack(side=tk.TOP, padx=5, pady=5)

        # Create the canvas for drawing
        self.canvas = tk.Canvas(self.root, width=500, height=400, bg="white")
        self.canvas.pack(side=tk.LEFT)

        # Bind the drawing function to mouse movement
        self.canvas.bind("<B1-Motion>", self.draw)

        # Clear Canvas Button
        clear_button = tk.Button(self.root, text="Clear Canvas", font=("Arial", 14), command=self.clear_canvas)
        clear_button.pack(pady=10)

    def set_color(self, color):
        self.brush_color = color

    def set_thickness(self, thickness):
        self.pen_thickness = thickness

    def draw(self, event):
        if self.brush_color:
            # Draw a circle with the selected color and pen thickness
            x1, y1, x2, y2 = event.x - self.pen_thickness, event.y - self.pen_thickness, event.x + self.pen_thickness, event.y + self.pen_thickness
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, width=self.pen_thickness)
            self.draw_history.append(('oval', x1, y1, x2, y2, self.brush_color, self.pen_thickness))

    def clear_canvas(self):
        self.canvas.delete("all")  # Clear the entire canvas
        self.draw_history = []  # Clear drawing history


# Create the root Tkinter window
root = tk.Tk()

# Create an instance of the DrawingApp class
drawing_app = DrawingApp(root)

# Run the Tkinter event loop
root.mainloop()
