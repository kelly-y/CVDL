import os
import numpy as np
import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from torchsummary import summary
import matplotlib.pyplot as plt
from PIL import Image
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

uiWidth = 391
uiHeight = 371
model = None

def showCifar10():
    transform = transforms.Compose( [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))] )
    dataset = torchvision.datasets.CIFAR10(root="./data", train=True, download=True, transform=transform)
    dataLoader = torch.utils.data.DataLoader(dataset, batch_size=9, shuffle=True, num_workers=2)

    classes = dataset.classes
    dataIter = iter(dataLoader)
    images, labels = next(dataIter)

    fig, axs = plt.subplots(3, 3)
    for i in range(3):
        for j in range(3):
            axs[i, j].imshow(images[i*3+j].permute(1, 2, 0))
            axs[i, j].title.set_text( classes[labels[i*3+j]] )
            axs[i, j].axis("off")
    
    plt.show()

def showMdlStructure():
    global model
    if not model:
        model = torchvision.models.vgg19(pretrained=False)
        model.classifier[6] = nn.Linear(4096, 10)
        model.to(device)
        model.load_state_dict( torch.load( os.path.join(os.getcwd(), "model_Final.pth") ) )
    summary(model, (3, 32, 32))

def showAugmentation(imgPath, uiShow):
    # Show
    pixmap = QPixmap(imgPath)
    pixmap = pixmap.scaled(uiWidth, uiHeight, aspectRatioMode=Qt.IgnoreAspectRatio)
    uiShow.setPixmap(pixmap)

    # Transforms
    img = Image.open(imgPath)

    imgRotater = transforms.RandomRotation(degrees=(0, 180))
    imgRotate = imgRotater(img)
    imgRotate = imgRotate.resize((32, 32))
    imgResizer = transforms.RandomResizedCrop(size=(32, 32))
    imgResize = imgResizer(img)
    imgHorizoner = transforms.RandomHorizontalFlip(p=1)
    imgHorizon = imgHorizoner(img)
    imgHorizon = imgHorizon.resize((32, 32))

    fig, axs = plt.subplots(1, 3)
    axs[0].imshow(imgRotate)
    axs[0].title.set_text("RandomRotation")
    axs[0].axis("off")
    axs[1].imshow(imgResize)
    axs[1].title.set_text("RandomResizedCrop")
    axs[1].axis("off")
    axs[2].imshow(imgHorizon)
    axs[2].title.set_text("RandomHorizontalFlip")
    axs[2].axis("off")

    plt.show()

def showAccLoss(uiShow):
    imgPath = os.path.join(os.getcwd(), "AccLoss_Final.png")
    pixmap = QPixmap(imgPath)
    pixmap = pixmap.scaled(uiWidth, uiHeight, aspectRatioMode=Qt.IgnoreAspectRatio)
    uiShow.setPixmap(pixmap)

def predict(imgPath, uiShow, lblConf, lblPred):
    # Show
    pixmap = QPixmap(imgPath)
    pixmap = pixmap.scaled(uiWidth, uiHeight, aspectRatioMode=Qt.IgnoreAspectRatio)
    uiShow.setPixmap(pixmap)

    # Load model
    global model
    if not model:
        model = torchvision.models.vgg19(pretrained=False)
        model.classifier[6] = nn.Linear(4096, 10)
        model.to(device)
        model.load_state_dict( torch.load( os.path.join(os.getcwd(), "model_Final.pth") ) ) 
    model.eval()
    classes = ["airplane", "automobile", "bird", "cat", "deef", "dog", "frog", "horse", "ship", "truck"]

    # Prediction and Confidence
    img = Image.open(imgPath)   # Open image
    img = img.resize((32, 32))
    imgArr = np.array(img)      # Convert to numpy array
    imgArr = np.expand_dims(imgArr, axis=0)     # Format
    input = torch.Tensor(imgArr).permute(0, 3, 1, 2).to(device)
    output = model(input)       # Predict
    _, predict = torch.max(output.data, 1)
    sftmx = F.softmax(output, dim=1)[0]
    conf = sftmx[predict].item()
    ans = classes[predict]      # Class Name

    # Show
    lblConf.setText("Confidence = " + str( round(conf, 2) ))
    lblPred.setText("Prediction Label: " + ans)