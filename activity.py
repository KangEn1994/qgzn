#!/usr/bin/env python
# coding=utf-8
# author:uncleyiba@qq.com
# datetime:2021/5/31 下午3:09
import os, sys, re, json, traceback, time
from sqlalchemy import Column, String, Integer, Text, DateTime, Float, Time
from sql_pool import Base, get_uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import datetime



class QgznActivity(Base):
    # 表名
    __tablename__ = "qgzn_activity"
    __table_args__ = {
        'mysql_charset': 'utf8'
    }
    # 表结构
    start_time = Column(Time, nullable=False)  # 活动开始时间  例如 100000
    name = Column(String(64), nullable=False)  # 活动名称
    flag = Column(Integer, nullable=False, default=0)  # 是否已执行  0 未执行  1 已执行    2暂停
    script_name = Column(String(64), nullable=False)  # 执行的脚本名称



def update_activity(activity_id, flag):
    from sql_pool import SqlPool
    session = SqlPool.get_session()
    activity = session.query(QgznActivity).filter(QgznActivity.id == activity_id).one()
    activity.flag = flag
    session.commit()
    session.close()

def init_activity():
    from sql_pool import SqlPool
    session = SqlPool.get_session()
    activities = session.query(QgznActivity).filter(QgznActivity.flag < 2).order_by(QgznActivity.start_time).all()
    now_time = datetime.datetime.now().time()
    for e in activities:
        if e.start_time > now_time:
            e.flag = 0
        else:
            e.flag = 1

    session.commit()
    session.close()

def add_activity(start_time, name, script_name):
    """
    添加活动
    :param start_time: 活动开始时间  例如 100000
    :param name: 活动名称
    :param script_name: 执行的脚本名称
    :return:
    """
    from sql_pool import SqlPool
    session = SqlPool.get_session()
    activity = QgznActivity(id=get_uuid(), start_time=start_time, name=name, script_name=script_name, flag=0)
    session.add(activity)
    session.commit()
    session.close()

def del_activity(activity_id):
    """
    删除活动
    :param activity_id: 活动ID
    :return:
    """
    from sql_pool import SqlPool
    session = SqlPool.get_session()
    activity = session.query(QgznActivity).filter(QgznActivity.id == activity_id).one()
    session.delete(activity)
    session.commit()
    session.close()


def get_todo_activities():
    """
    获取所有活动
    :return:
    """
    from sql_pool import SqlPool
    session = SqlPool.get_session()
    activities = session.query(QgznActivity).filter(QgznActivity.flag == 0).order_by(QgznActivity.start_time).all()
    session.close()
    return activities


def get_all_activities():
    """
    获取所有活动
    :return:
    """
    from sql_pool import SqlPool
    session = SqlPool.get_session()
    activities = session.query(QgznActivity).order_by(QgznActivity.start_time).all()
    session.close()
    return activities


if __name__ == "__main__":
    # from sqlalchemy import create_engine
    # from sql_pool import MYSQL_PORT, MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USER, MYSQL_DATABASE
    #
    # engine = create_engine(
    #     'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
    #         MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE))
    # Base.metadata.create_all(engine)
    # 将日期格式转换成datatiem
    # dt = datetime.datetime.strptime("2023-10-01 10:00:00", "%Y-%m-%d %H:%M:%S")
    # 10:00  虎牢
    # 11:00  魔神
    # 15:15  竞技场5次
    # 15:30  虎牢
    # 16:30  押镖
    # 20:80  蓬莱or虚星
    # add_activity(datetime.time(10,10,0), "血战虎牢", "xuezhan")
    # add_activity(datetime.time(11,0,0), "魔神", "moshen")
    # add_activity(datetime.time(15,15,0), "竞技场", "jingjichang")
    # add_activity(datetime.time(15,30,0), "血战虎牢", "xuezhan")
    # add_activity(datetime.time(16,30,0), "押镖", "yabiao")
    # add_activity(datetime.time(20,40,0), "蓬莱", "penglai")
    # add_activity(datetime.time(10, 5, 0), f"魂环", "hunhuan")
    # add_activity(datetime.time(14, 10, 0), f"魂环", "hunhuan")
    #
    # add_activity(datetime.time(18, 15, 0), f"魂环", "hunhuan")
    # add_activity(datetime.time(22, 20, 0), f"魂环", "hunhuan")

    # add_activity(datetime.time(10, 20, 0), f"巫蛊禁地", "wugujindi")
    # add_activity(datetime.time(11, 30, 0), f"巫蛊禁地", "wugujindi")
    # add_activity(datetime.time(12, 40, 0), f"巫蛊禁地", "wugujindi")
    # add_activity(datetime.time(13, 50, 0), f"巫蛊禁地", "wugujindi")
    # add_activity(datetime.time(14, 55, 0), f"巫蛊禁地", "wugujindi")
    # add_activity(datetime.time(16, 20, 0), f"巫蛊禁地", "wugujindi")
    # add_activity(datetime.time(17, 30, 0), f"巫蛊禁地", "wugujindi")
    # add_activity(datetime.time(18, 40, 0), f"巫蛊禁地", "wugujindi")
    # add_activity(datetime.time(19, 50, 0), f"巫蛊禁地", "wugujindi")
    # add_activity(datetime.time(20, 55, 0), f"巫蛊禁地", "wugujindi")
    # add_activity(datetime.time(12, 30, 1), f"关闭科举弹窗", "special1230")








    # for i in range(60):
    #     add_activity(datetime.time(8 + i // 4, (i % 4) * 15, 0), f"挂机{i+1}", "guaji")
    # del_activity("7c359b63a92044cc94aa098349fea3f1")

    l = get_all_activities()
    for e in l:
        if "禁地" in e.name:
            print(e.id, e.start_time, e.name, e.script_name, e.flag)
    #         del_activity(e.id)

