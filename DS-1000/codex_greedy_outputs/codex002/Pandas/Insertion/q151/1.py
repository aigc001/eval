
def get_relationship(df):
    relationships = []
    for i, column1 in enumerate(df.columns):
        for j, column2 in enumerate(df.columns):
            if i != j:
                relationship = get_relationship_between_columns(df[column1], df[column2])
                relationships.append(f'{column1} {column2} {relationship}')
    return relationships


def get_relationship_between_columns(column1, column2):
    if len(column1) != len(column2):
        raise ValueError('Columns must have the same length')

    unique_values_column1 = set(column1)
    unique_values_column2 = set(column2)

    if len(unique_values_column1) == 1 and len(unique_values_column2) == 1:
        return 'one-to-one'
    elif len(unique_values_column1) == 1:
        return 'one-to-many'
    elif len(unique_values_column2) == 1:
        return 'many-to-one'
    else:
        return 'many-to-many'


relationships = get_relationship(df)
for relationship in relationships:
    print(relationship)
