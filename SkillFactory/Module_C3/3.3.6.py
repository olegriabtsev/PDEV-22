import time

i = 10
while i in range(i, -1, -1):
    print(i)
    time.sleep(1)
    i -= 1
print('Time is over!')
