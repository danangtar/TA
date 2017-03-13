v = 0
m = 128
b = 0
vtemp = 2 * v + b
print(abs(vtemp))
print(2 * (255 - m))
if 128<=m<=255:
    if abs(vtemp) <= 2 * (255 - m):
        print("ok")