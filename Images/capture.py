import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened():  # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False


counter = 0
iteration = 5
while rval:
    img = []
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if iteration == 5:
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        iteration = 0
    else:
        iteration = iteration + 1

    key = cv2.waitKey(20)
    for (x, y, w, h) in faces:
            frame = cv2.rectangle(frame, (x - 10, y - 10),
                                  (x + w + 10, y + h + 10),
                                  (255, 0, 0), 0)

            if key == 115:
                counter += 1
                cv2.imwrite("img" + str(counter) + ".jpg",
                            frame[y:y + h, x:x + w])

                print("img" + str(counter) + ".jpg SAVED")

    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    if key == 27:  # exit on ESC
        break
cv2.destroyWindow("preview")
