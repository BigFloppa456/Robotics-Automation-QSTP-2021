#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('hello_node')

pub = rospy.Publisher('/hello', String)
rate = rospy.Rate(1)



while not rospy.is_shutdown():
    pub.publish('Hello')
    rate.sleep()