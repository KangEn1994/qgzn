from scripts.func import get_pixel_color, click_mouse, move_and_click, similar_color, capture_screen, move_gundong, jietu, move_mouse, up_mouse, down_mouse
from conf import dabaoditu_button, zhuangbei_button,jingying_button
import time, random, datetime
"""
魏   1194,823
1122,668   1406,704
1528,577   1470,490

1228,588   1350,509


蜀   1333,822
1052,569    1128,655
1348,702    1576,618

1232,591   1436,588


吴   1464,822
1051,549   1186,723
1404,723    1560,713

1182,610   1508,604



攻击第一个守卫  2525,552
攻击长官    2536,515

1052,569  159427
"""

location = {
    "wei": {"self": [1194, 823], "small":[[1122,668], [1406,704], [1528,577], [1470,490], [1228,588], [1350,509]]},
    "shu": {"self": [1333, 822], "small":[[1052,569], [1128,655], [1348,702], [1576,618], [1232,591], [1436,588]]},
    "wu": {"self": [1464, 822], "small":[[1051,549], [1186,723], [1404,723], [1560,713], [1182,610], [1508,604]]},
}

location = {
    "wei": {"self": [1194, 823], "small":[[1122,668], [1406,704], [1528,577], [1470,490]]},
    "shu": {"self": [1333, 822], "small":[[1052,569], [1128,655], [1348,702], [1576,618]]},
    "wu": {"self": [1464, 822], "small":[[1051,549], [1186,723], [1404,723], [1560,713]]},
}

last_time = 0

def run():
    global last_time
    now = datetime.datetime.now()
    now_int = int(now.strftime("%H%M%S"))
    if now_int - last_time < 800:
        return 0
    last_time = now_int

    # 这部分主要功能室抢夺城池
    # 进入地图
    move_and_click(2051, 183)
    time.sleep(1)
    move_and_click(1550,794)
    time.sleep(2)
    jietu("进入征战天下准备夺取城池")
    move_and_click(1127, 981)  # 检测的同时进行挂机

    find_flag = False
    gongcheng_flag = True
    if gongcheng_flag:
        for map_key in ["wei", "shu", "wu"]:
            content = f"{map_key}:"
            for index, each_city in enumerate(location[map_key]["small"]):
                move_and_click(2385, 804)  # 打开征战地图
                # 点击打开指定国家的地图
                move_and_click(location[map_key]["self"][0], location[map_key]["self"][1])
                time.sleep(1)
                # 首先要判定这个城市有没有丢失
                point = get_pixel_color(each_city[0], each_city[1])
                if similar_color(point, "159427", threshold=80):   # 相似则说明没丢失
                    # print(f"{map_key}国第{index + 1}个城市没有丢失，跳过")
                    content += f"{index + 1}: 占领;"
                    continue
                else:  # 如果不相似，则说明丢失了，需要点击小城市进行攻击判定
                    move_and_click(each_city[0], each_city[1])
                    time.sleep(2)
                    # 2524,555  09E842
                    point = get_pixel_color(2524,555)
                    point2 = get_pixel_color(2518,557)
                    # print(point)
                    if similar_color(point, "09E842", threshold=30):   # 相似则说明可以进攻，进入攻击命令
                        find_flag = True
                        # print(f"{map_key}国第{index + 1}个城市可以进攻，开始攻击")
                        content += f"{index + 1}: 攻击;"
                        # 1 恢复兵力
                        # move_and_click(2487,643)
                        # time.sleep(0.5)
                        # move_and_click(1405,673)
                        # 2. 攻击第一个卫兵
                        move_and_click(2525,552)
                        point = get_pixel_color(2524,555)
                        t = 0
                        while similar_color(point, "09E842", threshold=30) and t < 30:
                            time.sleep(0.5)
                            point = get_pixel_color(2524,555)
                            t += 1
                        # 3. 攻击boss
                        move_and_click(2536,515)
                        point = get_pixel_color(2524,555)
                        t = 0
                        while t < 40 and not similar_color(point, "09E842", threshold=30):
                            time.sleep(0.5)
                            point = get_pixel_color(2524,555)
                            t += 1
                        # 4. 点击退出
                        move_and_click(2339,430)
                    elif similar_color(point2, "1110D6", threshold=30):   # 相似则说明可以进攻，进入攻击命令
                        # 直接攻击boss
                        find_flag = True
                        # print(f"{map_key}国第{index + 1}个城市可以进攻，开始攻击")
                        content += f"{index + 1}: 攻击;"
                        # 1 恢复兵力
                        move_and_click(2487, 643)
                        time.sleep(0.5)
                        move_and_click(1405, 673)
                        # 2. 攻击第一个卫兵
                        # move_and_click(2525, 552)
                        # point = get_pixel_color(2524, 555)
                        # t = 0
                        # while similar_color(point, "09E842", threshold=30) and t < 30:
                        #     time.sleep(0.5)
                        #     point = get_pixel_color(2524, 555)
                        #     t += 1
                        # 3. 攻击boss
                        move_and_click(2536, 515)
                        point = get_pixel_color(2524, 555)
                        t = 0
                        while t < 40 and not similar_color(point, "09E842", threshold=30):
                            time.sleep(0.5)
                            point = get_pixel_color(2524, 555)
                            t += 1
                        # 4. 点击退出
                        move_and_click(2339, 430)
                    else:
                        # print(f"{map_key}国第{index + 1}个城市还在保护中，跳过")
                        content += f"{index + 1}: 保护;"
                        continue  # 这个城市还在保护中
            # content += "<br/>"
            jietu(content)
        # 点击挂机1分钟，清一些兵力
        if find_flag:
            move_and_click(1127, 981)
            time.sleep(60 * 1)

        # 退出该场景
        move_and_click(2337, 437)
        return 1
    else:
        time.sleep(30)
        # 退出该场景
        move_and_click(2337, 437)
        return 1
if __name__ == "__main__":
    import time
    time.sleep(2)
    run()
