from datetime import datetime
from pytz import timezone

data_str = '2026/08/14 07:34:23'
data_format= '%Y/%m/%d %H:%M:%S'


#data = datetime.strptime(data_str,data_format)
data = datetime.now(timezone('Asia/Tokyo'))
print(data)

# print(datetime.now().timestamp())