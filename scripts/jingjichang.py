from scripts.func import get_pixel_color, click_mouse, move_and_click, similar_color, capture_screen, move_gundong
from conf import dabaoditu_button, zhuangbei_button
import time


"""
计算好每场排队和战斗的时间，然后点按钮就好了，预计每场保留2min应该是足够的

"""


def run():

    for i in range(5):
        move_and_click(2163, 185)  # 点击跨服竞技
        move_and_click(1579,837)   # 点击立即挑战
        time.sleep(60)   # 默认先等一分钟，之后判定是否已经出来
        point = get_pixel_color(2336,374)
        t = 0
        while (not similar_color(point, "54AAEC")) and t < 60:
            time.sleep(1)
            # 避免段位提升
            move_and_click(1997, 648)
            point = get_pixel_color(2336, 374)
            t += 1
        print(f"完成第{i + 1}场竞技")




if __name__ == "__main__":
    import time
    time.sleep(2)
    run()
