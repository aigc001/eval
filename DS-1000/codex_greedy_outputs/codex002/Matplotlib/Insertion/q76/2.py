plt.figure()
for i, col in enumerate(x.T):
    plt.plot(col, label=["a", "b"][i])
plt.legend()
