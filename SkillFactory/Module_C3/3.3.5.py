import time

seconds = time.time()
print(seconds)
print('---')
local_time = time.ctime(seconds)
# time.sleep(2.4)
print('Local time:', local_time)
print()
named_tuple = time.localtime()
time_string = time.strftime('%m/%d/%Y, %H:%M:%S', named_tuple)
print(time_string)






