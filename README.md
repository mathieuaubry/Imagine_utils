# Imagine ToolBox
We share some useful scripts for developping deep learning model.
The default environment is : Python 3.6 + Pytorch 1.0 


## Table of Content
* [LoadPartialNetwork](#LoadPartialNetwork)
* [ConvertHR2LR](#ConvertHR2LR)
* [ConvertPNG2JPG](#ConvertPNG2JPG)
* [VisualWebsite](#VisualWeb)

## LoadPartialNetwork
Motivation: Only want to use part of pre-trained network. 
Script is [here](https://github.com/tdeprelle/Imagine_utils/blob/master/LoadPartialNetwork/LoadPartialNetwork.py)

## ConvertHR2LR
Motivation : For visual images, we should firstly save them with high resolution, then convert to low resolution if limited by space memory. 
Dependency : [ImageMagick](https://www.imagemagick.org/)
Script is [here](https://github.com/tdeprelle/Imagine_utils/blob/master/ConvertHR2LR/ConvertHR2LR.py)
A demo can be found in ```ConvertHR2LR/demo.sh```

## ConvertPNG2JPG
Motivation : The same motivation as [ConvertHR2LR](ConvertHR2LR), the function allows to convert png image to jpg image keeping transparence
Dependency : [ImageMagick](https://www.imagemagick.org/)
Script is [here](https://github.com/tdeprelle/Imagine_utils/blob/master/ConvertPNG2JPG/ConvertPNG2JPG.py)
A demo can be found in ```ConvertPNG2JPG/demo.sh```

## VisualWeb
Motivation : Visualizing images with website
Script is [here](https://github.com/tdeprelle/Imagine_utils/blob/master/VisualWeb/visualize.py)
A demo can be found in ```VisualWeb/demo.sh```






