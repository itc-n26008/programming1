import random

alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
#print(alphabet)
ch = random.choice(alphabet)
print(ch)
while True:
    val = input()
    if ch == val:
       print('OK')
       break
    else:
         print('NG')
