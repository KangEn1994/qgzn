# 设定一个半小时打一次，一次应该耗时还挺久的
import datetime

from scripts.func import get_pixel_color, click_mouse, move_and_click, similar_color, capture_screen, move_gundong, jietu, move_mouse, up_mouse, down_mouse
import time, random
from scripts import func

tiaozhan = [1667,746]
"""
2514,499  16A125
2514,524  179E25
2514,548  16A326
2514,572  16A325
2514,597  189C24
2514,621  17A226
"""

def gongji(n):
    color_list = [[2514, 499], [2514, 524], [2514, 548], [2514, 572], [2514, 597], [2514, 621]]
    flag = True
    t = 0  # 设置0.2秒检测一次，如果2分钟后都还存在， 则判定出现问题，默认退出
    while flag and t < 240:
        flag = False
        for i in range(len(color_list)):
            # print(color_list)
            while similar_color(get_pixel_color(color_list[i][0], color_list[i][1]), "179F26",
                                threshold=30) and t < 240:
                # 找到目标boss并进行攻击
                move_and_click(color_list[i][0] - 200, color_list[i][1])
                # color_list[i] = get_pixel_color(color_list[i][0], color_list[i][1])
                t += 1
                flag = True
                time.sleep(0.2)
    jietu(f"巫蛊禁地{n}清扫完毕")


def run():
    # 打开跨服
    move_and_click(2105, 179)

    # 点击多次左箭头
    move_and_click(927, 808)
    move_and_click(927, 808)
    move_and_click(927, 808)

    # 选择第二个
    move_and_click(1174,814)

    for i in range(1):
        # 先进入
        move_mouse(1002,375)
        time.sleep(0.5)
        down_mouse()
        time.sleep(0.5)
        move_mouse(1002, 675)
        time.sleep(0.5)
        up_mouse()
        move_and_click(1010,409)
        move_and_click(tiaozhan[0], tiaozhan[1])
        # 进行攻击
        time.sleep(2)
        gongji(i + 1)
    # 高度差在64
    first = [1018,368]

    for i in range(7): # 2-8层
        # 基于攻击完成之后
        # 点击打宝地图
        move_and_click(2504,206)
        # 点击多次左箭头
        move_and_click(927, 808)
        move_and_click(927, 808)
        move_and_click(927, 808)

        # 选择第二个
        move_and_click(1174, 814)

        move_and_click(first[0], first[1] + i * 64)
        move_and_click(tiaozhan[0], tiaozhan[1])
        # 进行攻击
        time.sleep(2)
        gongji(i + 2)


    move_and_click(2303,430)
    move_and_click(1413,677)

if __name__ == "__main__":
    import time
    time.sleep(2)
    run()
    # print(int(random.random() * 5) + 2)