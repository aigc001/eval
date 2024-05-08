
# Melt the dataframe
melted_df = pd.melt(df, id_vars=['user', 'someBool'], var_name='date')

# Create a new dataframe with the desired format
final_df = pd.DataFrame({'user': melted_df['user'],
                         'date': melted_df['date'],
                         'value': melted_df['value'],
                         'someBool': melted_df['someBool']})
