import datetime
import time

from scripts.func import get_pixel_color, click_mouse, move_and_click, similar_color, capture_screen
from log import add_log, get_uuid
from conf import dabaoditu_button, xiyou_button
from key import get_key, RUN_OVER, RUN_ING


def run():

    # 根据时间去进行限定，通常晚上10点以后不再进行点击
    now_time = datetime.datetime.now().time()
    if now_time > datetime.time(22, 0, 0):
        # print("当前时间不适合点击博状元，跳过")
        return 0

    # 单行  2098,484  0A1DFF
    #  多行
    x, y = 2098, 484
    if similar_color(get_pixel_color(2098, 484), "0A1DFF"):
        x, y = 2098, 484
    elif similar_color(get_pixel_color(2098,562), "1A21FF"):# 双行
        x, y = 2098,562
    elif similar_color(get_pixel_color(2098,600), "1427FF"):# 双行
        x, y = 2098,600
    elif similar_color(get_pixel_color(2098,677), "1E32FF"):# 双行
        x, y = 2098,677
    else:  # 都不符合要求
        return 0



    # 假设找到了，那么此时的i, j必然就是目标的坐标
    move_and_click(x, y)
    # 点击掷色子，注意要判定是否有弹窗，所以实际操作可以是关闭弹窗，点击筛子，这样循环

    # 判定是否需要掷色子
    point1, point2, point3 = get_pixel_color(1352, 780), get_pixel_color(1347, 780), get_pixel_color(1343,780)
    # print(point1, point2, point3)
    t = 0
    while (similar_color(point1, "139B28") or similar_color(point2, "139A28") or similar_color(point3, "139A28")) and t < 50:
        if get_key("run").value == RUN_OVER:
            # add_log(f"{get_uuid()} 运行终止，退出博状元")
            return -1
        move_and_click(1477, 779)  # 关闭弹窗
        move_and_click(1337, 824)  # 点击掷色子
        point1, point2, point3 = get_pixel_color(1352, 780), get_pixel_color(1347, 780), get_pixel_color(1343, 780)
        time.sleep(1)
        t += 1



    # 关闭
    move_and_click(1548, 399)
    # 执行挂机
    # move_and_click(1130,981)
    # move_and_click(1130,981)



if __name__ == "__main__":
    import time
    time.sleep(2)
    run()



