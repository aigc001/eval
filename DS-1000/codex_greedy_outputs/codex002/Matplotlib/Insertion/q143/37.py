sns.catplot(x="time", y="pulse", hue="kind", col="diet", data=df, kind="scatter",
            col_order=["Fat", "NoFat"], 
            col_wrap=2,
            height=4,
            aspect=1,
            sharex=False,
            sharey=False,
            legend_out=True,
            legend_out_kws={"title": "Exercise"},
            facet_kws={"margin_titles": True,
                        "xlabel": "Time",
                        "ylabel": "Pulse",
                        "col_order": ["Fat", "NoFat"],
                        "col_wrap": 2})

plt.subplots_adjust(top=0.9)
plt.suptitle("Group: Fat", x=0.5, y=0.95)
plt.text(0.5, 0.45, "Group: No Fat", horizontalalignment='center', verticalalignment='center',
         transform=plt.gcf().transFigure)
plt.show()
