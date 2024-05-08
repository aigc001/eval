
# For Qu1, replace values that occur less than 3 times with 'other'
df['Qu1'] = df['Qu1'].apply(lambda x: 'other' if df['Qu1'].value_counts()[x] < 3 else x)

# For Qu1, replace 'egg' with 'other'
df['Qu1'] = df['Qu1'].replace('egg', 'other')

# For Qu2 and Qu3, replace values that occur less than 2 times with 'other'
for col in ['Qu2', 'Qu3']:
    df[col] = df[col].apply(lambda x: 'other' if df[col].value_counts()[x] < 2 else x)
