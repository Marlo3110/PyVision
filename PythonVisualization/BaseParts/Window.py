import tkinter as Tk
from screeninfo import get_monitors

class Window:
    def __init__(self, WindowScaleType = "AbsoluteScale", Resizeable = False, Title = "My PythonVisualization window!", WindowSizeX = 500, WindowSizeY = 500, WindowAspectRatioX = 0.50, WindowAspectRatioY = 0.50,
                 UsePrimary = True):

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

    def UpdateScreenSize(self):
        """
        Updates the size of the window you changed with ObjectName.WindowSizeX/Y
        or ObjectName.AspectRatioX/Y. It wont change until you call this function.
        """

        if self.WindowScaleType == "AbsoluteScale":
            if self.WindowSizeX > self.Monitor.width or self.WindowSizeY > self.Monitor.height:
                return None
            self.Window.minsize(self.WindowSizeX, self.WindowSizeY)
            self.Window.maxsize(self.WindowSizeX, self.WindowSizeY)

        elif self.WindowScaleType == "RelativeScale":
            if self.AspectRatioX > 1 or self.AspectRatioY > 1:
                return None
            self.Window.minsize(self.Monitor.width/self.AspectRatioX, self.Monitor.height/self.AspectRatioY)
            self.Window.maxsize(self.Monitor.width/self.AspectRatioX, self.Monitor.height/self.AspectRatioY)



    def MainLoop(self, Function = None, Interval = 1000):
        if Function != None:
            self.Window.after(Interval, Function)
            self.Window.update()
        else:
            self.Window.mainloop()


    