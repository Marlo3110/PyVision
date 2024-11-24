import PythonVisualization.BaseParts as BP
from time import sleep, time

Window = BP.Window(WindowScaleType = "RelativeScale", WindowAspectRatioX = 0.50, WindowAspectRatioY = 0.50)

print(Window.Monitor)
print("")

#def UpdateScreenSize():
#    while True:
#        StartTime = time()
#        sleep(1)
#        EndTime = time()
#        
#        DeltaTime = EndTime-StartTime
#        Window.AspectRatioX += 0.1*DeltaTime*100
#        Window.AspectRatioY += 0.1*DeltaTime*100
#        Window.UpdateScreenSize()
#        
#        print(f"X: {Window.AspectRatioX}, Y: {Window.AspectRatioY}")
#
#        Window.Window.update()

Window.SetScreenSize(AspectRatioX = 0.50, AspectRatioY = 0.50)
Window.UpdateScreenSize()

def Test():
    Window.SetScreenSize(AspectRatioX = 0.75, AspectRatioY = 0.75)
Window.MainLoop(Test, 1000)