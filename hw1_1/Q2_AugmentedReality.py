import os, cv2
import numpy as np

def ShowOnBoard(words, folderPath, dirContent):
    words = words.upper()
    if len(words) > 6:
        print("Bomb!!")
        return

    objPoint = np.zeros((8*11, 3), np.float32)
    objPoint[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)

    for fileName in dirContent:
        file = os.path.join(folderPath, fileName)

        objPoints = []
        imgPoints = []

        img = cv2.imread(file)
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(grayImg, (11, 8), None)
        if ret == True:
            objPoints.append(objPoint)
            imgPoints.append(corners)

            ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objPoints, imgPoints, grayImg.shape[::-1], None, None)

            for word, (char, bias) in enumerate( zip(words, [ [7, 5, 0], [4, 5, 0], [1, 5, 0], [7, 2, 0], [4, 2, 0], [1, 2, 0] ]) ):
                fs = cv2.FileStorage(os.path.join(folderPath, "Q2_lib", "alphabet_lib_onboard.txt"), cv2.FileStorage_READ)
                fn = fs.getNode(char)

                axises = np.float32(fn.mat().flatten().reshape((-1, 3))) + bias

                for idx in range(0, len(axises), 2):
                    axis = axises[idx: idx+2]
                    imgPts, jac = cv2.projectPoints(axis, np.float32(rvecs), np.float32(tvecs), mtx, dist)
                    img = cv2.line(img, tuple(imgPts[0][0].astype(int)), tuple(imgPts[1][0].astype(int)), (0, 0, 255), 3)

            img = cv2.resize(img, (500, 500))
            cv2.imshow("Image", img)
            cv2.waitKey(1000)
    
    cv2.destroyAllWindows()

def ShowVertically(words, folderPath, dirContent):
    words = words.upper()
    if len(words) > 6:
        print("Bomb!!")
        return

    objPoint = np.zeros((8*11, 3), np.float32)
    objPoint[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)

    for fileName in dirContent:
        file = os.path.join(folderPath, fileName)

        objPoints = []
        imgPoints = []

        img = cv2.imread(file)
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(grayImg, (11, 8), None)
        if ret == True:
            objPoints.append(objPoint)
            imgPoints.append(corners)

            ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objPoints, imgPoints, grayImg.shape[::-1], None, None)

            for word, (char, bias) in enumerate( zip(words, [ [7, 5, 0], [4, 5, 0], [1, 5, 0], [7, 2, 0], [4, 2, 0], [1, 2, 0] ]) ):
                fs = cv2.FileStorage(os.path.join(folderPath, "Q2_lib", "alphabet_lib_vertical.txt"), cv2.FileStorage_READ)
                fn = fs.getNode(char)

                axises = np.float32(fn.mat().flatten().reshape((-1, 3))) + bias

                for idx in range(0, len(axises), 2):
                    axis = axises[idx: idx+2]
                    imgPts, jac = cv2.projectPoints(axis, np.float32(rvecs), np.float32(tvecs), mtx, dist)
                    img = cv2.line(img, tuple(imgPts[0][0].astype(int)), tuple(imgPts[1][0].astype(int)), (0, 0, 255), 3)

            img = cv2.resize(img, (500, 500))
            cv2.imshow("Image", img)
            cv2.waitKey(1000)
    
    cv2.destroyAllWindows()