import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

counter = 0

def update_title(axes,x,counter):
    counter = counter + 1
    axes.plot(x+counter,np.sin(x+counter))
    axes.figure.canvas.draw()

fig, ax = plt.subplots()

x = np.linspace(-3, 3)
ax.plot(x, np.sin(x))

# Create a new timer object. Set the interval to 100 milliseconds
# (1000 is default) and tell the timer what function should be called.
timer = fig.canvas.new_timer(interval=500)
timer.add_callback(update_title, ax,x,counter)
timer.start()

# Or could start the timer on first figure draw
#def start_timer(evt):
#    timer.start()
#    fig.canvas.mpl_disconnect(drawid)
#drawid = fig.canvas.mpl_connect('draw_event', start_timer)

plt.show()