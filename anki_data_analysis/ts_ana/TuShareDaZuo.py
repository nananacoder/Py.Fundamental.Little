import tushare as ts
import datetime


print("------------ShangZheng---------------")
daystart = datetime.datetime.now().strftime("%Y-%m-%d")
print(daystart)
# today = datetime.date.today()
today = datetime.datetime.now()
print(today)
day7ago = today - datetime.timedelta(days=7)
print(day7ago)

# sh = ts.get_hist_data('sh',start=today.strftime('%Y-%m-%d'),end=today.strftime('%Y-%m-%d'))
sh = ts.get_hist_data('sh',start='2016-03-10',end='2016-03-14')
# print(sh)
print(sh[['close']])


