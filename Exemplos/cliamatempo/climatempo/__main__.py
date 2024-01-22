import meuRandom
import sys

x = meuRandom.meuRandom()
print(type(x))

for pathItem in sys.path:
    print(pathItem)
print("____prefix____")
print(sys.prefix)
