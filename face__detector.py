import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("news.jpg")
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.5, minNeighbors=2)

for x, y, w, h in faces:
    #the x, y is the beginning point of the rectangle, and w, h is the end point
    # the (0, 255, 0) represent color, and 3 represent 
    img=cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)

print(faces)
print(type(faces))

#resized=cv2.resize(img, (100,100))
resized=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Gray", resized)
cv2.waitKey()
cv2.destroyAllWindows()