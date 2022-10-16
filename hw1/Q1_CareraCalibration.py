import os, cv2
import numpy as np

def CornerDectection(folderPath, dirContent):
    for fileName in dirContent:
        file = os.path.join(folderPath, fileName)
        img = cv2.imread(file)
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(grayImg, (11, 8), None)
        if ret == True:
            cv2.drawChessboardCorners(img, (11, 8), corners, ret)
            img = cv2.resize(img, (500, 500))
            cv2.imshow("Image", img)
            cv2.waitKey(500)
    cv2.destroyAllWindows()

def FindIntrinsic(folderPath, dirContent):
    objPoint = np.zeros((8*11, 3), np.float32)
    objPoint[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)

    objPoints = []   # 3D points in world space
    imgPoints = []   # 2D points in image plane

    for fileName in dirContent:
        file = os.path.join(folderPath, fileName)
        img = cv2.imread(file)
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(grayImg, (11, 8), None)
        if ret == True:
            objPoints.append(objPoint)
            imgPoints.append(corners)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objPoints, imgPoints, grayImg.shape[::-1], None, None)
    print("Intrinsic: ")
    print(mtx)
    print()

def FindExtrinsic(numTxt, folderPath, dirContent):
    num = int(numTxt)
    objPoint = np.zeros((8*11, 3), np.float32)
    objPoint[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)

    objPoints = []   # 3D points in world space
    imgPoints = []   # 2D points in image plane

    for fileName in dirContent:
        file = os.path.join(folderPath, fileName)
        img = cv2.imread(file)
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(grayImg, (11, 8), None)
        if ret == True:
            objPoints.append(objPoint)
            imgPoints.append(corners)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objPoints, imgPoints, grayImg.shape[::-1], None, None)
    r, _ = cv2.Rodrigues( np.array(rvecs[num-1]) )
    rt = np.concatenate((r, tvecs[num-1]), axis=1)
    print("Extrinsic of ", numTxt, ".bmp : ", sep="")
    print(rt)
    print()

def FindDistortion(folderPath, dirContent):
    objPoint = np.zeros((8*11, 3), np.float32)
    objPoint[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)

    objPoints = []   # 3D points in world space
    imgPoints = []   # 2D points in image plane

    for fileName in dirContent:
        file = os.path.join(folderPath, fileName)
        img = cv2.imread(file)
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(grayImg, (11, 8), None)
        if ret == True:
            objPoints.append(objPoint)
            imgPoints.append(corners)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objPoints, imgPoints, grayImg.shape[::-1], None, None)
    print("Distortion: ")
    print(dist)
    print()

def ShowResult(folderPath, dirContent):
    objPoint = np.zeros((8*11, 3), np.float32)
    objPoint[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)

    objPoints = []   # 3D points in world space
    imgPoints = []   # 2D points in image plane

    for fileName in dirContent:
        file = os.path.join(folderPath, fileName)
        img = cv2.imread(file)
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(grayImg, (11, 8), None)
        if ret == True:
            objPoints.append(objPoint)
            imgPoints.append(corners)

            ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objPoints, imgPoints, grayImg.shape[::-1], None, None)

            height, width = img.shape[:2]
            newCameraMtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (width, height), 1, (width, height))
            dst = cv2.undistort(img, mtx, dist, None, newCameraMtx)

            x, y, w, h = roi
            dst = dst[y:y+h, x:x+w]

            img = cv2.resize(img, (500, 500))
            dst = cv2.resize(dst, (500, 500))
            all = np.hstack([img, dst])
            cv2.imshow("Image and Result", all)
            cv2.waitKey(500)
    
    cv2.destroyAllWindows()