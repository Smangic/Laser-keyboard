# Made by S级魔人
# During 2021/11/17 18:59
from abc import abstractmethod
import cv2 as cv
import pyautogui
from pynput import keyboard, mouse


Keyboard = keyboard.Controller()
Mouse = mouse.Controller()
class Key:
    def __init__(self, UpLeft_x, UpLeft_y, DownRight_x, DownRight_y, name):
        self.UpLocation = (UpLeft_x, UpLeft_y)  # 键位的左上边界
        self.LowLocation = (DownRight_x, DownRight_y)  # 键位的右下边界
        self.CentalLocation = (int(1 / 2 * (UpLeft_x + DownRight_x)), int(1 / 2 * (UpLeft_y + DownRight_y)))
        self.Name = name

    def getlowlocation(self):
        return self.LowLocation

    def getuplocation(self):
        return self.upLocation

    def __str__(self):
        return self.Name+"的左上角的坐标是" + self.UpLocation.__str__() + "右下角的坐标是" + self.LowLocation.__str__()

    def isCalled(self):
        Keyboard.press(self.Name)
        return

    def drawIt(self, img):
        """在彩色图上画出对应的按键"""
        cv.rectangle(img, self.UpLocation, self.LowLocation, (255, 0, 0), 3)
        # cv.putText(img, self.Name, self.CentalLocation, cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1, cv.LINE_AA)
        return

