g = sns.FacetGrid(df, col="species", hue="sex", margin_titles=True, sharey=False)
g.map(sns.barplot, "sex", "bill_length_mm")
plt.show()
