#!/usr/bin/env python3
from datetime import timedelta, datetime
from time import strftime

deltaAfter = (360 / 60 / 60) - (360 / 12 / 60 / 60)
deltaBefore = - (360 / 60 / 60) + (360 / 12 / 60 / 60)
for line in open(__import__('sys').argv[1], 'r'):
	deg, dir, hour = line.split()
	deg, hour = float(deg), int(hour)
	ang = (360.0 - 360.0 * (hour / 12.0))
	if dir == 'after':
		if ang > deg: deg += 360
		x = round((deg - ang) / deltaAfter)
		ans = datetime(1997, 5, 5, hour=hour, minute=0, second=0) + timedelta(seconds=x)
	else:
		print(deg, ang)
		if ang < deg: ang += 360
		x = round(abs(deg - ang) / deltaBefore)
		ans = datetime(1997, 5, 5, hour=hour, minute=0, second=0) + timedelta(seconds=x)
	ans = ans.time()
	hour = ans.hour % 12
	if hour == 0: hour = 12
	print('{}:{}:{}'.format(hour, str(ans.minute).ljust(2, '0'), str(ans.second).ljust(2, '0')))