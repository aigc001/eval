
models = [model]

# Create a list to store the model names
model_names = []

for model in models:
   model_names.append(type(model).__name__)
   scores = cross_val_score(model, X, y, cv=5)
   print(f'Name model: {type(model).__name__} , Mean score: {scores.mean()}')

# Create a DataFrame to store the model names and their corresponding scores
df = pd.DataFrame({'Model Name': model_names, 'Mean Score': scores.mean()})
