import datetime
import time
def get_day_nday_ago(date,n):
    t = time.strptime(date, "%Y-%m-%d")
    y, m, d = t[0:3]
    Date = str(datetime.datetime(y, m, d) - datetime.timedelta(n)).split()
    return Date[0]
def get_nday_list(date,n):
    import datetime
    before_n_days = []
    t = time.strptime(date, "%Y-%m-%d")
    y, m, d = t[0:3]
    for i in range(1, n + 1)[::-1]:
        before_n_days.append(str(datetime.datetime(y, m, d) - datetime.timedelta(days=i)).split(' ')[0])
    return before_n_days
# 示例
# a=get_day_nday_ago('2017-02-11',7)
