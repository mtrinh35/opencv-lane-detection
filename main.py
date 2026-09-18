import cv2
import numpy as np

# object already created, VideoCapture methods in cap
cap = cv2.VideoCapture('DashCam10Sec.mp4')

# display video specs
print("Frame width: ", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Height: ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("FPS: ", cap.get(cv2.CAP_PROP_FPS))


# allow for window size changes
cv2.namedWindow('DashCamWindow', cv2.WINDOW_NORMAL)

resize_bool = False
triangle = np.array([(0, 2160), (2500, 1080), (3840, 2160)])

# ret says if video reading is success, frame is image itself
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # convert to gray scale, BGR not necessary as it's extra info
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # blur to rid of noise, rids of tiny brightness changes from detection
    blurred_image = cv2.GaussianBlur(gray_image, (0, 0), 5)

    # canny, to detect edges throughout entire image
    edges = cv2.Canny(blurred_image, threshold1=10, threshold2=40)

    mask = np.zeros_like(edges)
    cv2.fillPoly(mask, [triangle], color=255)

    idk = cv2.bitwise_and(edges, mask)

    cv2.imshow('DashCamWindow', idk)
    if resize_bool == False:
        cv2.resizeWindow('DashCamWindow', 800, 525)
        resize_bool = True
    
    # press q to shutdown window
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    
# bottom left corner: (2160, 0)
# bottom right corner: (2160, 3840)
# middle: (1080, 1920)
