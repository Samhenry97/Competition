from math import sqrt

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def contains(self, x, y):
        return self.x1 <= x and self.x2 >= x and self.y1 <= y and self.y2 >= y

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def contains(self, x, y):
        dist = sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
        return dist <= self.r

sCount = int(input())
shapes = []

for _ in range(sCount):
    l = list(input().split())
    if l[0] == 'rectangle':
        shapes.append(Rectangle(int(l[1]), int(l[2]), int(l[3]), int(l[4])))
    else:
        shapes.append(Circle(int(l[1]), int(l[2]), int(l[3])))

points = int(input())
for _ in range(points):
    x, y = map(int, input().split())
    containCount = 0
    for i in range(len(shapes)):
        if shapes[i].contains(x, y):
            containCount += 1
    print(containCount)
