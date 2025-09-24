import win32gui
import win32con
import ctypes

# 获取句柄为394888的窗口
hwnd = 394888
if win32gui.IsWindow(hwnd):
    # 获取窗口左上角坐标
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    # 计算窗口内坐标(500, 500)的屏幕绝对坐标
    x = left + 500
    y = top + 500
    # 获取窗口DC
    hdc = win32gui.GetDC(hwnd)
    # 获取颜色
    color = win32gui.GetPixel(hdc, 500, 500)
    # print(color)
    win32gui.ReleaseDC(hwnd, hdc)
    r = color & 0xff
    g = (color >> 8) & 0xff
    b = (color >> 16) & 0xff
    print(f"窗口坐标(500,500)颜色: R={r}, G={g}, B={b}")
    # 鼠标左键点击
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    ctypes.windll.user32.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
else:
    print("窗口句柄不存在")

# hwnd_list = []
# win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hwnd_list)
#
# print(hwnd_list)
#
# for each in hwnd_list:
#     text = win32gui.GetWindowText(each)
#     if "chrome" in text.lower() or "firefox" in text.lower() or "edge" in text.lower() or "倾国" in text:
#         print(each, win32gui.GetWindowText(each))