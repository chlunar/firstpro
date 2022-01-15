import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import *

g = 9.8
theta = np.radians(45)
l = 1
# b는 물체에 가해지는 저항력, m은 물체의 질량
b = 1
m = 3


def dU_dx(U, x):
    # v = x'  =>  x = U[0], v = U[1], function return [x', v']
    return [U[1], - b / m * U[1] - g / l * np.sin(U[0])]


U0 = [theta, 0]

xs = np.arange(0, 10, 0.05)

Us = odeint(dU_dx, U0, xs)
ys = Us[:, 0]

fig, ax = plt.subplots()
ax.set(xlim=[-l - 0.5, l + 0.5], ylim=[-l - 0.5, l + 0.5])
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle='--')

line, = ax.plot([], [], color='b', linewidth=2)
obj, = ax.plot([], [], 'bo')
time_text = ax.text(-l - 0.2, -l - 0.2, '')


def init():
    line.set_data([], [])
    return line,


def iterr(i):
    theta = ys[i]
    x = l * np.sin(theta)
    y = -l * np.cos(theta)
    line.set_data([0, x], [0, y])
    obj.set_data([x], [y])
    time_text.set_text('time = {:.1f}'.format(xs[i]))
    return line, obj, time_text


anim = animation.FuncAnimation(fig, iterr, init_func=init, frames=len(ys), interval=0.05 * 1000, blit=True)
plt.show()