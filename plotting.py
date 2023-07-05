from Capture import df
from bokeh import plotting
from bokeh.io import figure, show, output_file

p=figure(x_axis_type='datetime', height=100, width=500, responsive=True, title="Motion Graphy")

q=p.quad(left=df['Start'], right=df['End'], bottom=0, top=1, color='green')

output_file("Graph.html")
show(p)