
# Replace &AMP; with &
df.replace('&AMP;', '&', regex=True, inplace=True)

# Replace &LT; with <
df.replace('&LT;', '<', regex=True, inplace=True)

# Replace &GT; with >
df.replace('&GT;', '>', regex=True, inplace=True)
