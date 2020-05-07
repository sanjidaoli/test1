import  time

# print(time.time())
# print(time.asctime())
# print(time.localtime())
# time.strftime
now_time=time.time()
before_twoday=now_time-60*60*24*2
after_threeday=now_time+60*60*24*3
time_tuple=time.localtime(before_twoday)
time_after=time.localtime(after_threeday)
print(time.strftime("%Y-%m-%d %H-%M-%S", time_tuple))
print(time.strftime("%Y-%m-%d %H-%M-%S", time_after))