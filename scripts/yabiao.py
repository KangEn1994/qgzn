from scripts.func import get_pixel_color, click_mouse, move_and_click, similar_color, capture_screen, move_gundong
from conf import dabaoditu_button, zhuangbei_button
import time


"""
计算好每趟镖要多久，定时点按钮就好了

"""


def run():
    move_and_click(2293,490)   # 点击参与活动
    move_and_click(1406,674)   # 点击立即前往
    time.sleep(3)
    for i in range(4):   # 每天四次
        move_and_click(1626,798)   # 点击点券镖车
        time.sleep(110)
        move_and_click(1325,723)   # 点击继续押镖
    # 点击退出
    move_and_click(2306,428)

if __name__ == "__main__":
    import time
    time.sleep(2)
    run()

