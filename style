import cv2
import numpy as np

def apply_style_transfer(image, style):
    # 讀取風格圖片
    style_image = cv2.imread(style)
    
    # 將風格圖片調整為與輸入圖片相同的大小
    style_image = cv2.resize(style_image, (image.shape[1], image.shape[0]))

    # 將風格圖片轉換為灰階
    gray_style = cv2.cvtColor(style_image, cv2.COLOR_BGR2GRAY)

    # 將風格圖片轉換為輸入圖片的負片效果
    negative_style = 255 - gray_style

    # 使用卷積核進行風格轉換
    stylized_image = cv2.filter2D(image, -1, negative_style)

    return stylized_image

# 讀取輸入圖片
input_image = cv2.imread('IMG_0112.jpg')

# 指定風格圖片的路徑
style_path = 'style.jpg'

# 套用風格轉換
stylized_image = apply_style_transfer(input_image, style_path)

# 顯示原始圖片和風格化後的圖片
cv2.imshow('Original Image', input_image)
cv2.imshow('Stylized Image', stylized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
