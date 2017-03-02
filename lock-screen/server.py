import random, time
s = "1234567890"

timeout = 60
codes = 15
tries = 8

print('''GAVPHONE REMOTE UTILITY

Phone is locked with several 4-digit codes.
For each your try it says two numbers:
1) number of right digits at right place
2) number of right digits at wrong place
For example, if code is 1234 and you typed 3624, phone response will be 1 2

All digits are different. You have only {} tries for one code else it will send rescue signal and dogs will find us.
You have a minute for all codes'''.format(tries))

solved = 0
startTime = time.time()
for i in range(codes):
  print("Key #{:>02d}".format(i+1))
  code = ''.join(random.sample(s, 4))
  guess = False
  for _ in range(tries):
    print(">>> ", end='')
    idea = input().strip()
    if len(idea) != 4:
      print("Error: bad input")
      break
    corr = 0
    coll = 0
    bad = False
    for i in range(4):
      if not(idea[i]) in s:
        bad = True
      elif idea[i] == code[i]:
        corr += 1
      elif idea[i] in code:
        coll += 1
    if bad:
      print("Error: bad input")
      break
    print(corr, coll)
    if corr == 4:
      guess = True
      break
  left = timeout - (time.time() - startTime)
  if left < 0:
    print("Time is out :( No flag for you")
    break
  elif guess:
    solved += 1
    print("Good work! You have {:.1f} seconds left".format(left))
  else:
    print("Failed :( The code was ", code)
    break
if solved == codes:
  print("Good job! Here's your flag: uctfimp0ssibletosolve")
else:
  print("Sorry, you haven't completed the mission.")
