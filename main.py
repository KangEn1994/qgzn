from scripts import jinzhuang, shenwen, penglai, guaji, hunhuan, bozhuangyuan, wuguzaoze, moshen, yabiao, xuezhan, jingjichang, shene, special, shijieboss, panlong, hefumowang, zhengzhantianxia, wugujindi, special1230
from activity import get_todo_activities, get_all_activities, add_activity, update_activity, init_activity
import time, datetime, traceback
from scripts import func
from key import get_key, update_key, add_key, RUN_ING, RUN_OVER
from log import add_log, get_uuid
from scripts.func import move_and_click



"""
# 2.0的核心宗旨
参与的活动：  
    10:00  虎牢
    11:00  魔神
    15:15  竞技场5次
    15:30  虎牢
    16:30  押镖
    20:80  蓬莱or虚星
其他时间活动
    挂精英boss
    点击博状元  同时作为延时手段
    打神纹boss
    绿毒boss
远程手动
    攻城
人工手动
    其他任务
"""
def run():
    func.jietu("脚本开始执行")
    try:
        # global boo, over
        # over = False
        boo = get_key("run").value
        init_activity()

        while boo == RUN_ING:
            now_time = datetime.datetime.now().time()
            # 判定是否有活动需要执行
            activities = get_todo_activities()
            if activities and now_time > activities[0].start_time:
                # 执行活动
                activity = activities[0]
                script_cnd = f"{activity.script_name}.run()"
                func.jietu("执行活动：" + activity.name)
                func.close_tanchuang()  # 关闭龙纹掉落识别
                func.exit_map()   # 退出当前地图
                eval(script_cnd)   # 执行脚本
                time.sleep(2)
                update_activity(activity.id, 1)   # 更新活动状态为已完成
                # guaji.run()
            # 不执行活动，执行挂机  理论上当前应该就在挂机状态
            guaji.run()
            boo = get_key("run").value
        # over = True

    except:
        # over = True
        func.jietu(f"脚本执行异常，结束{traceback.format_exc()}")
        # boo = False
        update_key("run", RUN_OVER)
    func.jietu("脚本结束执行")





