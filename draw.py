import cv2
import numpy as np

ix, iy, k = 200, 200, -1
def mouse(event, x, y, flags, param):
    global ix, iy, k
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
        k = 1
        

cv2.namedWindow("draw")
cv2.setMouseCallback("draw", mouse)

cap = cv2.VideoCapture(0)


while True:
    _, frm = cap.read()

    frm = cv2.flip(frm, 1)

    cv2.imshow("draw", frm)

    if cv2.waitKey(1) == 27 or k == 1:
        old_gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)
        mask = np.zeros_like(frm)
     