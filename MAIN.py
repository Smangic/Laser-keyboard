# Made by S级魔人
# During 2021/12/20 22:40
# Made by S级魔人
# During 2021/12/8 23:01
import cv2 as cv
import numpy as np
import pandas as pd
import Keyboard
import time
from matplotlib import pyplot as plt


# 对摄像头的每一帧图像进行形态学操作，并得到较为清晰的二值化后的图像（有可能要把部分区域的值手动置0）
def getBinary(ret, frame):
    """对摄像头的每一帧图像进行形态学操作，并得到较为清晰的二值化后的图像（有可能要把部分区域的值手动置0），返回腐蚀后的二值化图像和灰度图"""
    if ret == True:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        kernel = np.ones((15, 15), np.uint8)
        after_erosion = cv.erode(gray, kernel)
        ret, binary = cv.threshold(after_erosion, 200, 255, cv.THRESH_BINARY)
    # 形态学操作暂时还未进行，仍需对binary进行一些调整

    return binary, after_erosion


# 从二值化图像中提取出所有的contour，并且提取出所有contour的坐标（上下边界以及中心点，尝试那种最好，预想的是得到中心点的坐标）
def getLocation(binary):
    """从二值化图像中提取出所有的contour，并且提取出所有contour的坐标（中心点）返回中心点坐标，以及是否有contour"""
    image, contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    hasContour = False
    while len(contours) is not 0:
        i = 0
        c = []
        while (i < len(contours)):
            j = 0
            while (j < len(contours[i])):
                c.append(contours[i][j][0].tolist())
                j = j + 1
            i = i + 1
        Data = pd.DataFrame(c)
        # center = [Data.mean(0), Data.min(1)]
        Center = (int(Data.mean(0)[0]), int(Data.min(0)[1]))
        hasContour = True
        return Center, hasContour
    return contours, hasContour


def drawCenter(gary, Center, hasContour):
    """在灰度图上画出中心点的坐标,返回彩色图"""
    if hasContour:
        color = cv.cvtColor(gary, cv.COLOR_GRAY2BGR)
        size = 1
        thickness = 4
        point_color = (0, 0, 255)
        cv.circle(color, Center, size, point_color, thickness)
        # cv.imshow("centers", color)
        return color
    else:
        return cv.cvtColor(gary, cv.COLOR_GRAY2BGR)


# 将得到的坐标于所有的键位进行比较，确定键位
def findKeys(Center, hasContour):
    """将得到的坐标于所有的键位进行比较，确定键位"""
    Keys = Keyboard.AllKey
    if hasContour:
        for Key in Keys:
            if (Center[0] > Key.UpLocation[0]) & (Center[0] < Key.LowLocation[0]) & (Center[1] > Key.UpLocation[1]) & (Center[1] < Key.LowLocation[1]):
                Key.isCalled()
                time.sleep(0.5)
                return
    else:
        return


def drawKeyboard(ret, image):
    """画出棋盘，直观判断点对不对(输入为彩色图 )"""
    # color = cv.cvtColor(image, cv.COLOR_GRAY2BGR)

    if ret:
        Keys = Keyboard.AllKey
        for Key in Keys:
            Key.drawIt(image)
        # cv.imshow('Keyboard', color)
        return image
    return image

def undistort(frame):
    fx = 872.088768489628
    cx = 665.292811702698
    fy = 873.008216129698
    cy = 299.017557466373
    k1, k2, p1, p2, k3 = -0.392198647446404, 0.188338835627981, 0.00171707513514057, -0.00141492826920151, -0.0524444216975700

    k = np.array([
        [fx, 0, cx],
        [0, fy, cy],
        [0, 0, 1]
    ])

    d = np.array([
        k1, k2, p1, p2, k3
    ])
    h, w = frame.shape[:2]
    mapx, mapy = cv.initUndistortRectifyMap(k, d, None, k, (w, h), 5)
    return cv.remap(frame, mapx, mapy, cv.INTER_LINEAR)

cap = cv.VideoCapture()
cap.open(0)
cap.set(3, 1080)
cap.set(4, 720)
pts1 = np.float32([[28, 243], [1256, 260], [158, 515], [1098, 530]])
pts2 = np.float32([[0,0], [1280,0], [0,720], [1280,720]])
T=cv.getPerspectiveTransform(pts1,pts2)
while cap.isOpened():
    ret, frame = cap.read()
    undistorted = undistort(frame)
    mapped = cv.warpPerspective(undistorted, T, (1280, 720))
    binary, erosion = getBinary(ret, mapped)
    Center, hasContour = getLocation(binary)
    color = drawCenter(erosion, Center, hasContour)
    KeyPlain = drawKeyboard(ret, color)
    findKeys(Center, hasContour)
    cv.imshow('KeyPlain', KeyPlain)
    if cv.waitKey(5) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()



