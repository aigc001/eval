
df[["exp_A", "exp_B"]] = df[["A", "B"]].apply(lambda x: np.exp(x))
