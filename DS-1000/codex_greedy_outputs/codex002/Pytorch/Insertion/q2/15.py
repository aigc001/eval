
# You can change the learning rate of the optimizer dynamically as follows:
for param_group in optim.param_groups:
    param_group['lr'] = 0.0005
