#!/usr/bin/env python
import rospy
import numpy as np
import sys
import matplotlib.pyplot as plt
from week2.srv import trajectory

rospy.init_node('client')
rospy.wait_for_service('path')

path_func = rospy.ServiceProxy('path',trajectory)

x = float(sys.argv[1])
y = float(sys.argv[2])
theta = float(sys.argv[3])
v = float(sys.argv[4])
w = float(sys.argv[5])

path = path_func(x,y,theta,v,w)

path_x = path.path_x
path_y = path.path_y

print ("X: ", path_x)
print ("Y: ", path_y)

plt.plot(path_x,path_y)
plt.xlabel("X-Coordinates")
plt.ylabel("Y-Coordinates")
plt.grid()
plt.show()

