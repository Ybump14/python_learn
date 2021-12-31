from python_learn.python_test.SQLAlchemy.model.test import Demo


def base_query(os, firmware, deviceModel):
    return [Demo.os == os, Demo.firmwareType == firmware,
            Demo.deviceModel == deviceModel]
