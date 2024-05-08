sns.catplot(x="time", y="pulse", hue="kind", col="diet", data=df, kind="scatter", xlabels="Exercise Time", ylabels="Pulse")
plt.show()
