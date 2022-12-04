import cv2
import numpy as np

def openVideo(vdoPath, lbl):
    cap = cv2.VideoCapture(vdoPath)
    lbl.setText("Video is loaded.")
    fps = cap.get(cv2.CAP_PROP_FPS)
    return cap, fps

def getKpts(frame):
    params = cv2.SimpleBlobDetector_Params()
    params.filterByArea = True
    params.minArea = 35
    params.maxArea = 55
    params.filterByInertia = True
    params.minInertiaRatio = 0.4
    params.maxInertiaRatio = 1
    params.filterByCircularity = True
    params.minCircularity = 0.8
    params.maxCircularity = 1

    detector = cv2.SimpleBlobDetector_create(params)
    kpts = detector.detect(frame)

    return kpts

def process(vdoPath, lbl):
    cap, _ = openVideo(vdoPath, lbl)
    _, frame = cap.read()
    cap.release()

    kpts = getKpts(frame)
    for kpt in kpts:
        x, y = int(kpt.pt[0]), int(kpt.pt[1])
        cv2.rectangle(frame, (x-6, y-6), (x+6, y+6), (0, 0, 255), 1)
        cv2.line(frame, (x, y-6), (x, y+6), (0, 0, 255), 1)
        cv2.line(frame, (x-6, y), (x+6, y), (0, 0, 255), 1)

    cv2.imshow("Image", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def trackVdo(vdoPath, lbl):
    cap, fps = openVideo(vdoPath, lbl)

    ret, oldFrame = cap.read()
    oldGry = cv2.cvtColor(oldFrame, cv2.COLOR_BGR2GRAY)
    oldKptsTmp = getKpts(oldGry)
    oldKpts = list()
    for kpt in oldKptsTmp:
        oldKpts.append([kpt.pt[0], kpt.pt[1]])
    oldKpts = np.array(oldKpts, dtype=np.float32)
    oldKpts = oldKpts.reshape(-1, 1, 2)

    lk_params = dict( winSize  = (15, 15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    mask = np.zeros_like(oldFrame)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gry = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        kpts, st, err = cv2.calcOpticalFlowPyrLK(oldGry, gry, oldKpts, None, **lk_params)
        gNew = kpts[st==1]
        gOld = oldKpts[st==1]

        for i, (new, old) in enumerate(zip(gNew, gOld)):
            xN, yN = new.ravel()
            xO, yO = old.ravel()
            xN, yN, xO, yO = int(xN), int(yN), int(xO), int(yO)
            mask = cv2.line(mask, (xN, yN), (xO, yO), (0, 255, 255), 2)
            frame = cv2.circle(frame, (xN, yN), 5, (0, 255, 255), -1)
        img = cv2.add(frame, mask)
        cv2.imshow("Image", img)
        key = cv2.waitKey(int(1000/fps))
        if key == 27:
            break

        oldGry = gry.copy()
        oldKpts = kpts.reshape(-1, 1, 2)

    cap.release()
    cv2.destroyAllWindows()