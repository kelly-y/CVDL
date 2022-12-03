import os, cv2, random
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

model = None

def showImages():
    fig, axs = plt.subplots(nrows=1, ncols=2)

    path = os.path.join(os.getcwd(), "inference_dataset")
    randCat = random.choice(os.listdir( os.path.join(path, "Cat") ))
    randDog = random.choice(os.listdir( os.path.join(path, "Dog") ))
    catImg = Image.open(os.path.join(path, "Cat", randCat))
    dogImg = Image.open(os.path.join(path, "Dog", randDog))
    catImg = catImg.resize((224, 224))
    dogImg = dogImg.resize((224, 224))

    axs[0].imshow(catImg)
    axs[0].set_title("Cat")
    axs[0].axis("off")
    axs[1].imshow(dogImg)
    axs[1].set_title("Dog")
    axs[1].axis("off")

    fig.canvas.set_window_title("Show Images")
    plt.show()

def showDistribution():
    img = Image.open( os.path.join(os.getcwd(), "distribution.png") )
    plt.imshow(img)
    plt.axis("off")
    plt.show()

def showMdlStructure():
    global model
    if not model:
        model = torchvision.models.resnet50()

        fcIn = model.fc.in_features
        model.fc = nn.Linear(fcIn, 1)

        model.to(device)
        model.load_state_dict( torch.load( os.path.join(os.getcwd(), "model_Final.pth") ) ) 

    summary(model, (3, 224, 224))

def showCamparison():
    pass

def inference(imgPath, picLbl, txtLbl):
    # Show image
    pixmap = QPixmap(imgPath)
    pixmap = pixmap.scaled(224, 224, aspectRatioMode=Qt.IgnoreAspectRatio)
    picLbl.setPixmap(pixmap)

    # Load model
    global model
    if not model:
        model = torchvision.models.resnet50()

        fcIn = model.fc.in_features
        model.fc = nn.Linear(fcIn, 1)

        model.to(device)
        model.load_state_dict( torch.load( os.path.join(os.getcwd(), "model_Final.pth") ) )
    model.eval()

    # Predict
    classes = ["Cat", "Dog"]
    img = Image.open(imgPath)
    if imgPath[:3] == "png":
        img = img.convert("RGB")
    img = img.resize((224, 224))
    imgArr = np.array(img)
    imgArr = np.expand_dims(imgArr, axis=0)
    inImg = torch.Tensor(imgArr).permute(0, 3, 1, 2).to(device)
    output = model(inImg)
    predict = 0 if output < 0.5 else 1
    ans = classes[predict]

    # Show ans
    txtLbl.setText("Prediction: " + ans)