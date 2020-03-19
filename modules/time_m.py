import time
from datetime import time as dt_time


# print((time.localtime()))

now = time.strftime("%d/%m/%Y - %H:%M:%S", time.localtime())
print(now)