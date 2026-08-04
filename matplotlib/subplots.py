import matplotlib.pyplot as plt

# Dataset 1 - Bell Shape
data1 = [
42, 45, 48, 50, 52,
54, 55, 56, 57, 58,
59, 60, 60, 61, 62,
62, 63, 64, 64, 65,
65, 66, 66, 67, 67,
68, 68, 69, 69, 70,
70, 71, 72, 72, 73,
74, 75, 76, 78, 80,
82, 85, 88, 90, 92
]

# Dataset 2 - Right Skewed
data2 = [
5, 6, 7, 8, 8, 9, 9,
10, 10, 11, 11, 12, 12,
13, 13, 14, 14, 15, 15,
16, 17, 18, 20, 22, 25,
30, 35, 40, 50, 60, 75, 90
]

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# First Histogram
ax[0].hist(data1, bins=10, color="skyblue", edgecolor="black")
ax[0].set_title("Bell Shape")
ax[0].set_xlabel("Marks")
ax[0].set_ylabel("Frequency")
ax[0].grid(alpha=0.3)

# Second Histogram
ax[1].hist(data2, bins=10, color="orange", edgecolor="black")
ax[1].set_title("Right Skewed")
ax[1].set_xlabel("Values")
ax[1].set_ylabel("Frequency")
ax[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()