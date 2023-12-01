from test_3 import sum_current_time


def test_sum_time_simple_one():
    assert sum_current_time('12:13:14') == 39


def test_sum_time_simple_two():
    assert sum_current_time('17:04:09') == 30


def test_sum_time_one_leading_zero():
    assert sum_current_time('03:14:15') == 32


def test_sum_time_two_leading_zero():
    assert sum_current_time('03:14:05') == 22


def test_sum_time_three_leading_zero():
    assert sum_current_time('03:04:05') == 12


def test_sum_time_invalid_hour_1():
    assert sum_current_time('99:01:01') == None


def test_sum_time_invalid_hour_2():
    assert sum_current_time('24:01:01') == None


def test_sum_time_invalid_minute_1():
    assert sum_current_time('01:99:01') == None


def test_sum_time_invalid_minute_2():
    assert sum_current_time('01:60:01') == None


def test_sum_time_invalid_second_1():
    assert sum_current_time('01:01:99') == None


def test_sum_time_invalid_second_2():
    assert sum_current_time('01:01:60') == None
