a, b, c = map(int, input().split())
while a or b or c:
    diff = b - a
    mult = b // a if a != 0 else -1
    if diff != 0 and b + diff == c:
        print('AP', c + diff)
    elif b * mult == c:
        print('GP', c * mult)
    
    a, b, c = map(int, input().split()) 