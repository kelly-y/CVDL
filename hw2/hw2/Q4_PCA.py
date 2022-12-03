import os, cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def doPCA(fldPath, dirPath):
    originImgs, rctImgs = list(), list()
    originGrys, rctGrys = list(), list()

    for fName in dirPath:
        img = cv2.imread(os.path.join(fldPath, fName))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        originImgs.append(img)
        originGrys.append(gry)

        # Split channel
        b, g, r = cv2.split(img)
        nB, nG, nR = b/255, g/255, r/255

        pcaB = PCA(n_components=10)
        rDB = pcaB.fit_transform(nB)

        pcaG = PCA(n_components=10)
        rDG = pcaG.fit_transform(nG)

        pcaR = PCA(n_components=10)
        rDR = pcaR.fit_transform(nR)

        # Inverse transform
        rctB = pcaB.inverse_transform(rDB)
        rctG = pcaG.inverse_transform(rDG)
        rctR = pcaR.inverse_transform(rDR)

        # Reconstruct
        rctImg = cv2.merge((rctB, rctG, rctR))
        rctGry = cv2.cvtColor((rctImg*255).astype(np.uint8), cv2.COLOR_BGR2GRAY)
        rctImgs.append(rctImg)
        rctGrys.append(rctGry)

    return originImgs, rctImgs, originGrys, rctGrys

def reconstructImg(fldPath, dirPath):
    fig, ax = plt.subplots(4, 15, figsize=(15, 12), subplot_kw={'xticks':[], 'yticks':[]})

    oImgs, rImgs, _, _ = doPCA(fldPath, dirPath)
    imgs = oImgs[:15] + rImgs[:15] + oImgs[15:] + rImgs[15:]
    for i in range(4):
        for j in range(15):
            ax[i, j].imshow(imgs[i*15+j])

    ax[0, 0].set_ylabel("Origin")
    ax[1, 0].set_ylabel("Reconstruction")
    ax[2, 0].set_ylabel("Origin")
    ax[3, 0].set_ylabel("Reconstruction")

    fig.suptitle("PCA")
    plt.show()

def computeError(fldPath, dirPath):
    _, _, oGrys, rGrys = doPCA(fldPath, dirPath)

    errs = []
    for ogry, rgry in zip(oGrys, rGrys):
        err = np.sum(np.abs(ogry - rgry))
        errs.append(err)

    print(errs)