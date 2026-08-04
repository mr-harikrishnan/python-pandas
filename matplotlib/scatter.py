import matplotlib.pyplot as plt
import numpy as np

x=[1,4,6,8,12,22.5]

y=[2,5,7,3,8,0]

temperature = [20, 25, 30, 35, 40, 45]

plt.scatter(x,y,c=temperature, cmap="jet",s=32,alpha=0.6)
plt.colorbar(label="Colour Intensity")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()



# cmap="viridis"
# cmap="plasma"
# cmap="inferno"
# cmap="magma"
# cmap="Set1"
# cmap="Set2"
# cmap="jet"
# cmap="cool"
# cmap="hot"
# cmap="rainbow"