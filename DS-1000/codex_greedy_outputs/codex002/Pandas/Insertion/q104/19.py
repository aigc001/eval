
# replace &AMP; with '&' in all columns
df = df.replace('&AMP;', '&', regex=True)

# evaluate expression in column Title
df['Title'] = df['Title'].str.replace('(\d) & (\d)', lambda m: str(int(m.group(1)) & int(m.group(2))), regex=True)
