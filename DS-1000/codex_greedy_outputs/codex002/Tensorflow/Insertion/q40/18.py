
#Training the model
history = model.fit(x=Xtrain,y=ytrain,validation_data=(Xtest,ytest),batch_size=32,epochs=epochs)

#Save the model in "export/1"
tf.keras.models.save_model(model, "export/1")
