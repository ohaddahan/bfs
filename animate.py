import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

# Requires "brew install ffmpeg"
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

n_frames = 3

nodes0 = [
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
]

nodes1 = [
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0.5],
]

nodes2 = [
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0.5, 0.5],
]

data = np.empty(n_frames, dtype=object)
data[0] = nodes0
data[1] = nodes1
data[2] = nodes2

fig = plt.figure()
plot =plt.imshow(data[0])

def init():
    plot.set_data(data[0])
    return plot

def update(j):
    plot.set_data(data[j])
    return [plot]

anim = FuncAnimation(fig, update, init_func=init, frames=n_frames, interval=500, repeat=False)# blit=True)
anim.save(filename='basic_animation.mp4', writer=writer)  #, fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()
