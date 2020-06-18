def seq(t, n):
    return ((t // n) * (n + (t - (t % n)))) >> 1

for _ in range(int(input())):
    t = int(input()) - 1
    print(seq(t, 3) + seq(t, 5) - seq(t, 15))