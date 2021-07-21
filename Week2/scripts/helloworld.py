#!/usr/bin/env python

import rospy
from std_msgs.msg import String

x = ["h","wo"]
def hello(msg):
    x[0] = (msg.data)
def world(msg):
    x[1] = (msg.data)

rospy.init_node('helloworld_node')

pub = rospy.Publisher('/helloworld', String)
rate = rospy.Rate(1)

sub1 = rospy.Subscriber('/hello',String,hello)
sub2 = rospy.Subscriber('/world',String,world)

while not rospy.is_shutdown():
    
    prt =  str(x[0])+" "+str(x[1])
    pub.publish(prt)

    rate.sleep()

rospy.spin()
