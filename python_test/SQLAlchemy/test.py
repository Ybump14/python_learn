from python_learn.python_test.SQLAlchemy.Enum import OsType, FirmwareType, DeviceModel, UpgradeState
from python_learn.python_test.SQLAlchemy.data import ORM
from python_learn.python_test.SQLAlchemy.model.test import Demo
from python_learn.python_test.SQLAlchemy.upgradeData import base_query

db = ORM('test')

queryData = base_query(OsType.IOS.value, FirmwareType.ARM.value, DeviceModel.AC200M.value)
old_queryDate = queryData.copy()
old_queryDate.append(Demo.creTime <= "2021-12-11 00:00:00")

old_ios_query_count = old_queryDate.copy()

old_ios_query_count_suc = old_ios_query_count.copy()
old_ios_query_count_suc.append(Demo.upgradeState == UpgradeState.SUCCESS.value)

old_ios_query_count = db.filter(Demo, *queryData).count()
old_ios_query_count_suc = db.filter(Demo, *old_ios_query_count_suc).count()
old_ios_query_count_fail = old_ios_query_count - old_ios_query_count_suc
print(old_ios_query_count)
print(old_ios_query_count_suc)
print(old_ios_query_count_fail)

new_queryDate = queryData.copy()
new_queryDate.append(Demo.creTime >= "2021-12-11 00:00:00")

new_ios_query_count = new_queryDate.copy()

new_ios_query_count_suc = new_ios_query_count.copy()
new_ios_query_count_suc.append(Demo.upgradeState == UpgradeState.SUCCESS.value)

new_ios_query_count = db.filter(Demo, *new_ios_query_count).count()
new_ios_query_count_suc = db.filter(Demo, *new_ios_query_count_suc).count()
new_ios_query_count_fail = new_ios_query_count - new_ios_query_count_suc
print(new_ios_query_count)
print(new_ios_query_count_suc)
print(new_ios_query_count_fail)
