#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
left_motor_a = Motor(Ports.PORT1, 2.5, False)
left_motor_b = Motor(Ports.PORT3, 2.5, False)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)

right_motor_a = Motor(Ports.PORT7, 2.5, True)
right_motor_b = Motor(Ports.PORT9, 2.5, True)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 200, 173, 76, MM, 1)
catapult_sensor = Bumper(Ports.PORT2)
left_diff = Motor(Ports.PORT4, False)
right_diff = Motor(Ports.PORT10, False)
claw_thing = Pneumatic(Ports.PORT12)
controller = Controller()
touchled_8 = Touchled(Ports.PORT8)



# generating and setting random seed
def initializeRandomSeed():
    wait(100, MSEC)
    xaxis = brain_inertial.acceleration(XAXIS) * 1000
    yaxis = brain_inertial.acceleration(YAXIS) * 1000
    zaxis = brain_inertial.acceleration(ZAXIS) * 1000
    systemTime = brain.timer.system() * 100
    urandom.seed(int(xaxis + yaxis + zaxis + systemTime)) 
    
# Initialize random seed 
initializeRandomSeed()

#endregion VEXcode Generated Robot Configuration
from vex import *
# ------------------------------------------
# 
# 	Project:      VEXcode Project
# 	Author:       VEX
# 	Created:
# 	Description:  VEXcode IQ Python Project
# 
# ------------------------------------------
intake_broadcast = Event()
loading = False
drivetrain.set_stopping(BRAKE)
left_diff.set_stopping(HOLD)
right_diff.set_stopping(HOLD)
left_diff.set_velocity(100, PERCENT)
right_diff.set_velocity(100, PERCENT)

def l4():
    wait(0.5, SECONDS)
    left_diff.set_velocity(100, PERCENT)
    right_diff.set_velocity(100, PERCENT)
    left_diff.spin_for(FORWARD, 50, DEGREES, wait=False)
    right_diff.spin_for(FORWARD, 50, DEGREES)
    wait(0.2, SECONDS)
    left_diff.set_timeout(1.25, SECONDS)
    right_diff.set_timeout(1.25, SECONDS)
    left_diff.spin_for(FORWARD, 10, DEGREES, wait=False)
    right_diff.spin_for(FORWARD, 10, DEGREES)
    wait(0.2, SECONDS)
    left_diff.spin_for(FORWARD, 50, DEGREES, wait=False)
    right_diff.spin_for(FORWARD, 50, DEGREES)
    wait(0.2, SECONDS)
    Wind_up()
    drivetrain.set_timeout(0.5, SECONDS)
    drivetrain.drive_for(REVERSE, 30, MM)
    drivetrain.set_timeout(0, SECONDS)


def intake():
    global loading, claw
    loading = True
    claw_thing.retract(CYLINDER1)
    claw = True
    drivetrain.drive_for(REVERSE, 100, MM)
    right_diff.set_timeout(1, SECONDS)
    left_diff.set_timeout(1, SECONDS)
    right_diff.spin_for(FORWARD, 235, DEGREES, wait=False)
    left_diff.spin_for(REVERSE, 235, DEGREES)
    claw_thing.extend(CYLINDER1)
    wait(0.5, SECONDS)
    right_diff.set_timeout(0, SECONDS)
    left_diff.set_timeout(0, SECONDS)
    claw = False
    right_diff.spin_for(REVERSE, 235, DEGREES, wait=False)
    left_diff.spin_for(FORWARD, 235, DEGREES)
    drivetrain.set_timeout(1, SECONDS)
    drivetrain.turn_for(RIGHT, 5, DEGREES)
    drivetrain.set_timeout(0, SECONDS)
    loading = False
def Launch_load():
    global myVariable, claw, console_thingy, screen_precision, console_precision, loading
    while not loading == False:
        pass
    wait(0.5, SECONDS)
    left_diff.set_velocity(100, PERCENT)
    right_diff.set_velocity(100, PERCENT)
    left_diff.spin_for(FORWARD, 50, DEGREES, wait=False)
    right_diff.spin_for(FORWARD, 50, DEGREES)
    wait(0.2, SECONDS)
    left_diff.set_timeout(1.25, SECONDS)
    right_diff.set_timeout(1.25, SECONDS)
    left_diff.spin_for(FORWARD, 10, DEGREES, wait=False)
    right_diff.spin_for(FORWARD, 10, DEGREES)
    wait(0.2, SECONDS)
    left_diff.spin_for(FORWARD, 50, DEGREES, wait=False)
    right_diff.spin_for(FORWARD, 50, DEGREES)
    wait(0.2, SECONDS)
    Wind_up()
    drivetrain.set_timeout(0.5, SECONDS)
    drivetrain.drive_for(REVERSE, 30, MM)
    drivetrain.set_timeout(0, SECONDS)
