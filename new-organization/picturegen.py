from PIL import Image

flag = '''Congratulations!

Wow! You found my very hard secret!
I thought it was very hard..

Flag is uctfexpertofbraincopter

You are very good in CTF, continue to solve hard puzzles and find good flags!

Best luck at other tasks!

UPML CTF team'''

x = 0
y = 0
dir = 1
ids = [[10] * 200 for i in range(200)]
sym = 0
pos = 0
while sym < len(flag):
  if y == 199 and dir == 1:
    ids[x][y] = 8
    x += 1
    ids[x][y] = 8
    y -= 1
    dir = -1
    continue
  if y == 0 and dir == -1:
    ids[x][y] = 9
    x += 1
    ids[x][y] = 9
    y += 1
    dir = 1
    continue
  if pos > ord(flag[sym]):
    pos = 0
    sym += 1
    ids[x][y] = 0
    y += dir
    continue
  if pos == ord(flag[sym]):
    pos += 1
    ids[x][y] = 4
    y += dir
    continue
  ids[x][y] = 2
  pos += 1
  y += dir

im = Image.open("old_logo.png")
pix = im.load()
for i in range(200):
  for j in range(200):
    r, g, b = pix[j, i]
    current = (r * 65536 + g * 256 + b) % 11
    goal = ids[i][j]
    if b >= 244:
      b -= 11
    if b < 11:
      b += 11
    b -= current
    b += goal
    pix[j, i] = r, g, b

im.save("logo.png", compress_level=0)