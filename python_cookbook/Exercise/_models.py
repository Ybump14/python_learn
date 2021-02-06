from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def sql_connect():
    # 创建数据库连接
    engine = create_engine("mysql://root:root@localhost:3306/test?charset=utf8", encoding='utf-8')
    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)
    # 创建session对象
    session = DBSession()
    Base.metadata.create_all(engine)
    return session


Base = declarative_base()


class SpiderDouban(Base):
    __tablename__ = 'spiderdouban'

    id = Column(Integer, primary_key=True)
    url = Column(String(255))
    title_chinese = Column(String(255))
    title_others = Column(String(255))
    director = Column(String(255))
    year = Column(String(255))
    country = Column(String(255))
    classify = Column(String(255))
    rating_num = Column(String(255))
    rating_people = Column(String(255))
    quote = Column(String(255))
