plt.pie(sizes, labels=labels, colors=colors,
         autopct='%1.1f%%', startangle=140, shadow=True)

plt.title('Pie Chart')

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.tight_layout()

plt.show()
