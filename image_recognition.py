import win32gui
import pyautogui
from time import sleep
import logging
import sys

class Image:
    def __init__(self):
        # 1. 创建 Logger 实例
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)  # 设置全局最低日志级别

        # 2. 创建日志格式
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # 3. 创建终端输出的 Handler (StreamHandler)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)     # 控制台只显示 INFO 及以上级别
        console_handler.setFormatter(formatter)

        # 4. 创建文件输出的 Handler (FileHandler)
        file_handler = logging.FileHandler('app.log', mode='a', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)      # 文件记录所有 DEBUG 及以上级别
        file_handler.setFormatter(formatter)

        # 5. 将 Handler 添加到 Logger
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

        self.flag = 0

    def image_click(self, src, region=None, confidence=0.9):
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
                self.logger.info(f'已点击{src}')
            except Exception as e:
                self.logger.info(f'点击异常{e}, 未找到{src}')
            else:
                break
            finally:
                sleep(0.3)

    def find_image(self, src, region=None, confidence=0.9):
        try:
            location = pyautogui.locateCenterOnScreen(src, region=region, confidence=confidence)
            if location:
                return 1
        except Exception as e:
            print(f'寻找异常{e}, 未找到{src}')
            return 0
        
if __name__ == "__main__":
    image = Image()
    image.image_click('rifu_image/baochou.png')
