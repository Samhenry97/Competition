for _ in range(int(input())):
    input()
    n = int(input())
    print(['NO', 'YES'][sum([int(input()) for _ in range(n)]) % n == 0])