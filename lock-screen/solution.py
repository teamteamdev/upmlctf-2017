from socket import socket, AF_INET, SOCK_STREAM
from itertools import permutations
import sys

# Server connection wrapper
class Connection:
  def __init__(self, ip, port):
    self._sock = socket(AF_INET, SOCK_STREAM)
    self._sock.connect((ip, port))
  
  def read(self, length = 1024):
    return self._sock.recv(length).decode()
  
  def write(self, data):
    self._sock.send(data.encode())
  
  def close(self):
    self._sock.close()

# calculate answer for any guess and answer
def calc(guess, answer):
  correct = 0
  exists = 0
  for i in range(4):
    if guess[i] == answer[i]:
      correct += 1
    elif guess[i] in answer:
      exists += 1
  return (correct, exists)

# establish connection
conn = Connection("ctf.upml.tech", 1234)

# generate all valid numbers
nums = set(permutations('0123456789', 4))
good = set()

flag_found = False

# make request with selected number
def request(num):
  global conn, flag_found
  conn.write(''.join(num) + '\n')
  data = conn.read()
  if data[0] == '4':
    print(num)
    if 'uctf' in data:
      print(data)
      flag_found = True
    sys.stdout.flush()
  return map(int, data.split('\n')[0].split())

# check the number and delete all wrong possibilities
# returns True if number is guessed
def check(num):
  global conn, good
  corr, ex = request(num)
  if corr == 4:
    return True
  for item in good.copy():
    if (corr, ex) != calc(num, item):
      good.remove(item)
  return False

welcome = conn.read()

while not flag_found:
  # all items are OK
  good = nums.copy()
  # each time check first available item
  while not check(next(iter(good))):
    continue

conn.close()