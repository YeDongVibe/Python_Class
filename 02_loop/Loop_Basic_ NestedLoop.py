#구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")

#별문자로 모양 그리기
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end="")
    print()

for i in range(4, 0, -1):
    for j in range(1, i+1):
        print("*", end="")
    print()
