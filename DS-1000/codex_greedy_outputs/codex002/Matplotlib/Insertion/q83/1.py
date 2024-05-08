plt.figure(figsize=(10, 8))

for i, col in enumerate(df.columns):
    plt.subplot(2, 2, i + 1)
    plt.plot(df.index, df[col], marker="o")
    plt.title(col)
    plt.xlabel("Date")
    plt.ylabel("Value")

plt.tight_layout()
plt.show()
