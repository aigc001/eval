
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.externals import joblib

# Load your data
data = pd.read_csv('your_data.csv')

# Preprocess your data
# Here we use StandardScaler to standardize the features
# You can replace it with your own preprocessing steps
preprocessor = StandardScaler()
data = preprocessor.fit_transform(data)

# Create an Isolation Forest model
model = IsolationForest(contamination=0.1)

# Create a pipeline that first preprocesses the data and then applies the model
pipeline = make_pipeline(preprocessor, model)

# Fit the model
pipeline.fit(data)

# Save the model to a file
joblib.dump(pipeline, 'sklearn_model')
