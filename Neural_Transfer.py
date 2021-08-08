from __future__ import print_function

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optm

from PIL import Image
import matplotlib.pyplot as plt

import torchvision.transforms as transforms
import torchvision.models as models

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 所需的输出图像大小
imsize = 512 if torch.cuda.is_available() else 128 # use small size if no gpu

loader = transforms.Compose([
    transforms.Resize(imsize), # scale imported image
    transforms.ToTensor()      # transform it into a torch tensor
])

def image_loader(image_name):
    image = Image.open(image_name)
    # fake batch dimension required to fit network's input dimensions
    image = loader(image).unsqueeze(0)
    return image.to(device, torch.float)

style_img = image_loader('data/images/picasso.jpg')
content_img = image_loader('data/images/dancing.jpg')

assert style_img.size() == content_img.size(), \
    'we need to import style and content images of the same size'

unloader = transforms.ToPILImage() # reconvert into PIL image

plt.ion()

def imshow(tensor, title=None):
    image = tensor.cpu().clone() # we clone the tensor to not do changes on it
    image = unloader(image)
    plt.imshow(image)
    if title is not None:
        plt.title(title)
    plt.pause(0.001) # pause a bit so that plots are updated

plt.figure()
imshow(style_img, title='Style Image')

plt.figure()
imshow(content_img, title='Content Image')



class ContentLoss(nn.Module):
    def __init__(self, target,):
        super(ContentLoss, self).__init__()
        # 我们从用于动态计算梯度的树中“分离”目标内容：
        # 这是一个声明的值，而不是变量。 
        # 否则标准的正向方法将引发错误。
        self.target = target.detach()
 
    def forward(self, input):
        self.loss = F.mse_loss(input, self.target)
        return input
