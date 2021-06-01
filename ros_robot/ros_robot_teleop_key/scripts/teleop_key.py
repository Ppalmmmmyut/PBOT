#!/usr/bin/env python

from __future__ import print_function
import threading
import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

msg = """
Control 
---------------------------
Moving around:
        8    
   4    5    6
        2

8/2 : forward/backward
4/6 : left/right
5 : force stop
Anykey to quit
"""



# -------------- Function_Teleop_key -------------------------
def teleop_key():
    
    rospy.init_node('ros_robot_teleop_key') #การกำหนก node ที่ใช้ในการส่งค่าในการความคุม
    
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    #pubr = rospy.Publisher('/my_robot/right_wheel_velocity_controller/command', Twist, queue_size=10)
    rate = rospy.Rate(10) #การกำหนดความถี่ในการส่ง 
    robotVel = Twist()
    velocity = 0.1 #การกำหนดความเร็วเริ่มต้นในการส่ง

    while(1):
        vel = input("Command : ")
        if vel == 8:
            robotVel.linear.x = velocity #การกำหนดความเร็วเชิงเส้นในแกน X
            print("Moving forward")

        elif vel == 2:
            robotVel.linear.x = -velocity
            print("Moving backward")

        elif vel == 4:
            robotVel.angular.z = velocity #การกำหนดความเร็วเชิงมุมในแกน Z
            print("Turn left")

        elif vel == 6:
            robotVel.angular.z = -velocity
            print("Turn right")

        elif vel == 5:
            robotVel.linear.x = 0.0
            robotVel.angular.z = 0.0
            print("STOP")

        else:
            robotVel.linear.x = 0.0
            robotVel.angular.z = 0.0
            pub.publish(robotVel)
            #pubr.publish(twist)
            print(" Quit ")
            break
        
        
        pub.publish(robotVel) #`คำสั่งในการส่งค่า`
        #pubr.publish(twist)
        rate.sleep()


if __name__=="__main__":
    try:
        print(msg)
        teleop_key()
    except rospy.ROSInterruptException:
        pass