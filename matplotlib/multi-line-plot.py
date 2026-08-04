import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

product_a = [120, 135, 150, 170, 180, 200]

product_b = [100, 110, 140, 160, 175, 190]

product_c = [90, 120, 130, 155, 170, 210]

plt.plot(months,product_a,label="product_a")

plt.plot(months,product_b,label="product_b")

plt.plot(months,product_c,label="product_c")

plt.xlabel("months")

plt.ylabel("product")

plt.title("Multi Plot Line")

plt.legend()

plt.grid(True,alpha=0.3)

plt.show()