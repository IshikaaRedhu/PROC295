from controller import Robot,Keyboard, Motion

robot = Robot()
keyboard = Keyboard()

forward = Motion("../../motions/Forwards50.motion")
backward = Motion("../../motions/Backwards.motion")
shoot = Motion("../../motions/Shoot.motion")
wave = Motion("../../motions/HandWave.motion")
turnleft60 = Motion("../../motions/TurnLeft60.motion")
turnright60 =  Motion("../../motions/TurnRight60.motion")
stepleft =  Motion("../../motions/SideStepLeft.motion")
stepright = Motion("../../motions/SideStepRight.motion")

timestep = 32

def print_msg() :
   print("Press Up to move forward.")
   print("Press Down to move backward.")
   print("Press 1 to shoot.")
   print("Press 2 to wave.")
   print("Press 3 to turn left.")
   print("Press 4 to turn right.")
   print("Press 5 to step left.")
   print("Press 6 to step right.")

print_msg()
key = -1

def startmotion(motion):
   motion.play()

while robot.step(timestep) != -1:
 
    key = keyboard.getKey()
    if key == Keyboard.UP:
       startmotion(forward)
    if key == Keyboard.DOWN:
       startmotion(backward)
    if key == 49 :
       startmotion(shoot)
    if key == 50 :
       startmotion(wave)
    if key == 51 :
       startmotion(turnleft60)
    if key == 52 :
       startmotion(turnright60)
    if key == 53 :
       startmotion(stepright)
    if key == 54 :
       startmotion(stepleft)
       
     
       