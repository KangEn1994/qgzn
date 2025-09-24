#!/usr/bin/env python
# coding=utf-8
# author: uncleyiba@qq.com
# datetime:2020-11-20 15:09
import os, sys, re, json, traceback, time
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base
import _locale
from sqlalchemy import Column, String, Integer, Text, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

import _locale, datetime

_locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_DATABASE = "game"


# 创建对象的基类:
DeclarativeBase = declarative_base()
from uuid import uuid4 as uuid

def get_uuid():
    """
    获取一个uuid，去除了'-'
    :return:
    """
    return str(uuid()).replace("-", "")

class Base(DeclarativeBase):
    __abstract__ = True
    DEL_NORMAL = 0
    DEL_DELETE = 1
    id = Column(String(64), primary_key=True)  # id使用uuid方便进行数据的迁移
    remark = Column(Text())  # 备注
    del_flag = Column(String(1), default="0")   # 删除标记  0正常   1删除
    create_by = Column(String(64))  # 创建者ID
    create_time = Column(DateTime(), default=datetime.datetime.now)  # 创建时间
    update_by = Column(String(64))  # 修改者ID
    update_time = Column(DateTime(), default=datetime.datetime.now)  # 修改时间





class SqlPool:
    engine = create_engine(
        "mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8".format(
            MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE),
        max_overflow=10,  # 超过连接池大小外最多创建的连接
        pool_size=20,  # 连接池大小
        pool_timeout=20,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=0.5 * 60  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
    SessionFactory = sessionmaker(bind=engine)

    @staticmethod
    def get_session():
        return scoped_session(SqlPool.SessionFactory)

    @staticmethod
    def create_all():
        Base.metadata.create_all(SqlPool.engine)


if __name__ == "__main__":
    for i in range(19):
        print(id(SqlPool.get_session()))
