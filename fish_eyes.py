import cv2
import numpy as np

def fish_eye(image, k1, k2):
    height, width = image.shape[:2]
    map_x, map_y = np.meshgrid(np.arange(width), np.arange(height))

    map_x = (map_x - width/2)/(width/2)
    map_y = (map_y - height/2)/(height/2)

    r, theta = cv2.cartToPolar(map_x, map_y)
    r = r**2*k1 + r*k2

    map_x, map_y = cv2.polarToCart(r, theta)
    
    map_x = np.int32(map_x * width/2 + width/2)
    map_y = np.int32(map_y * height/2 + height/2)

    fish_eye_image = cv2.remap(image, map_x, map_y, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)

    return fish_eye_image

# 讀取圖片
image = cv2.imread('IMG_0112.jpg')

# 設定魚眼效果參數 (k1, k2)
k1 = 0.5
k2 = 0.5

# 套用魚眼效果
fish_eye_image = fish_eye(image, k1, k2)

# 顯示原始圖片和魚眼效果圖片
cv2.imshow('Original Image', image)
cv2.imshow('Fish Eye Effect', fish_eye_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
