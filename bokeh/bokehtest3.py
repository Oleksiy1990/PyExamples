### Example from the Quickstart tutorial

import numpy as np

from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show

# prepare some data
N = 100
x = np.linspace(0, 4*np.pi, N)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.sin(x) + np.cos(x)

# output to static HTML file
output_file("linked_panning.html",mode="inline")

# create a new plot
s1 = figure(width=250, plot_height=250, title=None,webgl=True)
s1.line(x, y0, color="navy")

# NEW: create a new plot and share both ranges
s2 = figure(width=250, height=250, x_range=s1.x_range, y_range=s1.y_range, title=None)
s2.triangle(x, y1, size=10, color="firebrick", alpha=0.5)

# NEW: create a new plot and share only one range
s3 = figure(width=250, height=250, x_range=s1.x_range, title=None)
s3.square(x, y2, size=10, color="olive", alpha=0.5)

# NEW: put the subplots in a gridplot
p = gridplot([[s1, s2, s3]], toolbar_location=None)

# show the results
show(p)


### Example from the high-level charts tutorial 

from bokeh.charts import Scatter, output_file, show
from bokeh.sampledata.autompg import autompg as df

print(df)

p = Scatter(df, x='mpg', y='weight', title="HP vs weight", color="navy",
            xlabel="Miles Per Gallon", ylabel="weight")

output_file("scatter.html")

show(p)

