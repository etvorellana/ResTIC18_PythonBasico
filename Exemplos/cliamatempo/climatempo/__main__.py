import random
import sys

x = random.random()
print(type(x))

for pathItem in sys.path:
    print(pathItem)
print("____prefix____")
print(sys.prefix)