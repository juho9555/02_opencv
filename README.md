# opencv
### opencv BGA 변환
```
import cv2
import numpy as np

#기본값
img = cv2.imread('../img/like_lenna.png')
#bgr
bgr = cv2.imread('../img/like_lenna.png', cv2.IMREAD_COLOR)
# a
bgra = cv2.imread('../img/like_lenna.png', cv2.IMREAD_UNCHANGED)

# shape
print("default", img.shape, "color", bgr.shape, "unchanged", bgra.shape)

cv2.imshow('img', img)
cv2.imshow('bgr', bgr)
cv2.imshow('alpha', bgra[:,:,3])

cv2.waitKey(0)
cv2.destroyAllWindows
```
- like_lenna.png를 가져와서 알파값으로 변환시키기
- 위 코드를 기반해서 여러가지로 활용가능 ex)RGB를 그레이 스케일로 변경, RGB값을 YUV로 변환 등

### BGR을 그레이 스케일로 변환
import cv2
import numpy as np

img = cv2.imread('../img/like_lenna.png')


# 복잡한 방법
img2 = img.astype(np.uint16)
b, g, r = cv2.split(img2) # 채널별로 분류

gray1 = ((b + g + r) / 3).astype(np.uint8) #평균값을 연산 후 dtype으로 변경

# 함수 사용하는 방법
```
img = cv2.imread('../img/like_lenna.png')

# 복잡한 방법
img2 = img.astype(np.uint16)
b, g, r = cv2.split(img2) # 채널별로 분류
gray1 = ((b + g + r) / 3).astype(np.uint8) #평균값을 연산 후 dtype으로 변경

# 함수 사용하는 방법
gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # BGR을 그레이스케일로 변경

cv2.imshow('original', img)
cv2.imshow('gray1', gray1)
cv2.imshow('gray2', gray2)
```
- 첫번째로 복잡하게 풀어서 쓰는 방법이 있다. 먼저 b,g,r값을 int값으로 만든 후 채널별로 분류하고 평균값을 통해 dtype으로 변경시키는 방법이다.
- 위 구문은 너무 길어서 opencv에 포함된 cv2.cvtColor() 함수를 이용하면 훨씬 간편하다.

- 
