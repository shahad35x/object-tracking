"""
object_tracking
-------------------
Automatic object tracking: watches the webcam feed and draws a box around
anything that moves, Uses background subtraction (MOG2) it learns what the static
background looks like, then anything that diffrint from it is "motion".

Press 'x' to quit.

"""

import cv2

MIN_AREA = 800  # ignore tiny specs of noise smaller than this (in pixels)

cap = cv2.VideoCapture(0)
back_sub = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=True)

while True:
    ok, frame = cap.read()
    if not ok:
        break

    mask = back_sub.apply(frame)
    mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)[1]  # drop shadow pixels (gray in the mask)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, None)          # clean up small noise

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < MIN_AREA:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Object", (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Object Tracking", frame)
    cv2.imshow("Motion Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()
