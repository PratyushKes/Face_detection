import cv2

face_cascade= cv2.CascadeClassifier(r"C:\Users\praty\OneDrive\Desktop\face\haarcascade_frontalface_default.xml")
img=cv2.imread(r"C:\Users\praty\OneDrive\Desktop\face\h.jpg", 1)
# resize = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces= face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
for x, y, w, h in faces:
    point1=(x, y)
    point2=(x+w, y+h)
    img= cv2.rectangle(img, point1, point2, (0,255,0), 3)

resized= cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Gray", resized)

cv2.waitKey(0)
cv2.destroyWindow()