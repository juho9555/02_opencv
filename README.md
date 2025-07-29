# opencv

## 📂 주요 실습 파일 요약 + 핵심 구문

| 파일명 | 주요 내용 | 핵심 함수 / 구문 |
|--------|-----------|------------------|
| **bgr2gray.py** | 컬러 이미지를 Grayscale로 변환 | `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`<br>`cv2.split()` + 평균 |
| **bgr2yuv.py** | BGR → YUV 변환, Y(밝기) 채널 추출 | `cv2.cvtColor(img, cv2.COLOR_BGR2YUV)` |
| **color.py** | 다양한 색공간 실습 (HSV, LAB 등) | `cv2.cvtColor(img, cv2.COLOR_BGR2HSV)` |
| **chromakey.py** | 초록 배경 제거 (크로마키 기법) | `cv2.inRange()`<br>`cv2.bitwise_and()` |
| **cropped.jpg** | ROI 실습용 잘라낸 이미지 (이미지 파일) | - |
| **histo.py** | Grayscale 히스토그램 분석 | `cv2.calcHist([gray], [0], None, [256], [0, 256])`<br>`matplotlib.pyplot.plot()` |
| **histo_rgb.py** | RGB 각 채널별 히스토그램 | `cv2.split(img)`<br>채널별 `calcHist()` |
| **histo_gray.py** | 그레이스케일 히스토그램 시각화 | `cv2.cvtColor()` + `calcHist()` |
| **histo_equalize.py** | 히스토그램 평활화 (대비 향상) | `cv2.equalizeHist(gray)` |
| **histo_normalize.py** | 픽셀 값 정규화 (0~255 범위로) | `cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)` |
| **masking.py** | 특정 영역만 추출 (마스킹) | `cv2.inRange()`<br>`cv2.bitwise_and()` |
| **threshold.py** | 임계값 기반 이진화 | `cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)` |

---

## 📝 수업 정리

첫번째로 복잡하게 풀어서 쓰는 방법이 있다. 예를 들어, b, g, r 값을 int 타입으로 바꾼 다음에 각각 분리해서 평균을 구하고, 다시 uint8로 변환하는 식이다.  
근데 이렇게 쓰면 코드도 길고 보기 어렵다. 그래서 OpenCV에서 제공하는 `cv2.cvtColor()` 함수를 쓰면 훨씬 간단하게 처리할 수 있다.

그리고 색공간은 그냥 RGB만 있는 게 아니라 YUV, HSV 등 다양하다. 상황에 따라서 더 유리한 색공간을 쓰는 게 좋다. 예를 들어 크로마키처럼 특정 색을 제거할 때는 HSV 색공간이 더 편하다.

히스토그램은 밝기 분포를 보거나 대비를 조절할 때 유용하게 쓸 수 있다. `equalizeHist()`나 `normalize()` 같은 함수로 이미지 분위기를 확 바꿀 수 있다.

## 히스토그램과 정규화, 평탄화

- **히스토그램**: 이미지 내 밝기 값이 얼마나 분포되어 있는지 그래프로 나타냄.  
  사진이 너무 어둡거나 밝으면 히스토그램이 한쪽으로 치우침.
  <img width="1280" height="498" alt="image" src="https://github.com/user-attachments/assets/add4ae56-b8f7-4e64-8ba1-a20fcaef1701" />


- **정규화**: 픽셀 값을 0부터 255 사이에 골고루 분포하도록 조절.  
  밝기가 한쪽에 몰려있으면 넓게 펴서 대비를 개선함.
  <img width="1280" height="613" alt="image" src="https://github.com/user-attachments/assets/d5957f63-6ef3-4a85-bcf5-83f03c9744d2" />


- **평탄화(히스토그램 평활화)**: 명암 대비를 높여 어두운 부분은 더 어둡게, 밝은 부분은 더 밝게 만들고, 이미지 디테일이 뚜렷해지면서 선명도가 향상됨.
  <p align="center">
  <img width="300" height="109" alt="image" src="https://github.com/user-attachments/assets/1070f009-ebfc-4182-8c84-740ae9772f1b" />
  </p>



## 역투영 (Back Projection)

- **역투영**은 이미지에서 특정 색상 분포를 기반으로 관심 영역을 찾는 방법이다.  
- 히스토그램을 기준으로 각 픽셀의 색상이 해당 히스토그램과 얼마나 일치하는지 확률처럼 계산한다.  
- 결과는 확률 맵 형태로 나오며, 관심 있는 색상이 많이 포함된 영역이 강조된다.  
- 주로 객체 추적, 색상 기반 검출 등에 사용된다.  

아래와 같이 역투영은 히스토그램 기반 마스킹 기법으로, 특정 색상 분포를 가진 영역만 효과적으로 추출할 수 있다.
<img width="1280" height="351" alt="image" src="https://github.com/user-attachments/assets/d97728c3-9b45-459c-961c-12cc7c6977df" />



