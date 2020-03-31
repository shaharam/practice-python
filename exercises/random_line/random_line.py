import random
import os

lines = open('text.txt').read().splitlines()
print random.choice(lines)

print os.path.dirname(__file__)     # Slash path
print os.getcwd()   # back slash path
