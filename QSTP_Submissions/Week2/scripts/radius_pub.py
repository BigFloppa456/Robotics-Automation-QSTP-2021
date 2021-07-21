#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

rospy.init_node('radius_node')

pub = rospy.Publisher('/radius', Float32,queue_size=1)
rate = rospy.Rate(1)
radius = float(input("Enter radius: "))


while not rospy.is_shutdown():

    
    pub.publish(radius)
    rate.sleep()