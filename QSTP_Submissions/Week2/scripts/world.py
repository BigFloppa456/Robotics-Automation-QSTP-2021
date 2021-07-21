#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('world_node')

pub = rospy.Publisher('/world', String)
rate = rospy.Rate(1)



while not rospy.is_shutdown():
    pub.publish('World')
    rate.sleep()