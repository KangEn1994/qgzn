from scripts.func import get_pixel_color, click_mouse, move_and_click, similar_color, capture_screen, move_gundong,jietu, up_mouse, down_mouse, move_mouse
from conf import dabaoditu_button, xiyou_button
import time


def run():
    # 2105,179  EA3FA3
    # 927,808  5A5A5A
    # 1009,807  799367
    # 1673,742  95CCB9
    # 打开跨服
    move_and_click(2105,179)

    # 点击多次左箭头
    move_and_click(927, 808)
    move_and_click(927, 808)
    move_and_click(927, 808)
    # 选择第一个
    move_and_click(1009, 807)
    # 选择巫蛊祭坛
    move_and_click(1010, 733)
    # 点击进入
    move_and_click(1673, 742)
    # 预留一秒的时间进入地图
    time.sleep(1)
    jietu("进入巫蛊祭坛")
    # color_list = [[2461, 679], [2461, 655], [2461, 549], [2461, 606], [2461, 630], [2461, 582], [2461, 533]]
    color_list = [[2453, 645], [2461, 621], [2461, 597], [2461, 573], [2461, 549], [2461, 525],
                  [2461, 501]]  # 默认先置空   第一个是lv10所以x小一点
    flag = True
    t = 0  # 设置0.2秒检测一次，如果2分钟后都还存在， 则判定出现问题，默认退出
    while flag and t < 600:
        flag = False
        for i in range(len(color_list)):
            # print(color_list)
            while similar_color(get_pixel_color(color_list[i][0], color_list[i][1]), "179F26",
                                threshold=15) and t < 600:
                # 找到目标boss并进行攻击
                move_and_click(color_list[i][0] - 100, color_list[i][1])
                # color_list[i] = get_pixel_color(color_list[i][0], color_list[i][1])
                t += 1
                flag = True
                time.sleep(0.2)

    jietu("巫蛊地图清扫完毕")



    # 出了新地图
    move_and_click(2504,224)
    # 点击多次左箭头
    move_and_click(927, 808)
    move_and_click(927, 808)
    move_and_click(927, 808)
    # 选择第一个
    move_and_click(1009, 807)
    # 点击进入
    move_and_click(1673, 742)
    # 预留一秒的时间进入地图
    time.sleep(1)
    jietu("进入巫蛊沼泽")
    # 这个地图的boss一共有 阿罗纳3 巫珏3  七神3  愚者2  奎师那2  苗淼尔2   乌苏1   阿若野1  东西南北中5  合计22只，y坐标偏差22*24=528， 最下面的y没默认为   679
    # 先移动到最下面   移动时使用x坐标2450    一个页面只能显示8只，所以需要翻页3次
    move_mouse(2450, 679)
    time.sleep(0.5)
    down_mouse()
    time.sleep(0.5)
    move_mouse(2450, 0)
    time.sleep(0.5)
    up_mouse()
    time.sleep(0.5)
    # 第一次清扫
    # color_list = [[2461, 679 - 24 * j] for j in range(8)]
    color_list = [[2461, 679], [2461, 655], [2461, 557], [2461, 606], [2461, 630], [2461, 582], [2461, 533], [2461, 509]]
    flag = True
    t = 0  # 设置0.2秒检测一次，如果2分钟后都还存在， 则判定出现问题，默认退出
    while flag and t < 600:
        flag = False
        for i in range(len(color_list)):
            # print(color_list)
            while similar_color(get_pixel_color(color_list[i][0], color_list[i][1]), "179F26",
                                threshold=15) and t < 600:
                # 找到目标boss并进行攻击
                move_and_click(color_list[i][0] - 100, color_list[i][1])
                # color_list[i] = get_pixel_color(color_list[i][0], color_list[i][1])
                t += 1
                flag = True
                time.sleep(0.2)
    # 向上移动
    move_mouse(2450, 679)
    time.sleep(0.5)
    down_mouse()
    time.sleep(0.5)
    move_mouse(2450, 679 + 24 * 8 + 2)
    time.sleep(0.5)
    up_mouse()
    time.sleep(0.5)
    # 第二次清扫
    # color_list = [[2461, 679 - 24 * j] for j in range(8)]
    color_list = [[2461, 679], [2461, 655], [2461, 630], [2461, 606], [2461, 582], [2461, 557], [2461, 533], [2461, 509]]
    flag = True
    t = 0  # 设置0.2秒检测一次，如果2分钟后都还存在， 则判定出现问题，默认退出
    while flag and t < 600:
        flag = False
        for i in range(len(color_list)):
            # print(color_list)
            while similar_color(get_pixel_color(color_list[i][0], color_list[i][1]), "179F26",
                                threshold=15) and t < 600:
                # 找到目标boss并进行攻击
                move_and_click(color_list[i][0] - 100, color_list[i][1])
                # color_list[i] = get_pixel_color(color_list[i][0], color_list[i][1])
                t += 1
                flag = True
                time.sleep(0.2)
    # 向上移动
    move_mouse(2450, 679)
    time.sleep(0.5)
    down_mouse()
    time.sleep(0.5)
    move_mouse(2450, 679 + 24 * 8 + 2)
    time.sleep(0.5)
    up_mouse()
    time.sleep(0.5)
    # 第三次清扫
    # color_list = [[2461, 675 - 24 * j] for j in range(8)]
    # color_list = [[2461, 679], [2461, 655], [2461, 557], [2461, 606], [2461, 630], [2461, 582], [2461, 533]]
    color_list = [[2461, 674], [2461, 650], [2461, 626], [2461, 602], [2461, 577], [2461, 553], [2461, 529], [2461, 504]]
    color_list = [[2461, 626], [2461, 553], [2461, 602], [2461, 529], [2461, 577],[2461, 504]]
    flag = True
    t = 0  # 设置0.2秒检测一次，如果2分钟后都还存在， 则判定出现问题，默认退出
    while flag and t < 600:
        flag = False
        for i in range(len(color_list)):
            # print(color_list)
            while similar_color(get_pixel_color(color_list[i][0], color_list[i][1]), "179F26",
                                threshold=15) and t < 600:
                # 找到目标boss并进行攻击
                move_and_click(color_list[i][0] - 100, color_list[i][1])
                # color_list[i] = get_pixel_color(color_list[i][0], color_list[i][1])
                t += 1
                flag = True
                time.sleep(0.2)




    # 确认已经都打完了
    # MoveTo 2343,436    // 点击【退出】  坐标2343,436
    move_and_click(2305,432)


if __name__ == "__main__":
    import time
    time.sleep(2)
    run()
