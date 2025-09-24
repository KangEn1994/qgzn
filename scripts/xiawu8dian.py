from scripts.func import get_pixel_color, click_mouse, move_and_click, similar_color, capture_screen, move_gundong, jietu
from conf import dabaoditu_button, zhuangbei_button,jingying_button
import time, random, datetime




def run():
    # 判定今天是星期几
    week_int = datetime.datetime.now().isoweekday()
    # 周几就是数字几

    if week_int in [2,5,7]:
        from scripts import qunxiong
        print(week_int)
    elif week_int in [1,4,6]:
        from scripts import guaji
        print(week_int)
    else:
        print("今天是周三，不进行操作")


run()