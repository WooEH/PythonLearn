s = [8, 6, 9, 10, 4, 7, 10, 6, 8, 7]
max = s[0]
idx = 0

print("s =", s, sep="")

for i in range(len(s)):
    if s[i] > max:
        max = s[i]
        idx = i

print("Max = %d" % max)
print("Idx = %d" % idx)