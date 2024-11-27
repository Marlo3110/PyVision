import tkinter as Tk


class Frame:
    def __init__(self, Parent: any = None, BackgroundColor: str = "FFFFFF", AspectRatioX:float = 0.5, AspectRatioY:float = 0.5,
                 AspectRatioXPosition:float = 0.5, AspectRatioYPosition:float = 0.5, Anchor:str = "center"
                 ):

        # Variables #
        self.BgColor = "#"+BackgroundColor
        self.Parent = Parent
        self.Type = "Frame"
        self.Container = Tk.Frame(self.Parent.Container, bg = self.BgColor)
        self.Anchor = Anchor
        self.Children = []

        self.AspectRatioX = AspectRatioX
        self.AspectRatioY = AspectRatioY
        self.AspectRatioXPosition = AspectRatioXPosition
        self.AspectRatioYPosition = AspectRatioYPosition
        # end #


        self.Container.place(relwidth = self.AspectRatioX, relheight = self.AspectRatioY,
                              relx = self.AspectRatioXPosition, rely = self.AspectRatioYPosition,
                              anchor = self.Anchor)

        

