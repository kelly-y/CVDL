import cv2
import numpy as np

def subtraction(vdoPath, lbl):
    cap = cv2.VideoCapture(vdoPath)
    fps = cap.get(cv2.CAP_PROP_FPS)
    lbl.setText("Video is loaded.")

    # Get all frames in video
    frames = list()
    grays = list()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frames.append(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        grays.append(gray)
    cap.release()

    # Build gaussian model
    frames, grays = np.array(frames), np.array(grays)
    trnFrms, tstFrms = grays[0:25], grays[25:]
    means = np.mean(trnFrms, axis=0)
    stds = np.std(trnFrms, axis=0)
    stds[stds < 5] = 5

    # Video processing
    masks = list()
    for i in range(tstFrms.shape[0]):
        mask = np.zeros(tstFrms.shape[1:], dtype=np.uint8)
        diff = np.abs(tstFrms[i] - means)
        mask[diff > stds*5] = 255
        masks.append(mask)

    # Show results
    for i in range(tstFrms.shape[0]):
        cv2.imshow("Original", frames[i+25])
        cv2.imshow("Mask", masks[i])
        cv2.imshow("Foreground", cv2.bitwise_and(tstFrms[i], tstFrms[i], mask=masks[i]))
        key = cv2.waitKey(int(1000/fps))
        if key == 27:
            break

    cv2.destroyAllWindows()