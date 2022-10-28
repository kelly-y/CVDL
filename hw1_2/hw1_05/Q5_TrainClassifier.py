import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from PIL import Image
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap

uiWidth = 361
uiHeight = 351

def train():
    pass

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
    pass

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

def showAccLoss():
    pass

def predict(imgPath, uiShow, lblConf, lblPred):
    pass