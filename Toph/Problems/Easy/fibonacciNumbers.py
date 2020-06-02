n = int(input())
fib = [1, 1]
for i in range(2, n):
    fib.append(fib[i-2] + fib[i-1])
print(fib[-1])