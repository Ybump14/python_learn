from datetime import datetime, timedelta

import pytest


@pytest.mark.parametrize(
    "a,b,expected",
    [
        pytest.param(
            datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1), id="forward"
        ),
        pytest.param(
            datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1), id="backward"
        ),
    ],
)
def test_timedistance_v3(a, b, expected):
    diff = a - b
    print(a)
    print(b)
    print(expected)
    assert diff == expected


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    print(x, y)


def setup_module():
    print('\n====初始化模块====')


def teardown_module():
    print('\n====清除模块====')


class TestDemo01():
    def setup_class(self):
        print('\n====初始化类====')

    def teardown_class(self):
        print('\n====清除类====')

    def setup_method(self):
        print('\n====初始化方法====')

    def teardown_method(self):
        print('\n====清除方法====')

    def test_101(self):
        print("\n测试用例test_101执行")
        assert 1 == 1

    def test_102(self):
        print("\n测试用例test_102执行")
        assert 1 == 1

    def test_103(self):
        print("\n测试用例test_103执行")
        assert 1 == 1
