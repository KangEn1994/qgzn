import time, datetime

from scripts.func import get_pixel_color, click_mouse, move_and_click, similar_color, capture_screen
from conf import dabaoditu_button, xiyou_button


def run():
    # # 获取当前日期
    # today = datetime.date.today()
    #
    # # 使用strftime函数格式化日期，%w代表周几（0为周日，1为周一，依此类推）
    # weekday = int(today.strftime("%w"))
    # 设置一个循环时间，这样就可以提前进入了
    now_time = datetime.datetime.now().time()
    while now_time < datetime.time(20, 40, 0):
        time.sleep(1)
        now_time = datetime.datetime.now().time()


    move_and_click(1477, 779)  # 关闭弹窗
    move_and_click(2107,179)   # 打开跨服
    time.sleep(1)
    for i in range(3):
        move_and_click(1740,809)  # 向右选中三次
    # move_and_click(1186,807)   # 选中目标活动
    move_and_click(1019,810)
    move_and_click(1626,734)   # 点击进入
    time.sleep(420)   # 不管是什么活动，等十分钟
    move_and_click(2329, 432)  # 点击退出



    # if weekday in [2, 4, 6]:   # 虚星
    #
    # else:  # 蓬莱
    #
    #     move_and_click(1477, 779)  # 关闭弹窗
    #     move_and_click(2098, 484)
    #     time.sleep(1)
    #     move_and_click(1607,732)
    #
    #     point = get_pixel_color(2516,502)
    #     t = 1
    #     while similar_color(point, "16A526") and t < 420:
    #         time.sleep(1)
    #         t += 1
    #     # 打完之后还有幸运筛子，所以还要等一两分钟
    #     time.sleep(90)
    #     move_and_click(2329,432)




if __name__ == "__main__":
    import time
    time.sleep(2)
    run()

    # import datetime
    #
    # # 获取当前日期
    # today = datetime.date.today()
    #
    # # 使用strftime函数格式化日期，%w代表周几（0为周日，1为周一，依此类推）
    # weekday = int(today.strftime("%w"))
    #
    # # 打印结果（以中文显示周几）
    # weekdays = ["周日", "周一", "周二", "周三", "周四", "周五", "周六"]
    # print(weekdays[weekday])