for _ in range(int(input())):
    input()
    input()
    a = max(list(map(int, input().split())))
    b = max(list(map(int, input().split())))
    print(['Godzilla', 'MechaGodzilla'][b > a])