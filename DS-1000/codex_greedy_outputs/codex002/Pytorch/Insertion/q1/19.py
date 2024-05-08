
# Assuming that you have a model and an optimizer
model = MyModel()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Now, let's say you want to change the learning rate to 0.001
for param_group in optimizer.param_groups:
    param_group['lr'] = 0.001
