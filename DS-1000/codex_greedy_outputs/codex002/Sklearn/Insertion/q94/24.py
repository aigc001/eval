
# ElasticNet Regression
ElasticNet = linear_model.ElasticNet() # create a lasso instance
ElasticNet.fit(X_train, y_train) # fit data

# print(lasso.coef_)
# print (lasso.intercept_) # print out the coefficients

print ("R^2 for training set:"),
print (ElasticNet.score(X_train, y_train))

print ('-'*50)

print ("R^2 for test set:"),
print (ElasticNet.score(X_test, y_test))
