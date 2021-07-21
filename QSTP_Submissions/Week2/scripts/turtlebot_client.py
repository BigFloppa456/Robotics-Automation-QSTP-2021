#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
from week2.srv import angularvelocity
from nav_msgs.msg import Odometry
"""For Task 3.3, Publishing to /cmd_vel after subscribing to ang_vel_server"""


rospy.init_node('turtle_client')
rospy.wait_for_service('compute_ang_vel')

findang = rospy.ServiceProxy('compute_ang_vel',angularvelocity)

def callback(msg):
    radius = msg.data
    recieved = findang(radius)

    angvel = recieved.ang_vel
    linvel = 0.1

    pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
    rate = rospy.Rate(1)

    move = Twist()
    
    while not rospy.is_shutdown():
    
        move.linear.x = linvel
        move.angular.z = angvel

        pub.publish(move)
        rate.sleep()

sub1 = rospy.Subscriber('/radius',Float32,callback) 
rospy.spin()