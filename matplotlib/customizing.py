import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,10)

plt.figure(figsize=(9,5))

plt.plot(x,x,"b-",label="Solid Line",linewidth=1.5)

plt.plot(x,x+1,"r--",label="Dashed Line",linewidth=1.5)

plt.plot(x,x+2,"g-.",label="Dash-dot Line",linewidth=1.5)

plt.plot(x,x+3,"m:",label="Doted Line",linewidth=2)

plt.plot(x,x+4,"co-",label="Circles",markersize=5,linewidth=1)

plt.plot(x,x+5,"rs-",label="Squares",markersize=5,linewidth=1)

plt.plot(x,x+6,"^-",label="Trangles",markersize=5,linewidth=1)

plt.legend()

plt.xlabel("X Axis")

plt.ylabel("Y Axis")

plt.grid(True)

plt.show()

# Common format string: '[color][marker][line]'
# Colors: b (blue), r (red), g (green), c (cyan), m (magenta), y (yellow), k (black)
# Markers: o (circle), s (square), ^ (triangle), * (star), + (plus), x (x)
# Lines: - (solid), -- (dashed), -. (dash-dot), : (dotted)