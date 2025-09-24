from scripts.func import get_pixel_color, click_mouse, move_and_click, similar_color, capture_screen, move_gundong, jietu
from conf import dabaoditu_button, zhuangbei_button,jingying_button
import time, random, datetime


def run():
    # 进入的方式暂时不考量

    # 设置一个循环时间，这样就可以提前进入了
    now_time = datetime.datetime.now().time()
    while now_time < datetime.time(10, 59, 56):
        time.sleep(1)
        now_time = datetime.datetime.now().time()


    # 打开跨服
    move_and_click(2105, 179)
    # 点击多次左箭头
    move_and_click(927, 808)
    move_and_click(927, 808)
    move_and_click(927, 808)
    # 选择第一个
    move_and_click(1009, 807)
    # 点击魔神入侵
    move_and_click(1442,386)
    # 点击前往挑战
    move_and_click(1612,808)
    time.sleep(1)

    # 逻辑是一个个boss看过去，如果不是自己的就跳过
    # 5个boss攻击位置  2453,510   2453,554   2453,598   2453,642  2453,686

    point_list = [[2453, 510], [2453, 554], [2453, 598], [2453, 642], [2453, 686]]
    point_order = [1, 2, 3, 4, 5]
    # point_list = point_list[::-1]
    key_point = [1280,197]
    key_color ="15A726"

    for each_point_id in point_order:
        each_point = point_list[each_point_id - 1]
        log_flag, t = True, 0
        move_and_click(each_point[0], each_point[1])
        # 如果判定这个boss是不是自己的呢
        time.sleep(15)   # 这是奔跑时间
        # jietu(f"截图{each_point_id}号boss归属情况")
        point = get_pixel_color(key_point[0], key_point[1])
        while similar_color(point, key_color, threshold=10) and t < 180:
            # if log_flag:
            #     jietu(f"检测到{each_point_id}号boss是自己的，持续攻击")
            #     log_flag = False
            time.sleep(0.5)
            t += 1
            point = get_pixel_color(key_point[0], key_point[1])

    move_and_click(2312,435)  # 离开

