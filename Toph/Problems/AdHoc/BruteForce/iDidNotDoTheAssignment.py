n = int(input())
prime = True
for i in range(2, n):
    if n % i == 0:
        prime = False
        break
if prime:
    print('NO PUNISHMENT')
else:
    print('\n'.join(['I DID NOT DO THE ASSIGNMENT.'] * n))