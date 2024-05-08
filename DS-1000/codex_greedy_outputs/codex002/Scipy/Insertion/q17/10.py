
uniform_times = np.random.uniform(0, T, len(times))
ks_result = stats.ks_2samp(times, uniform_times)
print(ks_result)
