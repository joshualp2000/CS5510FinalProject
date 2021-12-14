from controller import Robot
import time

def get_devices(robot):
    devices = {}
    device_names = ["head_2_joint",
                    "head_1_joint",
                    "torso_lift_joint",
                    "arm_1_joint",
                    "arm_2_joint",
                    "arm_3_joint",
                    "arm_4_joint",
                    "arm_5_joint",
                    "arm_6_joint",
                    "arm_7_joint",
                    "hand_right_thumb_abd_joint",
                    "hand_right_thumb_virtual_1_joint",
                    "hand_right_thumb_flex_1_joint",
                    "hand_right_thumb_virtual_2_joint",
                    "hand_right_thumb_flex_2_joint",
                    "hand_right_index_abd_joint",
                    "hand_right_index_virtual_1_joint",
                    "hand_right_index_flex_1_joint",
                    "hand_right_index_virtual_2_joint",
                    "hand_right_index_flex_2_joint",
                    "hand_right_index_virtual_3_joint",
                    "hand_right_index_flex_3_joint",
                    "hand_right_middle_abd_joint",
                    "hand_right_middle_virtual_1_joint",
                    "hand_right_middle_flex_1_joint",
                    "hand_right_middle_virtual_2_joint",
                    "hand_right_middle_flex_2_joint",
                    "hand_right_middle_virtual_3_joint",
                    "hand_right_middle_flex_3_joint",
                    "hand_right_ring_abd_joint",
                    "hand_right_ring_virtual_1_joint",
                    "hand_right_ring_flex_1_joint",
                    "hand_right_ring_virtual_2_joint",
                    "hand_right_ring_flex_2_joint",
                    "hand_right_ring_virtual_3_joint",
                    "hand_right_ring_flex_3_joint",
                    "hand_right_little_abd_joint",
                    "hand_right_little_virtual_1_joint",
                    "hand_right_little_flex_1_joint",
                    "hand_right_little_virtual_2_joint",
                    "hand_right_little_flex_2_joint",
                    "hand_right_little_virtual_3_joint",
                    "hand_right_little_flex_3_joint",
                    "wheel_left_joint",
                    "wheel_right_joint"]
                    
    for device_name in device_names:
        devices[device_name] = robot.getDevice(device_name)      
    return devices       

                
def grip(devices):
    devices["hand_right_thumb_virtual_1_joint"].setPosition(0.79)
    devices["hand_right_thumb_flex_1_joint"].setPosition(0.79)
    devices["hand_right_thumb_virtual_2_joint"].setPosition(0.79)
    devices["hand_right_thumb_flex_2_joint"].setPosition(0.79)

    devices["hand_right_index_abd_joint"].setPosition(0.52)
    devices["hand_right_index_flex_1_joint"].setPosition(0.79)
    devices["hand_right_index_flex_2_joint"].setPosition(0.79)
    devices["hand_right_index_flex_3_joint"].setPosition(0.79)

    devices["hand_right_middle_abd_joint"].setPosition(0.52)
    devices["hand_right_middle_flex_1_joint"].setPosition(0.79)
    devices["hand_right_middle_flex_2_joint"].setPosition(0.79)
    devices["hand_right_middle_flex_3_joint"].setPosition(0.79)

    devices["hand_right_ring_abd_joint"].setPosition(0.52)
    devices["hand_right_ring_flex_1_joint"].setPosition(0.79)
    devices["hand_right_ring_flex_2_joint"].setPosition(0.79)
    devices["hand_right_ring_flex_3_joint"].setPosition(0.79)

    devices["hand_right_little_abd_joint"].setPosition(0.52)
    devices["hand_right_little_flex_1_joint"].setPosition(0.79)
    devices["hand_right_little_flex_2_joint"].setPosition(0.79)
    devices["hand_right_little_flex_3_joint"].setPosition(0.79)

def pick_up(devices):
    devices["arm_4_joint"].setPosition(-5)
    devices["arm_2_joint"].setPosition(1.01)
    
def init_wheels():
    pass

robot = Robot()
timestep = int(robot.getBasicTimeStep())
devices = get_devices(robot)
wheelL = robot.getDevice('wheel_left_joint')
wheelR = robot.getDevice('wheel_right_joint')
lidar = robot.getDevice('Hokuyo URG-04LX-UG01')
wheelL.setPosition(float('inf'))
wheelR.setPosition(float('inf'))
wheelL.setVelocity(0)
wheelR.setVelocity(0)

lidar.enable(64)
lidar.enablePointCloud()
devices['arm_1_joint'].getPositionSensor().enable(64)
devices["hand_right_thumb_abd_joint"].setPosition(1.57)
c = 0
bandaid = 0

"""
1.80352
1.01
-0.223801
"""

while robot.step(timestep) != -1:
    range_image = lidar.getRangeImage()
    points = range_image
    smallest = 10000
    sIndex = 0
    print("Start", end=" -> ")
    for i in range(len(points)):
        if points[i] < smallest:
            smallest = points[i]
            sIndex = i
    print(f"smallest={smallest:.4f}, i={sIndex}", end=" -> ")

    if smallest <= 0.8:
        print("lt 0.78", end=" -> ")
        wheelL.setVelocity(0)
        wheelR.setVelocity(0)
        devices['arm_1_joint'].setPosition(1.525)
        print(f"joint pos={devices['arm_1_joint'].getPositionSensor().getValue():.4f}", end=" -> ")
        if devices['arm_1_joint'].getPositionSensor().getValue() >= 1.4:
            print("abt to grip", end=" -> ")
            bandaid += 1
            if bandaid < 20: continue
            grip(devices)
            c += 1
            print(c, end=" -> ")
            if c > 10:
                print("pick up", end=" -> ")
                pick_up(devices)
    elif smallest < 10000:
        print("movement", end=" -> ")

        if sIndex > 340:
            print("Right", end=" -> ")

            # wheelL.setPosition(1)
            wheelR.setVelocity(0)
            wheelL.setVelocity(2)
        elif sIndex < 331:
            print("Left", end=" -> ")

            # wheelR.setPosition(1)
            wheelL.setVelocity(0)
            wheelR.setVelocity(2)
        elif sIndex > 319 and sIndex < 341:
            print("Forward", end=" -> ")

            # wheelL.setVelocity(0)
            # wheelR.setVelocity(0)
            # wheelL.setPosition(1)
            # wheelR.setPosition(1)
            wheelL.setVelocity(2)
            wheelR.setVelocity(2)
    print()
print("Outside of loop")

