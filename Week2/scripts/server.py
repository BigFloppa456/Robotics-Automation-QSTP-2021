#!/usr/bin/env python
import rospy
import numpy as np
from week2.srv import trajectory,trajectoryResponse
dt = 0.05
n = 50
x_pts = []
y_pts = []
def path(request):
    x=request.x
    y=request.y
    theta=request.theta
    w = request.w
    v =request.v

    x_pts.append(x)
    y_pts.append(y)

    t1 = 0
    t2 = dt

    for i in range(n):
        vx = v*(np.cos(theta))
        vy = v*(np.sin(theta))

        ax = -v*w*(np.sin(theta))
        ay = v*w*(np.cos(theta))

        x += vx*(t2-t1) + 0.5 * ax * ((t2-t1)**2)
        y += vy*(t2-t1) + 0.5 * (ay-9.81) * ((t2-t1)**2)

        x_pts.append(x)
        y_pts.append(y)

        t1 += dt
        t2 += dt
        theta += w*(t2-t1)
    
    return trajectoryResponse(path_x = (x_pts),path_y = (y_pts))




rospy.init_node('server')
service = rospy.Service('path', trajectory, path)
rospy.spin()