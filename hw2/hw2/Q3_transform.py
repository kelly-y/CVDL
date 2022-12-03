import cv2
import numpy as np

def perspective(vdoPath, imgPath, lblVdo, lblImg):
    # Open image and Video
    img = cv2.imread(imgPath)
    lblImg.setText("Image is loaded.")
    cap = cv2.VideoCapture(vdoPath)
    lblVdo.setText("Video is loaded.")
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Read video and process frame by frame
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Load predefined dictionary & Initialize & Detect
        dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_250)
        parameters = cv2.aruco.DetectorParameters_create()
        mkrCrns, mkrIds, rjtCdts = cv2.aruco.detectMarkers(frame, dictionary, parameters=parameters)

        # Get id of each marker
        id1 = np.squeeze(np.where(mkrIds == 1))
        id2 = np.squeeze(np.where(mkrIds == 2))
        id3 = np.squeeze(np.where(mkrIds == 3))
        id4 = np.squeeze(np.where(mkrIds == 4))

        # Process the transform
        if id1!=[] and id2!=[] and id3!=[] and id4!=[]:     # 4 corners are all detected
            pt1 = np.squeeze(mkrCrns[id1[0]])[0]
            pt2 = np.squeeze(mkrCrns[id2[0]])[1]
            pt3 = np.squeeze(mkrCrns[id3[0]])[2]
            pt4 = np.squeeze(mkrCrns[id4[0]])[3]

            ptsDst = [[pt1[0], pt1[1]], [pt2[0], pt2[1]], [pt3[0], pt3[1]], [pt4[0], pt4[1]]]
            ptsSrc = [[0, 0], [img.shape[1], 0], [img.shape[1], img.shape[0]], [0, img.shape[0]]]

            h, status = cv2.findHomography(np.float32(ptsSrc), np.float32(ptsDst))
            wrapped = cv2.warpPerspective(img, h, (frame.shape[1], frame.shape[0]))

            # Merge
            mask = np.zeros(frame.shape, dtype=np.uint8)
            channel = frame.shape[2]
            ignoreMaskColor = (255,) * channel
            cv2.fillConvexPoly(mask, np.int32(ptsDst), ignoreMaskColor)
            mask = cv2.bitwise_not(mask)
            mskedImg = cv2.bitwise_and(frame, mask)

            result = cv2.bitwise_or(wrapped, mskedImg)

            # Display
            images = np.hstack((frame, result))
            images = cv2.resize(images, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            cv2.imshow("Image", images)
            key = cv2.waitKey(int(1000/fps))
            if key == 27:
                break

    cap.release()
    cv2.destroyAllWindows()