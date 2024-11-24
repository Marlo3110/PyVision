import PythonVisualization.BaseParts as BP
from time import sleep, time

Window = BP.Window()

print(Window.Monitor)
print("")

def UpdateScreenSize():
    while True:
        StartTime = time()
        sleep(1)
        EndTime = time()
        
        DeltaTime = EndTime-StartTime
        Window.AspectRatioX += 0.1*DeltaTime*100
        Window.AspectRatioY += 0.1*DeltaTime*100
        Window.UpdateScreenSize()
        
        print(f"X: {Window.AspectRatioX}, Y: {Window.AspectRatioY}")

        Window.Window.update()

Window.MainLoop(UpdateScreenSize,1)