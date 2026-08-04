import matplotlib.pyplot as plt

marks = [
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

plt.hist(marks, bins=15, color="skyblue", edgecolor="black")

plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.grid(alpha=0.3)

plt.show()