fig, axs = plt.subplots(2, 1, sharey=False)

sns.regplot(x="bill_length_mm", y="bill_depth_mm", data=df, ax=axs[0])
sns.regplot(x="bill_length_mm", y="flipper_length_mm", data=df, ax=axs[1])

plt.show()
