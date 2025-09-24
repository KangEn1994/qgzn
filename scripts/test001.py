import win32api
import win32con
import win32gui
import win32ui
import time
import numpy as np
from PIL import Image


# 移动鼠标到指定位置
def move_mouse(x, y):
    win32api.SetCursorPos((x, y))
    print(f"鼠标已移动到 ({x}, {y})")


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

    print(f"{'双击' if double else '单击'} {button} 键")

def get_pixel_color(x, y, target=16):
    hdc = win32gui.GetDC(0)
    color = win32gui.GetPixel(hdc, x, y)
    win32gui.ReleaseDC(0, hdc)
    r = color & 0xFF
    g = (color >> 8) & 0xFF
    b = (color >> 16) & 0xFF
    if target == 16:
        hex_color = '{:02X}{:02X}{:02X}'.format(b, g, r)
        print(f"[{x}, {y}]当前颜色识别结果为: {hex_color}")
        return hex_color
    else:
        rgb_tuple = [b, g, r]
        print(f"[{x}, {y}]当前颜色识别结果为: {rgb_tuple}")
        return rgb_tuple

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


# 使用示例
if __name__ == "__main__":
    # 移动鼠标到 (100, 100)
    # move_mouse(100, 100)
    # time.sleep(1)
    #
    # # 在当前位置左键单击
    # click_mouse(button="left")
    # time.sleep(1)
    time.sleep(2)
    # 获取坐标(500, 500)的颜色
    for i in range(5):
        for j in range(5):
            color = get_pixel_color(2311 + i, 474 + j)
            # print(f"坐标 ({2311 + i},{474 + j}) 的RGB颜色值: {color}")
            # time.sleep(0.1)
    # color = get_pixel_color(2311,474)
    # print(f"坐标 (500,500) 的RGB颜色值: {color}")


    # 截取全屏
    # full_screenshot = capture_screen()
    # full_screenshot.save("full_screen.png")
    # print("已保存全屏截图: full_screen.png")
    #
    # # 截取指定区域 (左上角x, 左上角y, 宽度, 高度)
    # region_screenshot = capture_screen((300, 200, 800, 600))
    # region_screenshot.save("region_screenshot.png")
    # print("已保存区域截图: region_screenshot.png")

    # 鼠标移动到 (500, 500) 并双击
    move_mouse(500, 500)
    click_mouse(button="left", double=True)
