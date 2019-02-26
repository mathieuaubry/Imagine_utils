from __future__ import print_function
import torch
import torch.nn as nn
from torch.autograd import Variable

class batchRenorm(nn.Module):
   """custom batchnorm using running mean and std during training"""

   def __init__(self, num_features,momentum=0.01,eps=1e-6):
   # def __init__(self, num_features,momentum=1e-3,eps=1e-3,affine=True):

       super(batchRenorm, self).__init__()

       self.num_features = num_features
       self.eps = eps
       self.momentum = momentum
       self.weight = nn.Parameter(torch.Tensor(num_features))
       self.bias = nn.Parameter(torch.Tensor(num_features))
       self.register_buffer('running_mean', torch.Tensor(num_features))
       self.register_buffer('running_var', torch.Tensor(num_features))
       self.mode = True
       self.reset_parameters()

   def train(self, mode):
       self.mode = mode

   def eval(self, mode):
       self.mode = mode

   def reset_parameters(self):
       self.running_mean.zero_()
       self.running_var.fill_(1)
       self.weight.data.fill_(1.0)
       self.bias.data.fill_(0)

   def __repr__(self):
       return self.__class__.__name__ + '(' + str(self.num_features) \
                + ', eps=' + str(self.eps) \
                + ', momentum=' + str(self.momentum) \
                + ', affine=' + str(self.affine) +')'

   def forward(self,input):

       beta = self.bias.view(1,self.num_features)
       gamma = self.weight.view(1,self.num_features)

       input = input.permute(0,2,1).contiguous()
       input_resize = input.view(-1,self.num_features).contiguous()

       if self.mode == True:
           self.running_var = (1-self.momentum)*self.running_var+self.momentum*torch.var(input_resize,0).data
           self.running_mean = (1-self.momentum)*self.running_mean+self.momentum*torch.mean(input_resize,0).data


       mean = Variable(self.running_mean)
       std  = Variable(torch.sqrt(self.running_var)+self.eps)
       output = (input-mean)/std
       output = output*self.weight + self.bias

       return output.permute(0,2,1).contiguous()

if __name__ == "__main__":

    input = Variable(torch.ones(5,4,3)).cuda()
    bn = batchRenorm(4).cuda()
    bn.train(True)
    bn(input)
    bn.eval(False)
    bn(input)
