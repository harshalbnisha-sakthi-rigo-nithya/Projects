import cv2

# Global variables
points = []
annotations = []
font = cv2.FONT_HERSHEY_SIMPLEX

def click_event(event, x, y, flags, param):
    # On left mouse click
    if event == cv2.EVENT_LBUTTONDOWN:
        text = input(f"Enter annotation for point ({x}, {y}): ")
        points.append((x, y))
        annotations.append(text)
        cv2.putText(img, text, (x, y), font, 0.7, (0, 0, 255), 2)
        cv2.circle(img, (x, y), 4, (255, 0, 0), -1)
        cv2.imshow("Image Annotation", img)

# Load image
path = "Codingal-Projects\AIEPCM2L2_Activities_Boilerplate_code_(2)-7a3e\AIEPCM2L2 Activities Boilerplate code\example.jpg"  # Change to your image path
img = cv2.imread(path)

if img is None:
    print("Error: Could not open or find the image.")
    exit()

cv2.imshow("Image Annotation", img)
cv2.setMouseCallback("Image Annotation", click_event)

print("Instructions:")
print(" - Left-click to add annotation.")
print(" - Press 's' to save annotated image.")
print(" - Press 'q' to quit.")

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite("annotated_image.jpg", img)
        print("Image saved as annotated_image.jpg")
    elif key == ord('q'):
        break

cv2.destroyAllWindows()
