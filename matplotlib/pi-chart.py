import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C++", "JavaScript", "SQL"]

students = [40, 25, 15, 10, 10]

colors = ["gold", "skyblue", "lightgreen", "orange", "pink"]

plt.pie(
    students,
    labels=subjects,
    colors=colors
)

plt.title("Students Learning Programming Languages")

plt.show()