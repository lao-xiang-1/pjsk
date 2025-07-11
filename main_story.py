# 日服
import keyboard
import pyautogui
from time import sleep
import winsound
import win32gui
import image_recognition as im

print('按下1开始运行')
keyboard.wait('1') # 等待按下1
running = True
winsound.Beep(800, 200)

i_r = im.Image()

# 获取鼠标位置
center_x, center_y = pyautogui.position()
# 获取窗口尺寸
hwnd = win32gui.GetForegroundWindow() # 获取当前置顶窗口的句柄
if hwnd == 0:
    print('窗口不存在！')
    exit()
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
region = (left, top, right - left, bottom - top)

while running:
    # 选择剧情
    pyautogui.click()

    # 进入剧情界面
    i_r.image_click('rifu_image/jueding.png', region)

    # 进入剧情
    if i_r.find_image('rifu_image/diyihua.png', region) == 1:
        i_r.image_click('rifu_image/diyihua.png', region)
    elif i_r.find_image('rifu_image/xvzhang.png', region) == 1:
        i_r.image_click('rifu_image/xvzhang.png', region)
    i_r.image_click('rifu_image/kongbai.png', region)
    i_r.image_click('rifu_image/wuyuyin.png', region)

    # # 跳过剧情
    # while True: # 判断是否有OK按钮
    #     while i_r.find_image('rifu_image/sandian.png', region) == 0: # 未找到三点按钮，等待
    #         sleep(0.5)
    #     while i_r.find_image('rifu_image/tiaoguo.png', region) == 0: # 没有跳过就一直点击三点
    #         i_r.image_click('rifu_image/sandian.png', region)
    #         sleep(0.5)
    #     i_r.image_click('rifu_image/tiaoguo.png', region)

    #     if i_r.find_image('rifu_image/quedingtiaoguo.png', region) == 1:
    #         i_r.image_click('rifu_image/quedingtiaoguo.png', region)
    #         break
    #     else:
    #         i_r.image_click('rifu_image/xiayiji.png', region)

    # 快速过剧情
    while i_r.find_image('rifu_image/sandian.png', region) == 0:
        # print('未找到三点按钮，等待')
        sleep(0.5)
    pyautogui.moveTo((left + right) // 2, (top + bottom) // 2)
    while i_r.find_image(r'image\OK.png', region) == 0:
        pyautogui.click()
        # sleep(0.1)
    sleep(1)
    
    # 获取报酬
    while i_r.find_image('rifu_image/jueding.png', region) == 0: # 未找到决定
        if i_r.find_image('rifu_image/OK.png', region) == 1:
            i_r.image_click('rifu_image/OK.png', region)
        elif i_r.find_image('rifu_image/baochou.png', region) == 1:
            i_r.image_click('rifu_image/baochou.png', region)
        elif i_r.find_image('rifu_image/fanhui.png', region) == 1:
            i_r.image_click('rifu_image/fanhui.png', region)

    # 回到初始状态
    sleep(1)
    pyautogui.moveTo(center_x, center_y)
