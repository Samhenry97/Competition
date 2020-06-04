for i in range(int(input())):
    n = int(input())
    grades = [float(input()) for _ in range(n)]
    print('Case {}: {:.3f}'.format(i+1, sum(grades) / n))