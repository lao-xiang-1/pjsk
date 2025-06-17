import keyboard
import pyautogui
from time import sleep
import winsound
import win32gui
import image_recognition as i_r

keyboard.wait('1') # 等待按下1
running = True
winsound.Beep(800, 200)

# 获取鼠标位置
center_x, center_y = pyautogui.position()
# 获取窗口尺寸
hwnd = win32gui.FindWindow(None, 'V2364A')
if hwnd == 0:
    print('窗口不存在！')
    exit()
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
region = (left, top, right - left, bottom - top)

while running:
    # 进入角色界面
    pyautogui.mouseDown()
    sleep(1)
    pyautogui.mouseUp()
    sleep(0.3)

    # 上篇
    i_r.image_click('image/shangpian.png', region)
    sleep(0.3)
    i_r.image_click('image/jiesuo.png', region)
    sleep(0.3)
    i_r.image_click('image/wuyuyin.png', region)
    sleep(2)
    i_r.image_click('image/sandian.png', region)
    sleep(0.3)
    i_r.image_click('image/tiaoguo.png', region)
    sleep(0.3)
    i_r.image_click('image/quedingtiaoguo.png', region)
    sleep(0.3)
    pyautogui.click()
    sleep(0.3)
    pyautogui.click()
    sleep(1)

    # # 练习
    # i_r.image_click('image/lianxi.png', region)
    # sleep(0.3)
    # i_r.image_click('image/tuijian.png', region)
    # sleep(0.3)
    # i_r.image_click('image/queding.png', region)
    # sleep(0.3)
    # i_r.image_click('image/OK.png', region)
    # sleep(1)
    # pyautogui.click()
    # sleep(0.5)
    # pyautogui.click()
    # sleep(0.5)
    # i_r.image_click('image/fanhui.png', region)

    # # 下篇
    # sleep(0.3)
    # i_r.image_click('image/xiapian.png', region)
    # sleep(0.3)
    # i_r.image_click('image/jiesuo.png', region)
    # sleep(0.3)
    # i_r.image_click('image/wuyuyin.png', region)
    # sleep(0.3)
    # i_r.image_click('image/sandian.png', region)
    # sleep(0.3)
    # i_r.image_click('image/tiaoguo.png', region)
    # sleep(0.3)
    # i_r.image_click('image/quedingtiaoguo.png', region)
    # sleep(1)
    # pyautogui.click()
    # sleep(0.3)
    # pyautogui.click()
    # sleep(1)

    # 返回
    i_r.image_click('image/fanhui.png', region)
    sleep(0.3)
    pyautogui.moveTo(center_x, center_y)
