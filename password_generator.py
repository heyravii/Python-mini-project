import random
a = "abcdefghijklmnopqrstwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ@!#%$"
passlen = 8
b = "".join(random.sample(a,passlen))
print(b)