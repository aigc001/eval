sns.catplot(x="time", y="pulse", hue="kind", col="diet", data=df, kind="scatter", ylabel="")
plt.show()
