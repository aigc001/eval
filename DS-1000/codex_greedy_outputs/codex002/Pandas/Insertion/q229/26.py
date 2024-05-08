
groups = df.groupby(['username', pd.cut(df.views, bins)])
counts = groups.size().unstack(fill_value=0)
