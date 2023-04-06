from PIL import Image

txt = open("dummy.txt")
BG = Image.open("myfont/bg.png")
sheet_width = BG.width
gap, ht = 125, 110
for i in txt.read():
    if i == "\n":
        gap, ht = 125, ht+36

    else:
        try:
            j = 1
            if j == 2:
                cases = Image.open("myfont/{}-2.png".format(str(ord(i))))
            else:
                cases = Image.open("myfont/h1/{}-1.png".format(str(ord(i))))
        except:
                cases = Image.open("myfont/h1/32-1.png".format(str(32)))
        cases = cases.convert("RGBA")
        BG.paste(cases, (gap, ht), cases)
        size = cases.width
        height = cases.height
        gap += size
        if sheet_width-10 < gap or (len(i) * 140 > (sheet_width - gap) and i == " "):
            gap, ht = 125, ht + 36

print(gap)
print(sheet_width)
BG.show()
