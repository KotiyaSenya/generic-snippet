from datetime import date, datetime, timedelta
from typing import List, Tuple, Union


class DateUtil:
    def __init__(self, special_time=None):
        self.special_time = special_time if special_time else datetime.now()

    def today(self):
        return self.special_time.date()

    def yesterday(self):
        return self.special_time.date() - timedelta(days=1)

    def week_start(self):
        week_day = self.special_time.isoweekday()
        return self.special_time.date() - timedelta(days=(week_day - 1))

    def week_end(self):
        return self.week_start() + timedelta(days=6)

    def month_start_day(self):
        return date(year=self.special_time.year, month=self.special_time.month, day=1)

    def month_end_day(self):
        return self.next_month_start_day() - timedelta(days=1)

    def next_month_start_day(self):
        if self.special_time.month == 12:
            next_month_start_day = date(year=(self.special_time.year + 1), month=1, day=1)
        else:
            next_month_start_day = date(year=self.special_time.year, month=self.special_time + 1, day=1)
        return next_month_start_day


def get_previous_months(key_date, limit=5, include_current=True, desc=True) -> List[Tuple['date', 'date']]:
    """
    获取之前月份范围
    :param key_date: 判断基准日期
    :param limit: 返回之前`limit`个月
    :param include_current: 返回值是否包含本月
    :param desc: 是否降序排列, 越靠近的排在前面
    """
    month_list = []
    if include_current:
        month_list = [get_current_month_range(key_date)]
    for i in range(limit):
        last_month_start, last_month_end = get_last_month_range(key_date)
        month_list.append((last_month_start, last_month_end))
        key_date = last_month_start
    if not desc:
        month_list.reverse()
    return month_list


def get_last_month_range(key_date: Union['date', 'datetime']) -> Tuple['date', 'date']:
    """获取上月范围"""
    last_month_start = get_last_month_start(key_date)
    last_month_end = date(key_date.year, key_date.month, 1) - timedelta(days=1)
    return last_month_start, last_month_end


def get_last_month_start(key_date: Union['date', 'datetime']):
    """获取上月开始日期"""
    if key_date.month == 1:
        last_month_start = date(key_date.year - 1, 12, 1)
    else:
        last_month_start = date(key_date.year, key_date.month - 1, 1)
    return last_month_start


def get_next_month_start(key_date: Union['date', 'datetime']) -> 'date':
    """获取下月开始日期"""
    if key_date.month == 12:
        next_month_start = date(key_date.year + 1, 1, 1)
    else:
        next_month_start = date(key_date.year, key_date.month + 1, 1)
    return next_month_start


def get_next_month_range(key_date: Union['date', 'datetime']) -> Tuple['date', 'date']:
    """获取下月范围"""
    next_month_start = get_next_month_start(key_date)
    next_month_end = get_next_month_start(next_month_start) - timedelta(days=1)
    return next_month_start, next_month_end


def get_current_month_range(key_date: Union['date', 'datetime']) -> Tuple['date', 'date']:
    """获取当前月范围"""
    month_start = date(key_date.year, key_date.month, 1)
    month_end = get_next_month_start(key_date) - timedelta(days=1)
    return month_start, month_end


if __name__ == '__main__':
    months = get_previous_months(datetime.now())
    print(months)
