from enum import Enum, unique


@unique
class UpgradeState(Enum):
    SUCCESS = 'success'


@unique
class OsType(Enum):
    ANDROID = 2
    IOS = 3


@unique
class DeviceModel(Enum):
    EP500 = 'EP500'
    EP500P = 'EP500P'
    AC300 = 'AC300'
    AC200M = 'AC200M'


@unique
class FirmwareType(Enum):
    IOT = 0
    ARM = 1
    DSP = 2
    BMS = 3
