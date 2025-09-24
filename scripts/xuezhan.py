from scripts.func import get_pixel_color, click_mouse, move_and_click, similar_color, capture_screen, move_gundong
from conf import dabaoditu_button, zhuangbei_button
import time


"""
理论上就是点击进图
然后等待一分钟  自动会去把boss打了
之后狂按下一层按钮按15秒，然后按确认进入下一层，如此循环11次

"""

def run():
    # 点击进入虎牢，但是坐标和操作流程忘了
    # move_and_click(2099,488)
    move_and_click(2293,490)
    move_and_click(1403,677)
    time.sleep(3)
    move_and_click(1671,814)
    # 理论上是先点击一个弹窗，然后确认去，再对话一下点确认，之后就进去了

    for i in range(11):  # 理论上12层 默认在1
        time.sleep(30)   # 每一层预计打怪保留12分钟
        for j in range(10):
            move_and_click(2408,720)   # 默认自带一秒的延时
        move_and_click(2091,820)
    time.sleep(60)
    # 12层都结束了
    # 点击退出，重新开始挂机
    move_and_click(2317,435)

if __name__ == "__main__":
    import time
    time.sleep(2)
    run()
