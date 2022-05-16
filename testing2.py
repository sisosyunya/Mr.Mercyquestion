first = 1
second = 1
total = []
result =0
while True:
    print(first)
    total.append(first)
    first += second
    print(second)
    total.append(second)
    second +=first
for s in range(len(total)):
    result += total[s]
print(total)
print("結果は"+str(result))