def Wind_up():
    global myVariable, claw, console_thingy, screen_precision, console_precision
    left_diff.spin(REVERSE)
    right_diff.spin(REVERSE)
    while not catapult_sensor.pressing():
        wait(20, MSEC)
    left_diff.stop()
    right_diff.stop()


def intake_broadcast_callback_0():
    global intake_broadcast
    intake()
    wait(0.5, SECONDS)
def timed_run():
    while not brain.buttonCheck.pressing():
        wait(20, MSEC)
    touchled_8.set_color(Color.RED_ORANGE)
    while True:
        if brain.timer.time(SECONDS) > 60:
            touchled_8.set_color(Color.PURPLE)
def init():
    touchled_8.set_color(Color.BLACK)
    right_diff.set_stopping(BRAKE)
    left_diff.set_stopping(BRAKE)
    Wind_up()
    claw_thing.retract(CYLINDER2)
    claw_thing.extend(CYLINDER1)
    touchled_8.set_color(Color.BLUE_GREEN)
    
def main():
    global intake_broadcast
    init()
    while not touchled_8.pressing():
        wait(20, MSEC)
        brain.timer.clear()
    right_diff.set_stopping(HOLD)
    left_diff.set_stopping(HOLD)
    claw_thing.extend(CYLINDER2)

    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(50, PERCENT)

    #-------Drive to the Level 4 pole-------

    drivetrain.drive_for(REVERSE, 90, MM)
    drivetrain.turn_for(LEFT, 35, DEGREES)
    drivetrain.set_timeout(0.75, SECONDS)
    drivetrain.drive_for(REVERSE, 375, MM)
    wait(0.5, SECONDS)
    
    #-------Launch it towards Level 4-------

    l4()
    drivetrain.drive_for(FORWARD, 275, MM)
    claw_thing.retract(CYLINDER2)

    drivetrain.set_turn_velocity(100, PERCENT)
    drivetrain.set_drive_velocity(100, PERCENT)
    wait(1,SECONDS)
    drivetrain.turn_for(RIGHT, 140, DEGREES)

    #-------On pole-------

    drivetrain.set_timeout(1, SECONDS)
    drivetrain.drive_for(REVERSE, 1000, MM)

    #-------Add a bit of force to get over the pole-------

    drivetrain.set_timeout(0.25, SECONDS)
    drivetrain.drive_for(REVERSE, 10, MM)

    #------Drive towards the next bean bag-------

    drivetrain.set_timeout(0,SECONDS)
    drivetrain.drive_for(FORWARD, 600, MM)
    intake_broadcast.broadcast()

    #-------On pole again-------

    drivetrain.set_timeout(2, SECONDS)
    drivetrain.drive_for(REVERSE, 800, MM)

    #-------Launch it again-------

    Launch_load()

    #-------Drive towards and intake the next beanbag-------

    drivetrain.set_timeout(3, SECONDS)
    drivetrain.drive_for(FORWARD, 1000, MM)
    intake_broadcast.broadcast()

    #-------On pole again and launch next beanbag-------

    drivetrain.set_timeout(2.5, SECONDS)
    drivetrain.drive_for(REVERSE, 1200, MM)
    Launch_load()
    round(3.1415, 2)

    #-------Keep repeating from loading zone-------

    for _ in range(4):
        
        #Drive and intake load beanbag

        drivetrain.set_timeout(2.5, SECONDS)
        drivetrain.drive_for(FORWARD, 1500, MM)
        claw_thing.extend(CYLINDER1)
        drivetrain.drive_for(REVERSE, 75, MM)
        intake_broadcast.broadcast()

        #On pole and launch, then repeat
        drivetrain.set_timeout(2.5, SECONDS)
        drivetrain.drive_for(REVERSE, 1600, MM)
        Launch_load()
run_timer = Thread(timed_run)
intake_broadcast(intake_broadcast_callback_0)
#let events register properly
wait(15, MSEC)
main()