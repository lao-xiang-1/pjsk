import win32gui
import pyautogui
from time import sleep

def image_click(src, region=None, confidence=0.9):
    # # 获取窗口尺寸
    # hwnd = win32gui.FindWindow(None, 'V2364A')
    # if hwnd == 0:
    #     print('窗口不存在！')
    #     exit()
    # left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    # region = (left, top, right - left, bottom - top)

    while True:
        try:
            location = pyautogui.locateCenterOnScreen(src, region=region, confidence=confidence)
            loc_x, loc_y = location
            pyautogui.moveTo(loc_x, loc_y)
            if src == 'image/sandian.png':
                sleep(0.7)
            else:
                sleep(0.3)
            pyautogui.click()
            print(f'已点击{src}')
        except Exception as e:
            print(f'异常{e}, 未找到{src}')
        else:
            break
        finally:
            sleep(0.3)

if __name__ == "__main__":
    image_click('image/sandian.png')