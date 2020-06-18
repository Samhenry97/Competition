facts = [0, 1, 2]
for i in range(3, 101):
    facts.append(i * facts[-1])
    
for _ in range(int(input())):
    print(facts[int(input())]) 