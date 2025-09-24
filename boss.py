#!/usr/bin/env python
# coding=utf-8
# author:uncleyiba@qq.com
# datetime:2021/5/31 下午3:09
import os, sys, re, json, traceback, time
from sqlalchemy import Column, String, Integer, Text, DateTime, Float
from sql_pool import Base, get_uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import datetime



class QgznBoss(Base):
    # 表名
    __tablename__ = "qgzn_boss"
    __table_args__ = {
        'mysql_charset': 'utf8'
    }
    # 表结构
    type = Column(String(2))   #  boss类型    1 金装 2 魂环 3 神纹 4 绿毒 5 盘龙  6 精英
    map = Column(String(20))   #  地图名称  主要是针对  精英  巫蛊1  巫蛊2
    name = Column(String(20))   #  boss名称
    cd = Column(Integer)   #  boss刷新间隔时间  分钟作为单位
    before = Column(Integer)   # 预计提前进入秒数
    last_time = Column(DateTime)   #  上次击杀完成时间
    next_time = Column(DateTime)   #  下次刷新时间



def update_boss(boss_id):
    """
    添加日志
    :param text: 日志内容
    :param pic_add: 图片地址
    :return:
    """
    from sql_pool import SqlPool
    session = SqlPool.get_session()
    boss = session.query(QgznBoss).filter(QgznBoss.id == boss_id).one()
    boss.last_time = datetime.datetime.now()
    boss.next_time = boss.last_time + datetime.timedelta(minutes=boss.cd)
    session.commit()
    session.close()


def add_boss(type, map, name, cd, before):
    """
    添加日志
    :param text: 日志内容
    :param pic_add: 图片地址
    :return:
    """
    from sql_pool import SqlPool
    session = SqlPool.get_session()
    boss = QgznBoss(
        id=get_uuid(),
        type=type,
        map=map,
        name=name,
        cd=cd,
        before=before,
        last_time=datetime.datetime.now(),
        next_time=datetime.datetime.now() + datetime.timedelta(minutes=cd)
    )
    session.add(boss)
    session.commit()
    session.close()



def get_bosses():
    """
    获取所有boss刷新时间信息
    :return:
    """
    from sql_pool import SqlPool
    session = SqlPool.get_session()
    boss_list = session.query(QgznBoss).order_by(QgznBoss.next_time.desc()).all()
    session.close()
    return boss_list

def get_jingying_boss():
    """
    获取所有精英boss刷新时间信息
    :return:
    """
    from sql_pool import SqlPool
    session = SqlPool.get_session()
    boss_list = session.query(QgznBoss).filter(QgznBoss.type == "6").order_by(QgznBoss.next_time.asc()).all()
    session.close()
    return boss_list



if __name__ == "__main__":
    # from sqlalchemy import create_engine
    # from sql_pool import MYSQL_PORT, MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USER, MYSQL_DATABASE
    #
    # engine = create_engine(
    #     'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
    #         MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE))
    # Base.metadata.create_all(engine)
# boss类型    1 金装 2 魂环 3 神纹 4 绿毒 5 盘龙  6 精英
#     add_boss("1", "jinzhuang0", "金装倒数第二层", 120, 10)
#     add_boss("1", "jinzhuang1", "金装最后一层", 180, 20)
#     add_boss("2", "hunhuan", "魂环", 180, 0)
#     add_boss("3", "shenwen", "神纹(左)", 45, 0)
#     add_boss("3", "shenwen", "神纹(右)", 45, 0)
#     add_boss("5", "panlong", "盘龙", 20, 0)
#
#     boss_list = [
#         [110, 3, 80],
#         [120, 2, 100],
#         [130, 2, 100],
#         [140, 2, 100],
#         [150, 2, 100],
#         [160, 2, 120],
#         [170, 2, 120],
#         [180, 1, 120],
#         [190, 1, 120],
#         [200, 1, 120],
#         [210, 1, 150],
#         [220, 1, 150],
#         [230, 1, 150],
#         [240, 1, 150],
#         [250, 1, 150]
#     ]
#     for each_boss in boss_list:
#         for floor in range(3):
#             name = f"{each_boss[0]}级{floor + 1}层精英"
#             map = f"jingying_{each_boss[0]}_{floor + 1}"
#             if floor >= each_boss[1]:
#                 name += "(跨服)"
#                 map += "_kua"
#             cd = each_boss[2]
#             before = 0
#             add_boss("6", map, name, cd, before)
    boss_list = get_jingying_boss()
    for each in boss_list:
        print(each.id, each.type, each.map, each.name, each.cd, each.before, each.last_time, each.next_time)
    pass
