
uniform_data = np.random.uniform(0, T, len(times))
ks_result = stats.kstest(times, 'uniform', args=(0, T))
