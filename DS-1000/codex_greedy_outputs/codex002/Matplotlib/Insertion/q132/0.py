plt.hist(x, bins=5, range=(0, 10), edgecolor='black')
plt.xticks(np.arange(0, 11, 2))
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.title('Histogram of x')
plt.show()
