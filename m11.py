import math

data = []
ans = []

with open("Testcase4.txt", "r") as file:
    x = 0
    l = 0

    for line in file:
        l += 1
        for i in line:
            if '0' <= i <= '9':
                x = x * 10 + int(i)
        
        data.append(x)
        print(f"x={x}")
        x = 0

        if l == 3:
            break

d = data[0] / (data[1]-1)
r = data[0] / 2

a = r * math.cos(math.radians(data[2]))
b = r * math.sin(math.radians(data[2]))
m = b / a

while data[1] > 0:
    ans.append((a, b))
    r -= d
    a = r * math.cos(math.radians(data[2]))
    b = r * math.sin(math.radians(data[2]))
    if b == -0:
        b = 0
    data[1] -= 1

with open("result.txt", "a") as wfile:
    for i in ans:
        wfile.write(f"({i[0]:.4f},{i[1]:.4f})\n")
