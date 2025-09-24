import datetime

from scripts.func import get_pixel_color, click_mouse, move_and_click, similar_color, capture_screen, move_gundong, jietu, move_mouse, up_mouse, down_mouse
from scripts import bozhuangyuan, panlong
from conf import dabaoditu_button, zhuangbei_button,jingying_button
import time, random
from scripts import func, shenwen
from key import update_key, get_key, RUN_ING, RUN_OVER

floor_one = [1691, 603]
floor_two = [1691,674]
floor_three = [1691,745]
floor = [floor_one, floor_two, floor_three]

now_map_index = 27   # 240阶  从10阶开始计算

map_index_height = 46

map_x = 1016
map_y_list = [374, 420, 466, 512, 558, 604, 650, 696, 742, 788, 834]
map_y_max = 2000

start_i = 11

def qietu(map_index):
    # print(f"当前切图目标: {map_index}")
    # 当前显示的最低层是  now_map_index - 9
    map_index = map_index // 10   # 输入默认是等级，所以是130
    if map_index >= now_map_index - 9:
        # 不需要进行下拉操作
        move_and_click(map_x, map_y_list[map_index - (now_map_index - 9)])
    else:
        # 计算需要下拉的量
        dis = (now_map_index - 9 - map_index) * map_index_height
        move_mouse(map_x, map_y_list[0])
        time.sleep(0.5)
        down_mouse()
        time.sleep(0.5)
        move_mouse(map_x, map_y_list[0] + dis)
        time.sleep(0.5)
        up_mouse()
        move_and_click(map_x, map_y_list[0])

def go_to_benfu(down=0):
    func.exit_map()
    # 打开精英页面
    move_and_click(dabaoditu_button[0], dabaoditu_button[1])
    move_and_click(jingying_button[0], jingying_button[1])
    # 进行切图
    qietu(now_map_index * 10 - down)  # 直接去最高层挂机
    move_and_click(floor[0][0], floor[0][1])
    time.sleep(3)
    # 这时候检测一下神纹即可
    shenwen.run()
    panlong.run()

# 1337,695   龙纹碎片掉落
def run():
    global start_i
    # 跨服判定机制
    now_time = datetime.datetime.now().time()
    time_10 = datetime.time(10, 0, 0)
    time_23 = datetime.time(23, 0, 0)

    kua_flag = False
    if now_time >= time_10 and now_time <= time_23:
        kua_flag = True


    func.close_tanchuang()  # 关闭龙纹碎片掉落和极品掉落

    # 检测是否还在挂机地图，如果不在了送它去一个地图挂机
    point = func.get_pixel_color(2311,591)
    if not func.similar_color(point, "80E0FE"):  # 90FFFF  抓抓的颜色是这个
        func.jietu(f"坐标颜色识别为{point},而非80E0FE， 判定为不在目标地图，执行挂机命令")
        func.exit_map()  # 先退出原图，避免检测错误
        # 打开精英页面
        move_and_click(dabaoditu_button[0], dabaoditu_button[1])
        move_and_click(jingying_button[0], jingying_button[1])
        # 进行切图
        qietu(now_map_index * 10 - 20)  # 直接去最高层挂机
        move_and_click(floor[0][0], floor[0][1])
        time.sleep(3)

        # 见缝插针检测一个神纹
        # from scripts import shenwen
        # shenwen.run()
        # shenwen.run()


    # 本身就在一个挂机地图，则需要检测图中的boss是否已经清理完成
    # 2317,505  17A226   2308,502   7C7B7B
    # 2317,532  18A226   2308,529   7C7B7B
    # 2317,559  18A327   2308,556   7C7B7B

    point1 = func.get_pixel_color(2308,502)
    point2 = func.get_pixel_color(2308,529)
    point3 = func.get_pixel_color(2308,556)
    # print(f"当前boss点颜色识别结果为: {point1}, {point2}, {point3}")
    if not (func.similar_color(point1, "7C7B7B") and func.similar_color(point2, "7C7B7B") and func.similar_color(point3, "7C7B7B")):   # 依旧存在boss
        # 什么也不干  或者执行一次博状元
        if not func.similar_color(point1, "7C7B7B"):
            move_and_click(2308,502)
        elif not func.similar_color(point2, "7C7B7B"):
            move_and_click(2308,529)
        elif not func.similar_color(point3, "7C7B7B"):
            move_and_click(2308,556)

        # print("进行博状元")
        bozhuangyuan.run()
        return True
    # return 0
    # 切换到下一个目标图， 但必须优先保证自己不在跨服地图中
    if kua_flag:
        go_to_benfu()
    else:
        shenwen.run()
    # 以一定的概率，比如20% 触发， start_i 变成11
    if random.random() < 0.2:
        start_i = 11

    p = 0
    if kua_flag:
        p = 1


    for i in range(start_i, now_map_index + 1 - p):
        run_boo = get_key("run")
        if run_boo.value != RUN_ING:
            return False

        move_and_click(dabaoditu_button[0], dabaoditu_button[1])
        move_and_click(jingying_button[0], jingying_button[1])
        qietu(i * 10)  # 切到下一个地图
        # 判定当前地图的boss是否还存在
        # 1691,573  1B9D26
        # 1691,644  1E9726
        # 1691,715  219226
        point_list = [func.get_pixel_color(1691, 573), func.get_pixel_color(1691, 644), func.get_pixel_color(1691, 715)]
        for j in range(len(point_list)):
            if not kua_flag:
                if i == 11:
                    pass
                elif i <= 17 and j > 1:
                    continue
                elif i >= 18 and j > 0:
                    continue
            # if i == 12 and j == 2:
            #     continue

            if func.similar_color(point_list[j], ["1B9D26", "1E9726", "219226"][j], 30):
                jietu(f"{i*10}阶{j+1}层存在精英boss准备攻击")
                move_and_click(floor[j][0], floor[j][1])
                start_i = i
                time.sleep(5)
                return True
        # 如果没有找到，则需要关闭地图，之后重新打开，如此进行切换
        move_and_click(1772, 322)
    else:
        start_i = 11

    if not kua_flag:
        go_to_benfu(down=0)





if __name__ == "__main__":
    import time
    time.sleep(2)
    # while True:
    #     run()
    point = func.get_pixel_color(2311, 591)
    print(point)
    # print(int(random.random() * 5) + 2)
    # move_and_click(dabaoditu_button[0], dabaoditu_button[1])
    # move_and_click(zhuangbei_button[0], zhuangbei_button[1])
    # guaji(20, 1)
    # point1 = func.get_pixel_color(2317, 505)
    # point2 = func.get_pixel_color(2317, 532)
    # point3 = func.get_pixel_color(2317, 559)
    # print(f"当前boss点颜色识别结果为: {point1}, {point2}, {point3}")