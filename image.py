import cv2
import numpy as np
#import picamera
#def Pi_cam():
    #camera = picamera.PiCamera()
    #camera.capture('image.jpg')

lower_range_rood = np.array([169, 100, 100], dtype=np.uint8)
upper_range_rood = np.array([189, 255, 255], dtype=np.uint8)

lower_range_geel = np.array([15, 100, 100], dtype=np.uint8)
upper_range_geel = np.array([35, 255, 255], dtype=np.uint8)

lower_range_blauw = np.array([95, 100, 100], dtype=np.uint8)
upper_range_blauw = np.array([115, 255, 255], dtype=np.uint8)

lower_range_groen = np.array([64, 100, 100], dtype=np.uint8)
upper_range_groen = np.array([84, 255, 255], dtype=np.uint8)


def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )
def find_squares(img):
    img = cv2.GaussianBlur(img, (5, 5), 0)
    squares = []
    for gray in cv2.split(img):
        for thrs in range(0, 255, 26):
            if thrs == 0:
                bin = cv2.Canny(gray, 0, 50, apertureSize=5)
                bin = cv2.dilate(bin, None)
            else:
                retval, bin = cv2.threshold(gray, thrs, 255, cv2.THRESH_BINARY)
            bin, contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                cnt_len = cv2.arcLength(cnt, True)
                cnt = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
                if len(cnt) == 4 and cv2.contourArea(cnt) > 1000 and cv2.isContourConvex(cnt):
                    cnt = cnt.reshape(-1, 2)
                    max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in range(4)])
                    if max_cos < 0.1:
                        squares.append(cnt)
    return squares
def get_img(option):
    if option == 'pc':
        img = cv2.imread("test.jpg", 1)
        return img
    elif option == 'PI':
        import picamera
        camera = picamera.PiCamera()
        camera.capture('image.jpg')
        img = cv2.imread("image.jpg", 1)
        return img
    else:
        print("invalid option")
def find_color(hsv):
    if cv2.inRange(hsv, lower_range_rood, upper_range_rood).any():
        print("dit is rood")
    elif cv2.inRange(hsv, lower_range_geel, upper_range_geel).any():
        print("dit is geel")
    elif cv2.inRange(hsv, lower_range_blauw, upper_range_blauw).any():
        print("dit is blauw")
    elif cv2.inRange(hsv, lower_range_groen, upper_range_groen).any():
        print("dit is groen")
    else:
        print("ik weet niet man")
def show_image(img):
    cv2.imshow('image', img)
    while (1):
        cv2.waitKey(0)
        break
    cv2.destroyAllWindows()
def to_hsv(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return hsv


option = 'PI'
img = get_img(option)
hsv = to_hsv(img)
find_color(hsv)
show_image(img)


#if __name__ == '__main__':
    #from glob import glob
    #for img in glob('lego/*.jpg'):
        #img = cv2.imread(img)
        #hsv = to_hsv(img)
        #find_color(hsv)
        #show_image(img)
        #ch = cv2.waitKey()
        #if ch == 27:
            #break
    #cv2.destroyAllWindows()