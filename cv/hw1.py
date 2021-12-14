import numpy as np
from matplotlib import pyplot as plt

# skid steer model of a robot that is 50cm long and 30cm

# 1. (10 pts) plot the following commanded path in global (x,y) space:
# Duration of command	Left Wheel Velocity	Right Wheel Velocity
# 5s	                1m/s	            1.5m/s
# 3s	                -1m/s	            -1.5m/s
# 8s	                0.8m/s	            -2m/s
# 10s	                2m/s	            2m/s


def move(time, x_pos, v_r, y_pos, v_l, theta):
    dt = .1
    width = .3
    thetaVel = (v_r - v_l)/width
    for _ in range(0, time*10):
        theta.append(theta[-1] + (thetaVel * dt))
        x_pos.append(x_pos[-1] + (-(v_r + v_l) / 2.0) * np.sin(theta[-1]) * dt)
        y_pos.append(y_pos[-1] + ((v_r + v_l) / 2.0) * np.cos(theta[-1]) * dt)


# width = .3
# length = .5
x_pos = [0.0]
y_pos = [0.0]
theta = [0.0]

move(5, x_pos, 1.5, y_pos, 1.0, theta)
plt.plot(x_pos, y_pos, '.', c='red')
plt.show()
move(3, x_pos, -1.5, y_pos, -1.0, theta)
plt.plot(x_pos, y_pos, '.', c='red')
plt.show()
move(8, x_pos, -2.0, y_pos, .8, theta)
plt.plot(x_pos, y_pos, '.', c='red')
plt.show()
move(10, x_pos, 2.0, y_pos, 2.0, theta)
plt.plot(x_pos, y_pos, '.', c='red')
plt.show()
# 2. (10 pts) Make a list of commands that will allow this robot to cover a space of 5m x 5m. Plot the resulting path (x, y) and trajectory (x, y, and angular velocities).
# 3. (10 pts) Do the same as the above but assume that you have swedish wheels. What has changed? What are the problems we can expect to see if we try to implement your commands on either skid-steered or swedish wheel systems?
# Xt = Xt-1 + Vx dt
# you can just say turn 90, set phi to 90
# change of x / change in time
# talk about software vs hardware
robby
