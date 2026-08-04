import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

product_a = [120, 135, 150, 170, 180, 200]

product_b = [100, 110, 140, 160, 175, 190]

product_c = [90, 120, 130, 155, 170, 210]

x = np.arange(len(months))
width=0.25

plt.bar(x-width,product_a,width,label='Product A',color='#FF6B6B')

plt.bar(x,product_b,width,label="Product B",color="#4ECDC4")

plt.bar(x+width,product_c,width,label="Product C",color="#95E1D3")

plt.xlabel("months")

plt.ylabel("products")

plt.title("Product Data")

plt.xticks(x,months)

plt.legend()

plt.grid(True,alpha=0.3)

plt.show()