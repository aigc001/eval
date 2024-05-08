g = seaborn.relplot(x="Height (cm)", y="Weight (kg)", hue="Gender", data=df)
g.set_axis_labels("Height (cm)", "Weight (kg)")
g.set_titles("{col_name}")
plt.show()
