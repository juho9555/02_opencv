import numpy as np, cv2
import matplotlib as plt

# 이미지 읽기
img = cv2.imread('../img/like_lenna.png')

# 마스크 만들기
mask = np.zeros_like(img)
cv2.circle(mask, (260, 210), 100, (255, 255, 255), -1)
#cv2.circle(이미지, (x, y), 반지름, (색상), 굵기)

# 마스킹
masked = cv2.bitwise_and(img, mask)

# 출력
cv2.imshow('original', img)
cv2.imshow('mask', mask)
cv2.imshow('masked', masked)
cv2.waitKey(0)
cv2.destroyAllWindows()