from bisect import bisect_left

fib = [1, 2]
ans = [2]
pref = [2]
while fib[-1] < 4 * 10**16:
    fib.append(fib[-1] + fib[-2])
    if fib[-1] % 2 == 0:
        ans.append(fib[-1])
        pref.append(fib[-1] + pref[-1])

for _ in range(int(input())):
    print(pref[bisect_left(ans, int(input()))-1])