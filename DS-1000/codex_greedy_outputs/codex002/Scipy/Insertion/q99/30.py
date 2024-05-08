
df['Time'] = pd.to_datetime(df['Time'])
df.set_index('Time', inplace=True)

def rolling_integral(df):
    return integrate.trapz(df['A'], x=df.index.astype(np.int64) // 10**9)

df['Integral'] = df.rolling('25S').apply(rolling_integral)
