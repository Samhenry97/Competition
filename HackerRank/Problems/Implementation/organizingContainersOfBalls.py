for _ in range(int(input())):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    gr = list(zip(*g))
    cont = sorted(sum(row) for row in g)
    ball = sorted(sum(row) for row in gr)
    print(['Impossible', 'Possible'][cont == ball])