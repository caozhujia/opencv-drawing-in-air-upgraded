import cv2
import numpy as np

ix, iy, k = 200, 200, -1
def mouse(event, x, y, flags, param):
    global ix, iy, k
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
     