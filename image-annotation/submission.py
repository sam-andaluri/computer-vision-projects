import cv2

def drawRect(event, x, y, flags, userdata):
    global startPos, endPos
    if event == cv2.EVENT_LBUTTONDOWN:
        #print("start " + str(x) + "," + str(y))
        startPos = [(x, y)]
    elif event == cv2.EVENT_LBUTTONUP:
        #print("end " + str(x) + "," + str(y))
        endPos = [(x, y)]
        cv2.rectangle(dummy, startPos[0], endPos[0], (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow("Window", dummy)
        features = dummy[startPos[0][1]:endPos[0][1], startPos[0][0]:endPos[0][0]]
        # cv2.imshow("features", features)
        cv2.imwrite("face.jpg", features)

source = cv2.imread("sample.jpg", 1)
# Make a dummy image, will be useful to clear the drawing
dummy = source.copy()
cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawRect)
k = 0
# loop until escape character is pressed
while k != 27:
    cv2.imshow("Window", dummy)
    k = cv2.waitKey(20) & 0xFF
cv2.destroyAllWindows()



