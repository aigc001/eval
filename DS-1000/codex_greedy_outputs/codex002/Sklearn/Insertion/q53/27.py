
from sklearn.svm import SVR
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Create a polynomial features object
poly_features = PolynomialFeatures(degree=2)

# Create a Support Vector Regression object
svr = SVR()

# Create a pipeline that first creates polynomial features and then fits the SVR
model = make_pipeline(poly_features, svr)

# Fit the model to the data
model.fit(X, y)

# Predict the labels of the data
predictions = model.predict(X)
