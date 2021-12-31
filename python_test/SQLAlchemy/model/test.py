from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime

Base = declarative_base()


class Demo(Base):
    __tablename__ = "demo"

    id = Column(Integer, primary_key=True)
    os = Column(Integer)
    deviceModel = Column(String)
    upgradeState = Column(String)
    firmwareType = Column(String)
    creTime = Column(DateTime)

    def __repr__(self):
        return '<Test(id=%s,os=%s,deviceModel=%s,upgradeState=%s,firmwareType=%s,creTime=%s)>' % (
            self.id, self.os, self.deviceModel, self.upgradeState, self.firmwareType, self.creTime)
