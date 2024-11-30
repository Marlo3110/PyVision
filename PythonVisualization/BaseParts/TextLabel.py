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
        self.Type = "TextLabel"
        self.Children = []
        self.Monitor = self.Parent.Monitor

        self.AspectRatioX = AspectRatioX
        self.AspectRatioY = AspectRatioY
        self.AspectRatioXPosition = AspectRatioXPosition
        self.AspectRatioYPosition = AspectRatioYPosition
        self.Anchor = Anchor
        self.ALLOWEDTYPES = ["Window", "Frame"]
        # end #

        if self.Parent == None:
            return None

        # initialize label #
        self.Container = Tk.Label(self.Parent.Container, text = self.Text, fg = self.TextColor, bg = self.BackgroundColor)
        self.Parent.Children.append(self)

        if self.Parent.Type in self.ALLOWEDTYPES: # Fix bug that when self.AspectRatioYPosition is 0.125 and self.AspecRatioY is 0.25 that theres a small gap
            self.Container.place(relwidth = self.AspectRatioX, relheight = self.AspectRatioY,
                                  relx = self.AspectRatioXPosition, rely = self.AspectRatioYPosition,
                                  anchor = self.Anchor)
            self.Parent.Container.update()
            self.Container.config(wraplength = self.Parent.Container.winfo_width())
            print(self.Parent.Container.winfo_width())

        # end #

    def __repr__(self) -> str:

        return (f"// TextLabel|Text:{self.Text}|TextColor:{self.TextColor}|BackgroundColor:{self.BackgroundColor}|Parent:{self.Parent.__repr__()}|AspectRatioX:{self.AspectRatioX}|AspectRatioY:{self.AspectRatioY}|AspectRatioXPosition{self.AspectRatioXPosition}|AspectRatioYPosition:{self.AspectRatioYPosition} //")


    def InitializeLabel(self, Parent):
        self.Parent = Parent

        self.Container = Tk.Label(self.Parent, text = self.Text, fg = self.TextColor, bg = self.BackgroundColor)
        self.Parent.Children.append(self.__repr__())