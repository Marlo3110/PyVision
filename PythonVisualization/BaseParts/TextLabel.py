import tkinter as Tk

class TextLabel:


    def __init__(self, Text:str = "TextLabel", TextColor:str = "FFFFFF", Parent:any = None, AspectRatioX:float = 0.5,
                  AspectRatioY:float = 0.5, AspectRatioXPosition:float = 0.5, AspectRatioYPosition:float = 0.5,
                  BackgroundColor:str = "000000", Anchor:str = "center") -> None:

        # Variables #
        self.Text = Text
        self.TextColor = "#"+TextColor
        self.BackgroundColor = "#"+BackgroundColor
        self.Parent = Parent

        self.AspectRatioX = AspectRatioX
        self.AspectRatioY = AspectRatioY
        self.AspectRatioXPosition = AspectRatioXPosition
        self.AspectRatioYPosition = AspectRatioYPosition
        self.Anchor = Anchor
        # end #

        # initialize label #
        self.TextLabel = Tk.Label(self.Parent.Window, text = self.Text, fg = self.TextColor, bg = self.BackgroundColor)
        self.Parent.Children.append(self.__repr__())

        if self.Parent.Type == "Window":
            self.TextLabel.place(relwidth = self.AspectRatioX, relheight = self.AspectRatioY,
                                  relx = self.AspectRatioXPosition, rely = self.AspectRatioYPosition,
                                  anchor = self.Anchor)
            


        # end #

    def __repr__(self) -> str:

        return (f"// TextLabel|Text:{self.Text}|TextColor:{self.TextColor}|BackgroundColor:{self.BackgroundColor}|Parent:{self.Parent.__repr__()}|AspectRatioX:{self.AspectRatioX}|AspectRatioY:{self.AspectRatioY}|AspectRatioXPosition{self.AspectRatioXPosition}|AspectRatioYPosition:{self.AspectRatioYPosition} //")
