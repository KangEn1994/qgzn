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

"""
run   0 运行中    1 暂停



"""
RUN_ING = "0"
RUN_OVER = "1"

class QgznKey(Base):
    # 表名
    __tablename__ = "qgzn_key"
    __table_args__ = {
        'mysql_charset': 'utf8'
    }
    # 表结构
    name = Column(String(64), nullable=False)  # key名字
    value = Column(String(64), nullable=False)  # key值

    def __str__(self):
        return f"QgznKey(id={self.id}, name={self.name}, value={self.value})"



def update_key(name, value):
    from sql_pool import SqlPool
    session = SqlPool.get_session()
    key = session.query(QgznKey).filter(QgznKey.name == name).one()
    key.value = value
    session.commit()
    session.close()


def add_key(name, value):
    from sql_pool import SqlPool
    session = SqlPool.get_session()
    key = QgznKey(id=get_uuid(), name=name, value=value)
    session.add(key)
    session.commit()
    session.close()

def get_key(name):
    """
    获取key
    :return:
    """
    from sql_pool import SqlPool
    session = SqlPool.get_session()
    key = session.query(QgznKey).filter(QgznKey.name == name).first()
    session.close()
    return key




if __name__ == "__main__":
    # from sqlalchemy import create_engine
    # from sql_pool import MYSQL_PORT, MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USER, MYSQL_DATABASE
    #
    # engine = create_engine(
    #     'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
    #         MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE))
    # Base.metadata.create_all(engine)

    # add_key("run", "0")
    print(get_key("run"))
