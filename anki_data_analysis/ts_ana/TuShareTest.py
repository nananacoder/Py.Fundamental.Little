import tushare as ts

print("------------DaPan ZhiShu---------------")
index = ts.get_index()
print(index)
print("------------DaPan ZhiShu-change desc---------------")
print(index.sort('change',ascending=False))
print("------------DaPan ZhiShu-change<-3---------------")
print(index[index.change<-3])

print("------------ShangZheng---------------")
sh = ts.get_hist_data('sh',start='2016-01-11',end='2016-01-13')
print(sh)

print("------------HS300---------------")
hs300 = ts.get_hist_data('hs300',start='2016-01-11',end='2016-01-13')
print(hs300)
       
print("------------ZhongXiaoBan ZhiShu---------------")
zxb = ts.get_hist_data('zxb',start='2016-01-11',end='2016-01-13')
print(zxb)

print("------------ChuangYeBan ZhiShu---------------")
cyb = ts.get_hist_data('cyb',start='2016-01-11',end='2016-01-13')
print(cyb)

print("------------ChuangYeBan-Week K---------------")
cybWW = ts.get_hist_data('cyb',start='2015-12-12',end='2016-01-13',ktype='W')
print(cybWW)

print("------------ChuangYeBan-60min K---------------")
cyb60 = ts.get_hist_data('cyb',start='2016-01-11',end='2016-01-13',ktype='60')
print(cyb60)

print("------------ChuanTouNengYuan---------------")
stockCTNY = ts.get_hist_data('600674',start='2016-01-11',end='2016-01-13')
print(stockCTNY)

#------------DaZuo Model--------------------------------------
print("------------HS300---------------")
hs300 = ts.get_hist_data('hs300',start='2016-01-11',end='2016-01-13')
print(hs300)
       
print("------------ZhongGuoPingAn---------------")
stockZGPA = ts.get_hist_data('601318',start='2016-01-11',end='2016-01-13')
print(stockZGPA)

print("------------QianYuanDianLi---------------")
stockQYDL = ts.get_hist_data('002039',start='2016-01-11',end='2016-01-13')
print(stockQYDL)

print("------------ChuanTouNengYuan---------------")
stockCTNY = ts.get_hist_data('600674',start='2016-01-11',end='2016-01-13')
print(stockCTNY)

print("------------GuoTouDianLi---------------")
stockGTDL = ts.get_hist_data('600886',start='2016-01-11',end='2016-01-13')
print(stockGTDL)


# print("------------Save as XLS file---------------")
# stockGTDL.to_excel('GTDL.xlsx')
# stockGTDL.to_excel('c:/day/000875.xlsx', startrow=2,startcol=5)


