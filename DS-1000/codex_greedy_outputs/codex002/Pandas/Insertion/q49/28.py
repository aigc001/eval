
df_filtered = df[(df.value < section_left) | (df.value > section_right)]
average = df_filtered.value.mean()
df_filtered = df_filtered.mean(axis=0)
df_filtered.index = ['X']
df = df[(df.value >= section_left) & (df.value <= section_right)].append(df_filtered)
