import os
import number as num

from number import factorial
from math import factorial as math_factorial
from datetime import time, datetime


x = factorial(5)
# 120

x = num.factorial(5)
# 120

x = math_factorial(5)
# 120

t = time()
# datetime.time(0, 0)

datetime_now = datetime.now()
# datetime.datetime(2022, 10, 13, 21, 24, 19, 873596)

#----------------------------------------

# Using the dir() Function
dir_num = dir(num)
print(dir_num)
