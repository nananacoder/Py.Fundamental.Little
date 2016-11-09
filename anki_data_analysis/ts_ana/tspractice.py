import tushare as ts

'''
    code：代码
    date : 交易日期 (index)
    changepercent:涨跌幅
    trade:现价
    open : 开盘价
    high : 最高价
    close : 收盘价
    low : 最低价
    volume : 成交量
    amount : 成交金额
    settlement:昨日收盘价
    turnoverratio:换手率

'''


#一次性获取全部日k线数据
ts.get_hist_data('600848')

#设定历史数据的时间：
ts.get_hist_data('600848', start='2015-01-05', end='2015-01-09')

#
ts.get_hist_data('600848', ktype='W') #获取周k线数据
ts.get_hist_data('600848', ktype='M') #获取月k线数据
ts.get_hist_data('600848', ktype='5') #获取5分钟k线数据
ts.get_hist_data('600848', ktype='15')
ts.get_hist_data('600848', ktype='30')
ts.get_hist_data('600848', ktype='60')


ts.get_hist_data('sh') #获取上证指数k线数据，其它参数与个股一致，下同
ts.get_hist_data('sz')
ts.get_hist_data('hs300')
ts.get_hist_data('sz50')
ts.get_hist_data('zxb')
ts.get_hist_data('cyb')

#获取历史复权数据，分为前复权和后复权数据，接口提供股票上市以来所有历史数据，默认为前复权
df = ts.get_stock_basics()
date = df.ix['600848']['timeToMarket'

#autype:string,复权类型，qfq-前复权 hfq-后复权 None-不复权，默认为qfq
#index:Boolean，是否是大盘指数，默认为False
ts.get_h_data('002337')
ts.get_h_data('002337', autype='hfq')
ts.get_h_data('002337', autype='None')
ts.get_h_data('002337', start='2015-01-01', end='2015-03-16')
ts.get_h_data('002337', index=True)

#一次性获取当前交易所有股票的行情数据（如果是节假日，即为上一交易日，结果显示速度取决于网速）
ts.get_today_all()



#获取个股以往交易历史的分笔数据明细
'''
    time：时间
    price：成交价格
    change：价格变动
    volume：成交手
    amount：成交金额(元)
    type：买卖类型【买盘、卖盘、中性盘】
'''
df = ts.get_tick_data('600848', date='2014-01-09')
df.head(10)

