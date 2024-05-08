
def get_relationship(df):
    relationships = pd.DataFrame(index=df.columns, columns=df.columns)

    for col1 in df.columns:
        for col2 in df.columns:
            if col1 == col2:
                relationships[col1][col2] = 'one-to-one'
            else:
                relationship = 'many-to-many'
                if df[col1].nunique() == df[col1].count():
                    relationship = 'one-to-many'
                if df[col2].nunique() == df[col2].count():
                    relationship = 'many-to-one' if relationship != 'many-to-many' else relationship
                relationships[col1][col2] = relationship

    return relationships

relationships = get_relationship(df)
print(relationships)
