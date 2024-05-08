
# Reverse the DataFrame and concatenate the 'text' column with '-' as the separator
result = df[::-1]['text'].str.cat(sep='-')
