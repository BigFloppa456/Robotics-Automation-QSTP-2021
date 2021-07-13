"""Week I Assignment
Simulate the trajectory of a robot approximated using a unicycle model given the
following start states, dt, velocity commands and timesteps
State = (x, y, theta);
Velocity = (v, w) 
1. Start=(0, 0, 0); dt=0.1; vel=(1, 0.5); timesteps: 25
2. Start=(0, 0, 1.57); dt=0.2; vel=(0.5, 1); timesteps: 10
3. Start(0, 0, 0.77); dt=0.05; vel=(5, 4); timestep: 50

Upload the completed python file and the figures of the three sub parts in classroom
"""
import numpy as np
import matplotlib.pyplot as plt

class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt

        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v: float, w: float, n: int):
        """
        Write the Kinematics model here
        Expectation:
            1. Given v, w and the current state self.x, self.y, self.theta
                and control commands (v, w) for n timesteps, i.e. n * dt seconds,
                return the final pose (x, y, theta) after this time.
            2. Append all intermediate points into the self.x_points, self.y_points list
                for plotting the trajectory.

        Args:
            v (float): linear velocity
            w (float): angular velocity
            n (int)  : timesteps

        Return:
            x, y, theta (float): final pose 
        """
        x = self.x
        y = self.y
        
        #Assumptions : Velocity and Angular Velocity remain constant
        
        theta = self.theta 
        dt = self.dt

        self.w = w
        self.n = n

        total_time = n*dt

        
        #Angular velocity of unicycle (w) = (theta dot)

        t1 = 0
        t2 = dt

        for i in range(n):
            vx = v*(np.cos(theta))
            vy = v*(np.sin(theta))

            ax = -v*w*(np.sin(theta))
            ay = v*w*(np.cos(theta))


            x += vx*(t2-t1) + 0.5 * ax * ((t2-t1)**2)
            #y += vy*(t2-t1) + 0.5 * (ay) * ((t2-t1)**2)       #Uncomment this line if gravity doesnt act upon the system
            y += vy*(t2-t1) + 0.5 * (ay-9.81) * ((t2-t1)**2)   #comment this line if gravity doesnt act upon system
            

            self.x_points.append(x)
            self.y_points.append(y)

            t1 += dt    
            t2 += dt
            theta += w*(t2-t1)  #Angular velocity of unicycle (w) = (theta dot)


        return x, y, theta

    def plot(self, v: float, w: float):
        """Function that plots the intermeditate trajectory of the Robot"""
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()

        # If you want to view the plot uncomment plt.show() and comment out plt.savefig()
        #plt.show()
        # If you want to save the file, uncomment plt.savefig() and comment out plt.show()
        plt.savefig(f"Unicycle_{v}_{w}.png")



if __name__ == "__main__":
    print("Unicycle Model Assignment")

    # make an object of the robot and plot various trajectories
    rob1 = Unicycle(0,0,0,0.1)
    rob2 = Unicycle(0,0,1.57,0.2) 
    rob3 = Unicycle(0,0,0.77,0.05)

    #Uncomment below lines as per requirements
    x1,y1,theta1=rob1.step(1,0.5,25)

    print("final x1 = "+str(x1))
    print("final y1 = "+str(y1))
    print("final theta1 = "+str(theta1))
    rob1.plot(1,0.5)
    print('')

    """
    x2,y2,theta2=rob2.step(0.5,1,10)
    print("final x2 = "+str(x2))
    print("final y2 = "+str(y2))
    print("final theta2 = "+str(theta2))
    rob2.plot(0.5,1)
    print('')

    x3,y3,theta3=rob3.step(5,4,50)
    print("final x3 = "+str(x3))
    print("final y3 = "+str(y3))
    print("final theta3 = "+str(theta3))
    rob3.plot(5,4)"""
