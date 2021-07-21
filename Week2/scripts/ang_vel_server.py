#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import Float32
from week2.srv import angularvelocity, angularvelocityResponse

linvel = 0.1
angvel = None

def angular(req):
    angvel = linvel/float(req.radius)
    return angularvelocityResponse(ang_vel = (angvel))


rospy.init_node('ang_vel')
#sub = rospy.Subscriber('/radius',Float32,angular)
service = rospy.Service('compute_ang_vel', angularvelocity,angular)
rospy.spin()