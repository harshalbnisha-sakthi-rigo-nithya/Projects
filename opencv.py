import cv2
import imutils
import time
"""
img = cv2.imread("images/humanvsai.png")

cv2.imwrite("images/humanvsaiCopy.png", img)

cv2.imshow("images/humanvsai", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
"""

"""img = cv2.imread("images/humanvsai.png")
gray_Image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", gray_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""img = cv2.imread("images/humanvsai.png")
blurred_Image = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blurred_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""img= cv2.imread("images/humanvsai.png")
canny_Image = cv2.Canny(img, 100, 200)
cv2.imshow("Original Image", img)
cv2.imshow("Canny Image", canny_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""img = cv2.imread("images/humanvsai.png")
dilated_Image = cv2.dilate(img, (7,7), iterations=3)
cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilated_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""img = cv2.imread("images/humanvsai.png")
eroded_Image = cv2.erode(img, (7,7), iterations=3)
cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", eroded_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""img = cv2.imread("images/humanvsai.png")
resized_Image = cv2.resize(img, (500,500))
cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resized_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""
"""
img = cv2.imread("images/humanvsai.png")
cropped_Image = img[100:400, 200:500]
cv2.imshow("Original Image", img)
cv2.imshow("Cropped Image", cropped_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""img = cv2.imread("images/humanvsai.png")
print("Image Shape:", img.shape)
print("Image Size:", img.size)
print("Image Data Type:", img.dtype)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""img = cv2.imread("images/humanvsai.png")
resized_Image = imutils.resize(img, width=20)
cv2.imwrite("images/ResizedImage.png", resized_Image)"""

"""img = cv2.imread("images/humanvsai.png")
guassianBlurimage = cv2.GaussianBlur(img, (5,5), 0)
cv2.imwrite("images/GuassianBlurImage.png", guassianBlurimage)
cv2.imshow("Guassian Blur Image", guassianBlurimage)"""

"""img = cv2.imread("images/humanvsai.png")
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshholdimg = cv2.threshold(grayimg, 180, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite("images/ThreshholdImage.png", threshholdimg)"""

"""vs = cv2.VideoCapture(0)

while True:
    ret, img = vs.read()
    if not ret:
        print("Camera not detected")
        break
    
    cv2.imshow("VideoStream", img)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

vs.release()
cv2.destroyAllWindows()
"""

import cv2
import imutils
import time
"""
img = cv2.imread("images/humanvsai.png")

cv2.imwrite("images/humanvsaiCopy.png", img)

cv2.imshow("images/humanvsai", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
"""

"""img = cv2.imread("images/humanvsai.png")
gray_Image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", gray_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""img = cv2.imread("images/humanvsai.png")
blurred_Image = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blurred_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""img= cv2.imread("images/humanvsai.png")
canny_Image = cv2.Canny(img, 100, 200)
cv2.imshow("Original Image", img)
cv2.imshow("Canny Image", canny_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""img = cv2.imread("images/humanvsai.png")
dilated_Image = cv2.dilate(img, (7,7), iterations=3)
cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilated_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""img = cv2.imread("images/humanvsai.png")
eroded_Image = cv2.erode(img, (7,7), iterations=3)
cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", eroded_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""img = cv2.imread("images/humanvsai.png")
resized_Image = cv2.resize(img, (500,500))
cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resized_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""
"""
img = cv2.imread("images/humanvsai.png")
cropped_Image = img[100:400, 200:500]
cv2.imshow("Original Image", img)
cv2.imshow("Cropped Image", cropped_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""img = cv2.imread("images/humanvsai.png")
print("Image Shape:", img.shape)
print("Image Size:", img.size)
print("Image Data Type:", img.dtype)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""img = cv2.imread("images/humanvsai.png")
resized_Image = imutils.resize(img, width=20)
cv2.imwrite("images/ResizedImage.png", resized_Image)"""

"""img = cv2.imread("images/humanvsai.png")
guassianBlurimage = cv2.GaussianBlur(img, (5,5), 0)
cv2.imwrite("images/GuassianBlurImage.png", guassianBlurimage)
cv2.imshow("Guassian Blur Image", guassianBlurimage)"""

"""img = cv2.imread("images/humanvsai.png")
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshholdimg = cv2.threshold(grayimg, 180, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite("images/ThreshholdImage.png", threshholdimg)"""

"""vs = cv2.VideoCapture(0)

while True:
    ret, img = vs.read()
    if not ret:
        print("Camera not detected")
        break
    
    cv2.imshow("VideoStream", img)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

vs.release()
cv2.destroyAllWindows()
"""

cam = cv2.VideoCapture(0)   # Use 0 unless you have 2 cameras
time.sleep(1)

firstFrame = None
area = 1000

while True:
    ret, img = cam.read()
    if not ret or img is None:
        print("Camera not detected")
        break

    text = "Normal"
    img = imutils.resize(img, width=1000)

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)

    if firstFrame is None:
        firstFrame = gaussianImg
        continue

    imgDiff = cv2.absdiff(firstFrame, gaussianImg)

    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
    threshImg = cv2.dilate(threshImg, None, iterations=2)

    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        if cv2.contourArea(c) < area:
            continue

        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving Object detected"

    print(text)

    cv2.putText(img, text, (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow("cameraFeed", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
