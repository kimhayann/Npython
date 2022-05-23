total = 0
counter = 1
while counter <= 10:
    grad = int(input("점수 입력: "))
    total = grad + total
    counter = counter + 1
aver = total / 5
print(total)
print(aver)