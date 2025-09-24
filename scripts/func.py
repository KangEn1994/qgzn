import win32api
import win32con
import win32gui
import win32ui
import time
import numpy as np
from PIL import Image
# import ctypes
# ctypes.windll.shcore.SetProcessDpiAwareness(2)  # PER_MONITOR_DPI_AWARE

def exit_map():
    move_and_click(2317,435)
    move_and_click(2530,341)
    time.sleep(2)

def close_tanchuang():
    move_and_click(1337,695)   # 龙纹
    move_and_click(1333, 770)   # 极品掉落


def move_mouse(x, y):
    win32api.SetCursorPos((x, y))
    # print(f"鼠标已移动到 ({x}, {y})")

def down_mouse():
    # 按住左键
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

def up_mouse():
    # 弹起左键
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def move_gundong(n):
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, n, 0)
    time.sleep(0.2)
    # print(f"鼠标已滚动 ({n})")


def get_pixel_color(x, y, target=16):
    hdc = win32gui.GetDC(0)
    color = win32gui.GetPixel(hdc, x, y)
    win32gui.ReleaseDC(0, hdc)
    r = color & 0xFF
    g = (color >> 8) & 0xFF
    b = (color >> 16) & 0xFF
    if target == 16:
        hex_color = '{:02X}{:02X}{:02X}'.format(b, g, r)
        # print(f"[{x}, {y}]当前颜色识别结果为: {hex_color}")
        return hex_color
    else:
        rgb_tuple = [b, g, r]
        # print(f"[{x}, {y}]当前颜色识别结果为: {rgb_tuple}")
        return rgb_tuple


# 鼠标点击 (可指定左键或右键)
def click_mouse(button="left", double=False):
    if button.lower() == "left":
        down_event = win32con.MOUSEEVENTF_LEFTDOWN
        up_event = win32con.MOUSEEVENTF_LEFTUP
    elif button.lower() == "right":
        down_event = win32con.MOUSEEVENTF_RIGHTDOWN
        up_event = win32con.MOUSEEVENTF_RIGHTUP
    else:
        raise ValueError("不支持的鼠标按钮类型")

    win32api.mouse_event(down_event, 0, 0)
    win32api.mouse_event(up_event, 0, 0)

    if double:
        time.sleep(0.1)
        win32api.mouse_event(down_event, 0, 0)
        win32api.mouse_event(up_event, 0, 0)

    # print(f"{'双击' if double else '单击'} {button} 键")


def move_and_click(x, y, button="left", double=False):
    move_mouse(x, y)
    time.sleep(0.5)  # 等待点击完成
    click_mouse(button, double)
    time.sleep(0.5)  # 等待点击完成

def similar_color(color1, color2, threshold=10):
    """
    判断两个颜色是否相似
    :param color1: 第一个颜色 (16进制字符串或RGB/BGR元组)
    :param color2: 第二个颜色 (16进制字符串或RGB/BGR元组)
    :param threshold: 相似度阈值
    :return: bool
    """
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        if len(hex_color) == 6:
            return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        raise ValueError('16进制颜色格式错误')

    if isinstance(color1, str):
        color1 = hex_to_rgb(color1)
    if isinstance(color2, str):
        color2 = hex_to_rgb(color2)

    return all(abs(c1 - c2) <= threshold for c1, c2 in zip(color1, color2))



# 屏幕截图 (全屏或区域截图)
def capture_screen(region=None):
    # 获取屏幕尺寸
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    # 如果指定区域，使用区域参数
    if region:
        left, top, width, height = region
        if width <= 0 or height <= 0:
            raise ValueError("无效的区域参数")

    # 创建设备上下文
    hdesktop = win32gui.GetDesktopWindow()
    hdc = win32gui.GetWindowDC(hdesktop)
    cdc = win32ui.CreateDCFromHandle(hdc)
    mdc = cdc.CreateCompatibleDC()

    # 创建位图
    bitmap = win32ui.CreateBitmap()
    bitmap.CreateCompatibleBitmap(cdc, width, height)
    mdc.SelectObject(bitmap)

    # 拷贝屏幕内容
    mdc.BitBlt((0, 0), (width, height), cdc, (left, top), win32con.SRCCOPY)

    # 转换为PIL图像对象
    bmpinfo = bitmap.GetInfo()
    bmpstr = bitmap.GetBitmapBits(True)
    img = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1
    )

    # 清理资源
    win32gui.DeleteObject(bitmap.GetHandle())
    mdc.DeleteDC()
    cdc.DeleteDC()
    win32gui.ReleaseDC(hdesktop, hdc)

    return img
# print(similar_color("1F1EC1", "1F1ED2", threshold=30))  # 测试颜色相似度函数

from log import get_uuid, add_log
def jietu(text):
    img = capture_screen()
    img_name = get_uuid()
    img.save(f"E:/pycharmProject/yeyou/img/{img_name}.png")
    add_log(f"{text}", img_name)


if __name__ == "__main__":
    # 测试函数
    time.sleep(2)
    move_mouse(1016, 365)
    time.sleep(1)
    down_mouse()
    time.sleep(0.5)
    move_mouse(1016, 1365)
    time.sleep(0.5)
    up_mouse()
    time.sleep(1)
    # move_and_click(200, 200, button="left", double=True)
    # time.sleep(1)
    # print(get_pixel_color(100, 100))
    # print(similar_color("E3F7FF", "E3F7FF", threshold=10))
    # jietu("测试截图功能")