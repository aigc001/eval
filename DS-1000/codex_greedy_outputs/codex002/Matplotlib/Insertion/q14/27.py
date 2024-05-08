
# create a pandas dataframe
df = pd.DataFrame({'x': x, 'y': y})

# use seaborn to draw a line plot
sns.lineplot(data=df, x='x', y='y')

# show the plot
plt.show()

