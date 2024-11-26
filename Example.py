import PythonVisualization.BaseParts as BP
from time import sleep, time

Window = BP.Window(WindowScaleType = "RelativeScale", WindowAspectRatioX = 0.50, WindowAspectRatioY = 0.50)
NewLabel = BP.TextLabel(Parent = Window, AspectRatioXPosition = 0.5, AspectRatioX= 1)
NewLabelNew = BP.TextLabel(BackgroundColor = "FFFFFF", TextColor = "000000",Parent = Window, AspectRatioXPosition = 0.50, AspectRatioYPosition= 0.25, AspectRatioX= 0.5)

print(Window.Monitor)
print("")

Window.SetScreenSize(AspectRatioX = 0.75, AspectRatioY = 0.75)
Window.UpdateScreenSize()


for i in Window.Children:
    print(i)
    print("")

Window.MainLoop()