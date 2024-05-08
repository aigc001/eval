g = sns.FacetGrid(df, row="b", hue="b", aspect=4)
g.map(sns.pointplot, "a", "c", linestyles="--", order=range(1, 31, 2), xticks=range(1, 31, 1))

# Set the xtick labels to be the actual values
for ax in g.axes.flatten():
    ax.set_xticklabels(ax.get_xticks())

plt.show()
