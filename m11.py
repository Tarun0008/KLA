import math

dt = []
result = []

with open("Testcase4.txt", "r") as file:
    c = 0
    l = 0

    for line in file:
        l += 1
        for i in line:
            if '0' <= i <= '9':
                c = c * 10 + int(i)
        
        dt.append(c)
        print(f"c={c}")
        c = 0

        if l == 3:
            break

d = dt[0] / dt[1]
r = dt[0] / 2

a = r * math.cos(math.radians(dt[2]))
b = r * math.sin(math.radians(dt[2]))
m = b / a

while dt[1] > 0:
    result.append((a, b))
    r -= d
    a = r * math.cos(math.radians(dt[2]))
    b = r * math.sin(math.radians(dt[2]))
    if b == -0:
        b = 0
    dt[1] -= 1

with open("result.txt", "a") as wfile:
    for i in result:
        wfile.write(f"({i[0]:.4f},{i[1]:.4f})\n")
