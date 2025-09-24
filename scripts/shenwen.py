# 判定神纹boss是否刷新，并且进入地图进行攻击


from scripts.func import get_pixel_color, click_mouse, move_and_click, similar_color, capture_screen
from conf import dabaoditu_button, shenwen_button
import time
from log import add_log, get_uuid


def exist():
    # 1128,449  2121EB     第三层红点
    # 1128,588  1F20EA     第四层红点
    # point1 = get_pixel_color(1224,775)
    # point2 = get_pixel_color(1436,775)
    # if not similar_color(point1, "2623D8"):
    #     return [1224,775]
    # elif not similar_color(point2, "2723D1"):
    #     return [1436,775]
    # else:
    #     return 0

    point1 = get_pixel_color(1228,765)
    point2 = get_pixel_color(1440,765)
    if similar_color(point1, "219224"):
        return [1228,765]
    elif similar_color(point2, "1C9C25"):
        return [1440,765]
    else:
        return 0






def run():
    # 打宝地图
    move_and_click(dabaoditu_button[0], dabaoditu_button[1])
    # 神纹
    move_and_click(shenwen_button[0], shenwen_button[1])
    # 判定是否存在
    move_and_click(1477, 779)  # 关闭弹窗
    point = exist()
    if not point:
        # print("神纹boss不存在，关闭打宝地图")
        move_and_click(1770,320)  # 关闭打宝地图
        return 0

    img = capture_screen()
    img_name = get_uuid()
    img.save(f"img/{img_name}.png")
    add_log(f"开始攻击神纹boss", img_name)

    # print(f"神纹boss存在，坐标: {point}")
    move_and_click(point[0], point[1])
    # 进入挑战

    move_and_click(1428,820)  # 点击【立即挑战】
    time.sleep(35)     # 啥也不用干，等40分钟就完事了
    return 1














if __name__ == "__main__":
    import time
    time.sleep(2)
    run()




