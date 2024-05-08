plt.scatter(b, a)

for i, (x, y) in enumerate(zip(b, a)):
    plt.text(x, y, c[i], fontsize=10, ha='center')

plt.xlabel('b')
plt.ylabel('a')
plt.title('Scatter plot of a over b')
plt.show()
