import datetime as dtm
import time

print dtm.datetime.now()
print dtm.datetime.today()

dt = dtm.datetime.now()
print dt.strftime('%y-%m-%d')
print dt.strftime('%y/%m/%d')
print dt.strftime('%y %m %d')

print dt.strftime('%y-%b-%d')
print dt.strftime('%y/%b/%d')
print dt.strftime('%y %b %d')

print time.time()
