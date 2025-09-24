#!/usr/bin/env python
# coding=utf-8
# author:uncleyiba@qq.com
# datetime:2021/5/31 下午3:09
import os, sys, re, json, traceback, time
from sqlalchemy import Column, String, Integer, Text, DateTime, Float
from sql_pool import Base, get_uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship



class QgznLog(Base):
    # 表名
    __tablename__ = "qgzn_log"
    __table_args__ = {
        'mysql_charset': 'utf8'
    }
    # 表结构
    text = Column(String(100))   #  日志内容
    pic_add = Column(String(100))   #  图片地址


def add_log(text, pic_add=""):
    """
    添加日志
    :param text: 日志内容
    :param pic_add: 图片地址
    :return:
    """
    from sql_pool import SqlPool
    session = SqlPool.get_session()
    log = QgznLog(id=get_uuid(),text=text, pic_add=pic_add)
    session.add(log)
    session.commit()
    session.close()

def get_logs(num=100):
    """
    获取日志
    :return:
    """
    from sql_pool import SqlPool
    session = SqlPool.get_session()
    logs = session.query(QgznLog).order_by(QgznLog.create_time.desc()).limit(num).all()
    # logs = session.query(QgznLog).filter(QgznLog.text.like("%不在目标地图%")).order_by(QgznLog.create_time.desc()).all()
    session.close()
    return logs




if __name__ == "__main__":
    # from sqlalchemy import create_engine
    # from sql_pool import MYSQL_PORT, MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USER, MYSQL_DATABASE
    #
    # engine = create_engine(
    #     'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
    #         MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE))
    # Base.metadata.create_all(engine)

    # import datetime
    # from route.service.database.sql_pool import SqlPool
    #
    # session = SqlPool.get_session()
    # doc_type = Doc(doc_uuid="1.pdf", task_id=4, labeling_result="{}",
    #                    create_time=datetime.datetime.now(),
    #                    update_time=datetime.datetime.now())
    # session.add(doc_type)
    # session.commit()
    # session.close()
    # add_log("1","2")
    from sql_pool import SqlPool

    session = SqlPool.get_session()
    logs = session.query(QgznLog).order_by(QgznLog.create_time.desc()).limit(200)     #.filter(QgznLog.text.like("%押镖%")).order_by(QgznLog.create_time.desc()).all()
    session.close()
    for each in logs:
        print(each.text, each.pic_add, each.create_time)
