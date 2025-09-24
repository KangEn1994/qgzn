# 判定魂环boss是否刷新，并且进入地图进行共计


hunhuan_button = [1061, 374]
from scripts.func import get_pixel_color, click_mouse, move_and_click, similar_color, capture_screen
from conf import dabaoditu_button, xiyou_button
import time
from log import add_log, get_uuid

def exist():
    # 1126,601  2020F0    冒号下面的点
    point1 = get_pixel_color(1126,733)
    if similar_color(point1, "14A528"):
        return [1126,733]
    else:
        return 0






def run():
    # 打宝地图
    move_and_click(dabaoditu_button[0], dabaoditu_button[1])
    # 稀有
    move_and_click(xiyou_button[0], xiyou_button[1])
    # 魂环
    move_and_click(hunhuan_button[0], hunhuan_button[1])
    # 判定是否存在
    point = exist()
    if not point:
        print("魂环boss不存在，关闭打宝地图")
        move_and_click(1770,320)  # 关闭打宝地图
        return 0

    img = capture_screen()
    img_name = get_uuid()
    img.save(f"img/{img_name}.png")
    add_log(f"开始进行魂环boss扫图", img_name)
    print(f"魂环boss存在，坐标: {point}")
    move_and_click(point[0], point[1])
    # 进入挑战
    move_and_click(1679, 805)  # 点击【立即挑战】
    time.sleep(1.5)   # 预留一秒的时间进入地图
    # color_list = [get_pixel_color(2547,500), get_pixel_color(2547,529), get_pixel_color(2547,558), get_pixel_color(2547,587)]
    color_list = [[2547,500], [2547,529], [2547,558], [2547,587]]  # 目标boss的坐标
    flag = True
    t = 0    # 设置0.2秒检测一次，如果2分钟后都还存在， 则判定出现问题，默认退出
    while flag and t < 180:
        flag = False
        for i in range(4):
            while similar_color(get_pixel_color(color_list[i][0], color_list[i][1]), "189C26", threshold=30) and t < 180:
                # 找到目标boss并进行攻击
                move_and_click(color_list[i][0] - 200, color_list[i][1])
                # color_list[i] = get_pixel_color(v)
                t += 1
                flag = True
                time.sleep(0.2)
    # 确认已经都打完了
    # MoveTo 2343,436    // 点击【退出】  坐标2343,436
    move_and_click(2343,436)
    move_and_click(1411,675)   # 避免突然刷新
    return 1














if __name__ == "__main__":
    import time
    time.sleep(2)
    run()




