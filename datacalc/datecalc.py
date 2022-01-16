# import time
#
# print(time.gmtime(0))
#
# time_here = time.localtime()
# print(time_here)
# print("year:", time_here[0], time_here.tm_year)

import time
from time import monotonic as my_timer
import random

input("Please enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Please enter to stop")

end_time = my_timer()

print("Started at " + time.strftime("%x", time.localtime(start_time)))
print("End at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))