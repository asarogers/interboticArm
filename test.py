
import math

from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
from interbotix_common_modules.common_robot.robot import robot_shutdown, robot_startup

# Initialize the robot object
robot = InterbotixManipulatorXS("px100", "arm", "gripper")

# Start the robot
robot_startup()

def grab():
    robot.gripper.grasp()

def release():
    robot.gripper.release()

def moveToSleepPose():
    robot.arm.go_to_sleep_pose()

def moveToHomePose():
    robot.arm.go_to_home_pose()


def rotateRobot():
    name = "waist"
    position = math.radians(int(input("how many degrees?\n")))
    move_time = 4
    accel_time = 0.5
    block = True
    robot.arm.set_single_joint_position(name, position, move_time, accel_time, False)

def moveShoulder():
    name = "shoulder"
    position = math.radians(int(input("how many degrees?\n")))
    move_time = 4
    accel_time = 0.5
    block = True
    robot.arm.set_single_joint_position(name, position, move_time, accel_time, False)

def moveElbow():
    name = "elbow"
    position = math.radians(int(input("how many degrees?\n")))
    move_time = 4
    accel_time = 0.5
    block = True
    robot.arm.set_single_joint_position(name, position, move_time, accel_time, False)
# Initialize mode for the loop
mode = ''
def moveWrist():
    name = "wrist_angle"
    position = math.radians(int(input("how many degrees?\n")))
    move_time = 4
    accel_time = 0.5
    block = True
    robot.arm.set_single_joint_position(name, position, move_time, accel_time, False)

# User control loop
while mode != 'q':
    mode = input("[h]ome, [s]leep, [q]uit, [g]rasp, [r]elease, [rr] rotate robot, [t]est [ms] move shoulder [me] move elbow\n").lower()
    
    match mode:
        case "t":
          robot.gripper.set_pressure(0.99)
        case "ms":
           moveShoulder()
        case 'h':
            moveToHomePose()
        case 'g':
            grab()
        case 'r':
            release()
        case 's':
            moveToSleepPose()
        case 'rr':
            rotateRobot()
        case 'me':
            moveElbow()
        case "mw":
            moveWrist()
            # Command the robot to twist for 2 seconds
            

# Shutdown the robot properly after exiting the loop
robot_shutdown()
