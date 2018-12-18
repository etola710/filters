import numpy as np
import matplotlib.pyplot as plt
import pdb

dt = 0.5
xk_1 = 0
vk_1 = 0
ak_1 = 0

a = 0.1
b = 0.1
g = 0.001

iteration = 0

fig = plt.figure()
fig.show()
fig.canvas.show
plt.axis([0, 200, 0, 1.5])

while True:
    xm = np.random.rand(1)

    xk = xk_1 + (vk_1 * dt)
    vk = vk_1 + (ak_1 * dt)
    ak = (vk - vk_1) /dt

    rk = xm - xk

    xk += a*rk
    vk += (b*rk)/dt
    ak += (2*g*rk)/np.power(dt,2)

    xk_1 = xk
    vk_1 = vk
    ak_1 = ak

    print("xk = " ,xk, "vk = " ,vk, "ak = ",ak)
    iteration += 1
    #plt.axis([0, 20+iteration, 0, 1.5])
    plt.plot(iteration,xm,'k+')
    plt.plot(iteration,xk,'b*')
    plt.pause(0.05)
    plt.draw()