import operator
from PIL import Image

i1 = Image.open("0.png").load()
i2 = Image.open("DF93D5.png").load()
i3 = Image.new("RGB", (1831, 2000), (255, 255, 255))
i3p = i3.load()

things = {}
for x in range(1831):
    for y in range(2000):
        z = tuple(map(operator.mul, (16, 16, 16, 0), tuple(map(operator.sub, i1[x, y], i2[x, y]))))
        if z[0] or z[1] or z[2] or z[3]:
            if z not in things:
                things[z] = 0
            things[z] += 1
            i3p[x, y] = 0,0,0
print(things)

i3.save("result.png")
