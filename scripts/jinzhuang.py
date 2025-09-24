# 判定金装boss是否刷新，并且进入地图进行共计
"""
判定金装boss方法: 指定坐标是否是红色的

攻击金装boss方法



Sub jintudaguai(x1, y1, x2, y2, x3, y3, x4, y4, t)
	MoveTo 2508, 206// 点击【打宝地图】  坐标2508 206
	Delay delay_time
	LeftClick 1
	Delay delay_time

	MoveTo x1,y1//  点击【稀有boss】  坐标1794  561
	Delay delay_time
	LeftClick 1
	Delay delay_time

	MoveTo x2,y2// 点击【魂环boss】   坐标1061  374
	Delay delay_time
	LeftClick 1
	Delay delay_time


	// 找颜色
	FindColorEx x3, y3, x4, y4, "1F21C9", 0, 0.9, intX, intY

	If intX < 0 And intY < 0 Then
		If t = 2 Then  // 找到了之后才需要重新进图
			go_back = 1
		End If
    	// 点击进入
    	MoveTo 1679,805    // 点击【立即挑战】  坐标1679 805
		Delay delay_time
		LeftClick 1
		Delay 2000
		Call daguai()
		// 确认全部打完后则点击退出
		MoveTo 2343,436    // 点击【退出】  坐标2343,436
		Delay delay_time
		LeftClick 1
	Else // 没找到则关闭打宝地图界面
		MoveTo 2508, 206// 点击【打宝地图】  坐标2508 206
		Delay delay_time
		LeftClick 1
	End If



End Sub

"""

jinzhuang_button = [1150, 376]
from scripts.func import get_pixel_color, click_mouse, move_and_click, similar_color, capture_screen
from conf import dabaoditu_button, xiyou_button
import time
from log import add_log, get_uuid

def exist():
    # 1128,449  15A128     第三层红点
    # 1128,588  17A229     第四层红点
    point1 = get_pixel_color(1128,588)
    point2 = get_pixel_color(1128,449)

    point3 = get_pixel_color(1128,687)
    point4 = get_pixel_color(1128,548)

    if similar_color(point1, "15A128"):
        return [1128,588]
    elif similar_color(point3, "15A128"):
        return [1128,687]
    elif similar_color(point2, "17A229"):
        return [1128,449]
    elif similar_color(point4, "17A229"):
        return [1128,548]
    else:
        return 0






def run():
    # 打宝地图
    move_and_click(dabaoditu_button[0], dabaoditu_button[1])
    # 稀有
    move_and_click(xiyou_button[0], xiyou_button[1])
    # 金装
    move_and_click(jinzhuang_button[0], jinzhuang_button[1])
    # 判定是否存在
    point = exist()
    if not point:
        print("金装boss不存在，关闭打宝地图")
        move_and_click(1770,320)  # 关闭打宝地图
        return 0

    img = capture_screen()
    img_name = get_uuid()
    img.save(f"E:\\pycharmProject\\yeyou/img/{img_name}.png")
    add_log(f"开始进行金装boss扫图", img_name)
    print(f"金装boss存在，坐标: {point}")
    move_and_click(point[0], point[1])
    # 进入挑战
    move_and_click(1679, 805)  # 点击【立即挑战】
    time.sleep(1)   # 预留一秒的时间进入地图
    color_list = [get_pixel_color(2537,500), get_pixel_color(2537,529), get_pixel_color(2537,558), get_pixel_color(2537,587)]
    # color_list = [get_pixel_color(2547,500), get_pixel_color(2547,529), get_pixel_color(2547,558), get_pixel_color(2547,587)]
    color_list = [[2549, 500], [2549, 529], [2549, 558], [2549,587]]  # 目标boss的坐标
    flag = True
    t = 0  # 设置0.2秒检测一次，如果2分钟后都还存在， 则判定出现问题，默认退出
    while flag and t < 180:
        flag = False
        for i in range(4):
            while similar_color(get_pixel_color(color_list[i][0], color_list[i][1]), "189C26",
                                threshold=30) and t < 180:
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




