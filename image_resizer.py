import cv2
#configurable parameters

source = "BeautyPlus_20190923170633813_save.jpg"
newimg = 'Minu.jpg'
scale_percent = 50
img = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("Mrinmoy" , img)

cv2.waitKey(0)

w = int(img.shape[1] * scale_percent / 100)
h = int(img.shape[0] * scale_percent / 100)

dsize =(w,h)

output = cv2.resize(img,dsize)

cv2.imwrite(newimg, output)
cv2.waitKey(0)
