import matplotlib.pyplot as plt

labels = ["Jabłka", "Banany", "Winogrona", "Pomarańcze"]
sizes = [30, 25, 20, 45]
colors = ['red', 'blue', 'green', 'yellow']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
        startangle=90,
        shadow=True)

plt.title("Wykres kołowy")
plt.axis('equal')

plt.show()
