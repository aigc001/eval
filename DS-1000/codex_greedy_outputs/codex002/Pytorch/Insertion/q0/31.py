
# To change the learning rate during training, you can access the 'param_groups' attribute of the optimizer object and change the 'lr' value.
# Here's how you can do it:

for param_group in optim.param_groups:
    param_group['lr'] = 0.001
