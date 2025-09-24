from scripts.func import get_pixel_color, click_mouse, move_and_click, similar_color, capture_screen, move_gundong
from conf import dabaoditu_button, zhuangbei_button
import time


"""
点击进入就完事了，一定时间后出来

"""


def run():
    move_and_click(2097,484)
    move_and_click(1593,803)
    time.sleep(10 * 60 )
    move_and_click(2317,437)

if __name__ == "__main__":
    import time
    time.sleep(2)
    run()
