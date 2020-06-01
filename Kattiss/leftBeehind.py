a, b = map(int, input().split())

while(a or b):
    if a + b == 13:
        print("Never speak again.")
    elif a > b:
        print("To the convention.")
    elif a < b:
        print("Left beehind.")
    else:
        print("Undecided.")

    a, b = map(int, input().split())
