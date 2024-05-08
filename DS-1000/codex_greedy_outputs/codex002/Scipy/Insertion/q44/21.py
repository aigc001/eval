
def kendall_tau(x, y):
    return stats.kendalltau(x, y)[0]

def rolling_kendall_tau(df, window):
    df_rolling = df.rolling(window)
    df_output = pd.DataFrame(index=df.index)
    
    for col in df.columns:
        df_output[col] = df_rolling.apply(lambda x: kendall_tau(x, df[col]))
        
    return df_output

rolling_kendall_tau(df, 3)
