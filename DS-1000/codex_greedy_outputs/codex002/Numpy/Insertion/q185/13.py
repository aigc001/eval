
df = pd.DataFrame(data)
df[name] = df.groupby('D').Q.apply(np.cumsum)
