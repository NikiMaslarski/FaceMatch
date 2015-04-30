import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened():  # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False


a = 0
while rval:
    img = []
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if a == 0:
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        a = 5
    else:
        a = a - 1

    print(faces)
    for (x, y, w, h) in faces:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h),
                                  (255, 0, 0), 2)
            img.append(frame[y:y + h, x:x + w])

    for index in range(len(img)):
        cv2.imshow("cropped" + str(index), img[index])

    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27:  # exit on ESC
        break
cv2.destroyWindow("preview")
