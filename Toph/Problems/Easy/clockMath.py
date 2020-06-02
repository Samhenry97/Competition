h, m = map(int, input().split())
h = (h/12)*360 + m/60*1/12*360
m = (m/60)*360
ans = abs(h-m)
ans = min(ans, 360-ans)
print(ans)