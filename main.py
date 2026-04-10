"""
Pipeline:
1.) Create a window with trackbars fr min and max HSV values
2.) Capture video frame
3.) Display mask to show when object seen
4.) Output HSV values for object seen
"""


import cv2
import numpy as np

def nothing(x):
    pass


cap = cv2.VideoCapture(0)


cv2.namedWindow("Trackbars")

#Creating trackbars to manipulate
cv2.createTrackbar("H min", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("H max", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("S min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("S max", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("V min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("V max", "Trackbars", 255, 255, nothing)

#Enables video feed
while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    #converts standard BGR colour to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Aquiring HSV values
    h_min = cv2.getTrackbarPos("H min", "Trackbars")
    h_max = cv2.getTrackbarPos("H max", "Trackbars")
    s_min = cv2.getTrackbarPos("S min", "Trackbars")
    s_max = cv2.getTrackbarPos("S max", "Trackbars")
    v_min = cv2.getTrackbarPos("V min", "Trackbars")
    v_max = cv2.getTrackbarPos("V max", "Trackbars")


    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    #creates a mask showing what can be seen by the current HSV settings
    mask = cv2.inRange(hsv, lower, upper)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    #Displays current HSV values
    print(f"H:{h_min}-{h_max} S:{s_min}-{s_max} V:{v_min}-{v_max}")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
