sns.pairplot(data=df, x_vars=["x"], y_vars=["y"], hue="id", palette="deep", diag_kind="kde", markers="o", plot_kws={"s": 100}, diag_kws={"bw": 1.5}, legend=False)
