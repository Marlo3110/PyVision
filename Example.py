import PythonVisualization.BaseParts as BP
from time import sleep, time

Window = BP.Window(WindowScaleType="RelativeScale", WindowAspectRatioX=0.75, WindowAspectRatioY=0.75)
MainFrame = BP.Frame(Window, BackgroundColor="FF0000", AspectRatioX=0.8, AspectRatioY=0.8)
Label1 = BP.TextLabel("TITLE", TextColor="FFFFFF", Parent=MainFrame, BackgroundColor="000000",
                   AspectRatioX=1, AspectRatioY=0.25, AspectRatioXPosition=0.5, AspectRatioYPosition=0.125)
Text123 = """
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt 
ut labore et dolore magna aliquyam erat,
 sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd 
 gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
   Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor 
   invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.
 At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
   no sea takimata sanctus est Lorem ipsum dolor sit amet."""
Label2 = BP.TextLabel(Text123, Parent = MainFrame, AspectRatioX = 0.75,
                       AspectRatioY = 0.75, AspectRatioYPosition = 0.625, AspectRatioXPosition = 0, Anchor = "w")
WeatherTitle = BP.TextLabel("Weather", Parent = MainFrame, AspectRatioX = 0.25, AspectRatioY = 0.25,
                             AspectRatioXPosition = 0.75, AspectRatioYPosition = 0.25, Anchor = "nw",
                             BackgroundColor = "FFFFFF", TextColor="000000")
WeatherText = BP.TextLabel("Today's weather is sunny and nice!", Parent = MainFrame, AspectRatioX = 0.25, AspectRatioY = 0.5,
                           AspectRatioXPosition = 0.75,AspectRatioYPosition = 0.5, Anchor = "nw",
                           BackgroundColor = "FFA000")

print(Window.Monitor)
print("")

Window.SetScreenSize(AspectRatioX = 0.75, AspectRatioY = 0.75)
Window.UpdateScreenSize()
NewI = Window
def TEST123():
    global NewI
    for i in NewI.Children:
        print(i.__repr__())
        print("")
        if i.Children != []:
            NewI = i
            TEST123()

Window.MainLoop()