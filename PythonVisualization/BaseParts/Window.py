import tkinter as Tk
from screeninfo import get_monitors

class Window:
    def __init__(self, WindowScaleType = "AbsoluteScale", Resizeable = False, Title = "My PythonVisualization window!", 
                 WindowSizeX = 500, WindowSizeY = 500, WindowAspectRatioX = 0.50, WindowAspectRatioY = 0.50, 
                 UsePrimary = True) -> None:
        
        """
        Create you window to contain all your frames or other objects.

        See documentation for more information.
        """

        # Define self variables
        self.WindowScaleType = WindowScaleType
        self.Resizeable = Resizeable
        self.Title = Title

        self.WindowSizeX = WindowSizeX
        self.WindowSizeY = WindowSizeY

        self.AspectRatioX = WindowAspectRatioX
        self.AspectRatioY = WindowAspectRatioY
        
        self.Window = Tk.Tk(self.Title)
        self.UsePrimary = UsePrimary
        self.Type = "Window"
        self.Children = []
        # end #

        # Select monitor #
        if self.UsePrimary == True:
            for i in get_monitors():
                if i.is_primary == True:
                    self.Monitor = i
        else:
            self.Monitor = get_monitors()[0]
        # end # 

        # Change resizeability #
        self.Window.resizable(self.Resizeable, self.Resizeable)
        self.UpdateScreenSize()

    def UpdateScreenSize(self, Print = False) -> None:
        """
        Updates the size of your window object.
        """

        if self.WindowScaleType == "AbsoluteScale":
            if self.WindowSizeX > self.Monitor.width or self.WindowSizeY > self.Monitor.height:
                return None
            self.Window.minsize(self.WindowSizeX, self.WindowSizeY)
            self.Window.maxsize(self.WindowSizeX, self.WindowSizeY)

        elif self.WindowScaleType == "RelativeScale":
            if self.AspectRatioX > 1 or self.AspectRatioY > 1:
                return None
            self.Window.minsize(int(self.AspectRatioX*self.Monitor.width), int(self.AspectRatioY*self.Monitor.height))
            self.Window.maxsize(int(self.AspectRatioX*self.Monitor.width), int(self.AspectRatioY*self.Monitor.height))

        
    def SetScreenSize(self, NewX = None, NewY = None, AspectRatioX = None, AspectRatioY = None, AutoUpdate = True,
                       Print = False) -> None:
        
        """
        Set the screen size of your window object. Either use RelativeScale or AbsoluteScale(see documentation).
        """

        if self.WindowScaleType == "AbsoluteScale":
            self.WindowSizeX = NewX
            self.WindowSizeY = NewY

        elif self.WindowScaleType == "RelativeScale":
            self.AspectRatioX = AspectRatioX
            self.AspectRatioY = AspectRatioY

        if AutoUpdate == True:
            self.UpdateScreenSize(Print)
            
    def MainLoop(self, Function = None, Interval:int = 1000) -> None:
        """
        Initiates the tk.mainloop() function. You can also use the parameter "Function" to 
        run "Interval"(ms) after the mainloop started.
        """
        if Function != None:
            self.Window.after(ms = Interval, func = Function)
            self.Window.mainloop()
        else:
            self.Window.mainloop()

    def __repr__(self) -> str:

        return (f"// Window|WindowScaleType:{self.WindowScaleType}|Title:{self.Title}| //")


    