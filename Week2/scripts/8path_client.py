#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
from week2.srv import angularvelocity
from nav_msgs.msg import Odometry
from math import *
"""Note: Incomplete as of now"""
class TurtleBot:

    def __init__(self):
        
        rospy.init_node('8path_client')
        rospy.wait_for_service('compute_ang_vel')

        self.findang = rospy.ServiceProxy('compute_ang_vel',angularvelocity)
        self.velocity_publisher = rospy.Publisher('/cmd_vel',Twist, queue_size=1)

        self.pose_subscriber = rospy.Subscriber('/odom',Odometry, self.update_pose)
        
        self.pos = Odometry()
        self.rate = rospy.Rate(1)
    
    def update_pose(self, msg):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.pos = msg
        self.x = round(self.pos.pose.pose.position.x, 4)
        self.y = round(self.pos.pose.pose.position.y, 4)

    def rotate(self):
        
        # Please, insert a number slightly greater than 0 (e.g. 0.01).
        distance_tolerance = input("Set your tolerance: ")

        vel_msg = Twist()

        
        radius = 1
        recieved = self.findang(radius)

        angvel = recieved.ang_vel
        linvel = 0.1

        pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
        rate = rospy.Rate(1)

        move = Twist()
        #sub = rospy.Subscriber('/odom',Odometry,initial)
        while not rospy.is_shutdown():
            # Linear velocity in the x-axis.
            move.linear.x = linvel
            move.linear.y = 0
            move.linear.z = 0

            # Angular velocity in the z-axis.
            move.angular.x = 0
            move.angular.y = 0
            move.angular.z = angvel

            # Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)

            # Publish at the desired rate.
            self.rate.sleep()

        # Stopping our robot after the movement is over.
        move.linear.x = 0
        move.angular.z = 0
        self.velocity_publisher.publish(move)

        # If we press control + C, the node will stop.
        rospy.spin()

if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.rotate()
    except rospy.ROSInterruptException:
        pass