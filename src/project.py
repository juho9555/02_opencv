import cv2
import numpy as np

# 1. 이미지 불러오기
bg = cv2.imread('../img/NewsDesk.jpg')  # 배경
cat = cv2.imread('../img/StandingCat.jpg')  # 고양이


# 2. 고양이 이미지 비율 유지하며 리사이즈
target_width = 200
scale_ratio = target_width / cat.shape[1]
target_height = int(cat.shape[0] * scale_ratio)
cat = cv2.resize(cat, (target_width, target_height))  # 비율 유지

# 3. 크로마키 마스크 (초록색 제거)
hsv = cv2.cvtColor(cat, cv2.COLOR_BGR2HSV)
lower_green = np.array([35, 40, 40])
upper_green = np.array([85, 255, 255])
mask = cv2.inRange(hsv, lower_green, upper_green)
mask_inv = cv2.bitwise_not(mask)
cat_fg = cv2.bitwise_and(cat, cat, mask=mask_inv)

# 4. 고양이 위치 설정 (중앙 뉴스데스크 위)
x_offset = (bg.shape[1] - target_width) // 2
y_offset = 60  

# ROI 설정 및 마스크 적용
roi = bg[y_offset:y_offset + target_height, x_offset:x_offset + target_width]
bg_masked = cv2.bitwise_and(roi, roi, mask=mask)
combined = cv2.add(bg_masked, cat_fg)
bg[y_offset:y_offset + target_height, x_offset:x_offset + target_width] = combined

# 5. 결과 출력
cv2.imshow('cat_news', bg)
cv2.waitKey(0)
cv2.destroyAllWindows()
