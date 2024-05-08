# Create a second lineplot with the same x values but different y values
y2 = 4 * np.random.rand(10)
sns.lineplot(x=x, y=y2, dashes=True, ax=ax)
