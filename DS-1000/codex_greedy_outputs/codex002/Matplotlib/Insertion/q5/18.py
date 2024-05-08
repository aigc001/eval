plt.figure(figsize=(10, 6))
for i, ls in enumerate(["-", "--", "-.", ":"], 1):
    plt.plot(x, np.random.randn(10) + i, label=f"Line {i} - Style: {ls}", linestyle=ls)

plt.title("Line Styles")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
