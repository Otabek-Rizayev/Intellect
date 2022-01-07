import random as r
lower = "abdefghijklmnopqrstuvwxyz"
upper = "ABDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "[]{}#$@!%^&=+/\|`()*;.,_-"

all = lower + upper + number + symbol
length = 9
password = "".join(r.sample(all, length))

print(" The password you generated is: ", password)
