from scripts.func import get_pixel_color, click_mouse, move_and_click, similar_color, capture_screen, move_gundong
from conf import dabaoditu_button, zhuangbei_button
import time


"""
点击进入就完事了，一定时间后出来

"""


def run():
    move_and_click(1477, 779)  # 关闭弹窗
    move_and_click(2099, 488)
    move_and_click(1403, 677)
    time.sleep(2)
    move_and_click(1607,804)
    # 然后就是挂机等打完再退出，默认设置要打五分钟吧
    time.sleep(480)  # 等待5分钟
    move_and_click(2359,432)

if __name__ == "__main__":
    import time
    time.sleep(2)
    run()
