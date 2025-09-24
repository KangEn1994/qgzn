from scripts.func import get_pixel_color, click_mouse, move_and_click, similar_color, capture_screen, move_gundong, jietu
from conf import dabaoditu_button, zhuangbei_button,jingying_button
import time, random, datetime




def run():
    # 周二  周五  周日
    # 进入方式暂时跳过不考虑   只考虑共计    2259,639
    # 坐标点位 2411,645   411,684    2411,724
    point_list = [
        [2411, 645],  # 3倍
        [411, 684],   # 2倍
        [2411, 724]   # 1倍
    ]
    now = datetime.datetime.now()
    # print(now.strftime("%H%M%S"))
    now_int = int(now.strftime("%H%M%S"))
    # if now_int < 201950:
    for i, each_point in enumerate(point_list):
        point = get_pixel_color(each_point[0], each_point[1])
        if similar_color(point, "19881F", threshold=20):
            jietu(f"{3 - i}倍旗帜被抢，准备夺回")
            move_and_click(2259, each_point[1] - 6)
    # else:
    #     # 点击退出
    #     move_and_click(2320,432)








if __name__ == "__main__":
    import time
    time.sleep(2)
    run()
    # print(int(random.random() * 5) + 2)