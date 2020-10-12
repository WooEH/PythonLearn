rec_now = int(input())
now_min = rec_now / 100
now_sec = rec_now % 100

rec_std = int(input())
std_min = rec_std / 100
std_sec = rec_std % 100

if std_sec > now_sec:
    now_sec += 60

res_min = now_min - std_min
res_sec = now_sec - std_sec

if res_sec >= 60:
    res_min += 1
    res_sec -= 60

print("%dm %ds" %(res_min, res_sec))

