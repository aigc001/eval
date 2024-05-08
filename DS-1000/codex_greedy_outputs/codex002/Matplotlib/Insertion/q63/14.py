plt.imshow(rand_mat, cmap='hot', interpolation='nearest')
plt.xticks(range(len(xlabels)), xlabels, rotation=90)
plt.yticks(range(len(ylabels)), ylabels[::-1])
plt.show()
