import matplotlib.pyplot as plt

data1 = [
    42, 45, 48, 50, 52,
    55, 56, 57, 58, 59,
    60, 60, 61, 62, 62,
    63, 64, 64, 65, 65,
    66, 66, 67, 67, 68,
    68, 69, 69, 70, 70,
    71, 72, 72, 73, 74,
    75, 76, 77, 78, 80,
    82, 85, 88, 90, 92
]

data2 = [
5, 6, 7, 8, 8, 9, 9,
10, 10, 11, 11, 12, 12,
13, 13, 14, 14, 15, 15,
16, 17, 18, 20, 22, 25,
30, 35, 40, 50, 60, 75, 90
]

plt.hist(data1, bins=15, color="skyblue", edgecolor="black",alpha=0.6)
plt.hist(data2, bins=15, color="orange", edgecolor="black",alpha=0.8)
plt.xlabel("Frequency")
plt.ylabel("Value")
plt.title("Over lapping histogram")
plt.show()