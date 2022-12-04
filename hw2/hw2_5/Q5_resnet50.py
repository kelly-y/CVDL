import os, random
import numpy as np
import torch
import torchvision
import torch.nn as nn
import torchvision.transforms as transforms
from torchsummary import summary
import matplotlib.pyplot as plt
from PIL import Image
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
    fig = plt.figure(0)
    plt.imshow(img)
    plt.axis("off")
    fig.canvas.set_window_title("Distribution")
    plt.show()

def showMdlStructure():
    global model
    if not model:
        model = torchvision.models.resnet50(pretrained=True)

        fcIn = model.fc.in_features
        model.fc = nn.Linear(fcIn, 1)

        model.to(device)

    summary(model, (3, 224, 224))

def showCamparison():
    img = Image.open( os.path.join(os.getcwd(), "accCompare.png") )
    fig = plt.figure(0)
    plt.imshow(img)
    plt.axis("off")
    fig.canvas.set_window_title("Accuracy Comparison")
    plt.show()

def inference(imgPath, txtLbl):
    # Load model
    global model
    if not model:
        model = torchvision.models.resnet50(pretrained=True)

        fcIn = model.fc.in_features
        model.fc = nn.Linear(fcIn, 1)

        model.to(device)
    model.load_state_dict( torch.load( os.path.join(os.getcwd(), "model", "model_BCE.pth") ) )
    model.eval()
    classes = ["Cat", "Dog"]

    # Define transform
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    # Predict
    img = Image.open(imgPath)
    img = img.convert("RGB")
    imgT = transform(img)
    imgT = imgT.unsqueeze(0)
    imgT = imgT.to(device)
    output = model(imgT)
    output = torch.sigmoid(output)
    predict = 0 if output.item() <= 0.5 else 1
    ans = classes[predict]

    # Show ans
    txtLbl.setText("Prediction: " + ans)