from scripts.func import get_pixel_color, click_mouse, move_and_click, similar_color, capture_screen, move_gundong
from conf import dabaoditu_button, xiyou_button
import time


def run():
    # 2105,179  EA3FA3
    # 927,808  5A5A5A
    # 1009,807  799367
    # 1673,742  95CCB9
    move_and_click(1477, 779)  # 关闭弹窗
    # 打开跨服
    move_and_click(2105,179)
    # 点击多次左箭头
    move_and_click(927,808)
    move_and_click(927, 808)
    move_and_click(927, 808)
    # 选择第一个
    move_and_click(1009,807)
    # 点击进入
    move_and_click(1639,391)
    move_and_click(1608,802)
    # 预留一秒的时间进入地图
    time.sleep(2)
    point = get_pixel_color(2550,503)
    t = 1
    while similar_color(point, "17A627") and t < 600:
        time.sleep(1)
        point = get_pixel_color(2550,503)
        t += 1
    time.sleep(120)   # 捡东西
    # MoveTo 2343,436    // 点击【退出】  坐标2343,436
    move_and_click(2329,432)

if __name__ == "__main__":
    import time
    time.sleep(2)
    run()