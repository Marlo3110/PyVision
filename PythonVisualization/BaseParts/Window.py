import tkinter as Tk
from screeninfo import get_monitors

class Window:
    def __init__(self, WindowScaleType = "AbsoluteScale", Resizeable = True, Title = "My PythonVisualization window!", WindowSizeX = 500, WindowSizeY = 500, WindowAspectRatioX = 0.50, WindowAspectRatioY = 0.50
                 ):

        # Define self variables
        self.WindowScaleType = WindowScaleType
        self.Resizeable = Resizeable
        self.Title = Title

        self.WindowSizeX = WindowSizeX
        self.WindowSizeY = WindowSizeY

        self.AspectRatioX = WindowAspectRatioX
        self.AspectRatioY = WindowAspectRatioY
        
        self.Window = Tk.Tk(self.Title)
        #

    def UpdateScreenSize(self):
        print("Updating screensize")

    