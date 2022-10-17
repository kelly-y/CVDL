import cv2
import numpy as np

def StereoDisparityMap(pathL, pathR):
    imgL = cv2.imread(pathL)
    imgR = cv2.imread(pathR)
    gImgL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
    gImgR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

    stereo = cv2.StereoBM_create(numDisparities=256, blockSize=25)
    disparity = stereo.compute(gImgL, gImgR)
    disp = np.uint8( (disparity-np.min(disparity)) / (np.max(disparity)-np.min(disparity)) * 255 )

    imgL = cv2.resize(imgL, (0, 0), fx=0.3, fy=0.3)
    imgR = cv2.resize(imgR, (0, 0), fx=0.3, fy=0.3)
    disp = cv2.resize(disp, (0, 0), fx=0.3, fy=0.3)

    all = np.hstack([imgL, imgR])
    cv2.imshow("ImageL and ImageR", all)
    cv2.imshow("Result", disp)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

def clkEvent(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        disp, all, width = param[0], param[1], param[2]
        rightX, rightY = x-disp[y][x]+width, y
        newAll = cv2.circle(all, (rightX, rightY), 3, (0, 0, 255), -1)
        newAll = cv2.circle(newAll, (x, y), 3, (255, 0, 0), -1)
        # cv2.destroyAllWindows()
        cv2.imshow("Check Disparity", newAll)

def CheckDisparityValue(pathL, pathR):
    imgL = cv2.imread(pathL)
    imgR = cv2.imread(pathR)
    imgL = cv2.resize(imgL, (0, 0), fx=0.5, fy=0.5)
    imgR = cv2.resize(imgR, (0, 0), fx=0.5, fy=0.5)
    gImgL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
    gImgR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

    stereo = cv2.StereoBM_create(numDisparities=256, blockSize=25)
    disparity = stereo.compute(gImgL, gImgR)
    disparity = np.uint8( (disparity-np.min(disparity)) / (np.max(disparity)-np.min(disparity)) * 255 )

    all = np.hstack([imgL, imgR])
    cv2.imshow("Check Disparity", all)
    cv2.setMouseCallback("Check Disparity", clkEvent, [disparity, all, imgL.shape[1]])

    cv2.waitKey(0)
    cv2.destroyAllWindows()