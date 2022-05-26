import cv2
import easyocr

# initialize cascade classifier
numberPlate_cascade = "numberplate_haarcade.xml"
detector = cv2.CascadeClassifier(numberPlate_cascade)

# read image
img = cv2.imread('car6.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#-- Detect Number plates
plates = detector.detectMultiScale(
      img_gray,scaleFactor=1.05, minNeighbors=7,
      minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
print(plates)

# iterate through each detected number plates
for (x,y,w,h) in plates:
    
    # draw bounding box
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Crop the numberplate
    plateROI = img_gray[y:y+h,x:x+w]
    cv2.imshow("Numberplate", plateROI)
    
# Show the final output
cv2.imshow('Output', img)
# wait until  any key is pressed
cv2.waitKey(0)

