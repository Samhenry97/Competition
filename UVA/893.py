from datetime import datetime, timedelta

delta, d, m, y = map(int, input().split())
while delta or d or m or y:
	date = datetime.strptime('{} {} {}'.format(d, m, y), '%d %m %Y')
	date += timedelta(days=delta)
	print(datetime.strftime(date, '%d %m %Y').lstrip('0').replace(' 0', ' '))

	delta, d, m, y = map(int, input().split())