import os
import cv2
from time import sleep


def cv_size(img):
    h, w, ll = img.shape
    w2 = int(w/2)
    h2 = int(h/2)
    print(h, w)
    if (h == w):
        return img
    if (w > h) :
        i = 0
        if h % 2 == 1 :
            i = 1
        crop = img[0:h, w2-h2:w2+h2+i]
        return crop
    if (w < h) :
        i = 0
        if w % 2 == 1 :
            i = 1
        crop = img[h2-w2:h2+w2 + i, 0:w]
        return crop  

pat = "W:\\REVOKDATA\\images\\"

for i in range (1, 61):
    d = os.path.join(os.getcwd() + "\images\\" + str(i))

    path = pat + str(i) + "\\" + os.listdir(d)[0]
    print(path)
    img = cv2.imread(path)
    img = cv_size(img)
    cv2.imshow("w", img)
    cv2.waitKey(55)
    cv2.imwrite("W:\\REVOKDATA\\images\\" + str(i) + "\\" + "hinh1.jpg", img)
    
