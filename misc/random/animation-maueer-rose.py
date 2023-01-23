import sys
from functools import partial
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
# from maurerrose import get_rose_xy

def get_rose_xy(n, d):
    """Get the Cartesian coordinates for points on the rose."""

    # The rose is (r = sin(nk), k) in polar coordinates, for
    # k = d, 2d, 3d, ..., 360d.
    # Add a final point at 361d to close the curve when plotted.
    k = d * np.linspace(0, 361, 361)
    r = np.sin(np.radians(n * k))
    x = r * np.cos(np.radians(k))
    y = r * np.sin(np.radians(k))
    return x, y


"""Animate a Maurer rose with a given n for increasing d."""

# Colours will change according to this colormap as d advances.
cmap = plt.get_cmap('hsv')

# Read n from the command line, initialize d to 1.
# n, d = int(sys.argv[1]), 1
n, d = 5, 1

# New Figure with a single Axes and a black background.
fig, ax = plt.subplots(facecolor='k')

# Initial plot.
x, y = get_rose_xy(n, d)
line, = ax.plot(x, y, c='r', lw=0.5)
# Annotate with the values of n and d.
ax.text(0.8, 0.9, f'n = {n}', ha='left', c='w')
text = ax.text(0.8, 0.8, f'd = {d}', ha='left', c='w')
# Make the Axes square and turn off tick marks, labels and spines.
ax.axis('equal')
ax.axis('off')

def init_animation():
    """Initialize animation: line and text are handed around at each frame."""
    return line, text

def animate(i):
    """Advance the animation by one frame, increasing d by 1."""

    global d
    d += 1
    x, y = get_rose_xy(n, d)
    line.set_data(x, y)
    # Also advance the colour, mapping i to [0,1]:
    c = cmap(i / 360)
    line.set_color(c)
    # Update the text label indicating the value of d.
    text.set_text(f'd = {d}')
    return line, text

frames = 360
interval = 50
#
anim = animation.FuncAnimation(fig, animate,
                               init_func=init_animation, frames=frames,
                               interval=interval)

# If we're saving the animation as a video, uncomment these two lines.
# writer = animation.FFMpegWriter(fps=20)
# anim.save('maurer-rose.mp4', writer=writer)

# If we're just viewing the animation locally, uncomment this line.
plt.show()