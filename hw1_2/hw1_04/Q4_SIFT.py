import cv2

def keypoints(imgPath):
    img = cv2.imread(imgPath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    sift = cv2.xfeatures2d.SIFT_create()
    kpt = sift.detect(img, None)
    imgKpt = cv2.drawKeypoints(img, kpt, 0)

    cv2.imshow("Image Keypoint", imgKpt)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def matchKeypoints(img1Path, img2Path):
    img1 = cv2.imread(img1Path)
    img2 = cv2.imread(img2Path)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    sift = cv2.xfeatures2d.SIFT_create()
    kpt1, des1 = sift.detectAndCompute(img1,None)
    kpt2, des2 = sift.detectAndCompute(img2,None)

    # BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    print(len(matches[0]))

    # Apply ratio test
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])

    img = cv2.drawMatchesKnn(img1, kpt1, img2, kpt2, good, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv2.imshow("Match", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()