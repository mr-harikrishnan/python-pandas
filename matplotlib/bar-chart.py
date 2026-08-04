import matplotlib.pyplot as plt


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [1200, 1500, 1800, 1700, 2100, 2500]

plt.bar(months,sales,color="red",edgecolor="black",linewidth=1.2,alpha=0.6)
plt.xlabel("months")
plt.ylabel("sales")
plt.title("Bar chart")
plt.show()