
images = Variable(torch.randn(5, 3, 4, 4))
labels = Variable(torch.LongTensor(5, 4, 4).random_(3))

def cross_entropy2d(input, target, weight=None, size_average=True):
    n, c, h, w = input.size()
    log_p = F.log_softmax(input, dim=1)
    log_p = log_p.permute(0, 3, 2, 1).contiguous().view(-1, c)
    log_p = log_p[
        target.view(n, h, w, 1).repeat(1, 1, 1, c) >= 0]
    log_p = log_p.view(-1, c)

    mask = target >= 0
    target = target[mask]
    loss = F.nll_loss(log_p, target.view(-1), weight=weight, size_average=False)
    if size_average:
        loss /= mask.data.sum()
    return loss

print(cross_entropy2d(images, labels))
