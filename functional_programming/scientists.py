import collections
from pprint import pprint

# structure of Scientist object
Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',
])

# Using tuple for immutable purpose (can't del or change the data)
scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
)
pprint(scientists)

print('#################################################################')
nobel_iter = filter(lambda x: x.nobel is True, scientists)  # returns iterator (mutable)
print(type(nobel_iter))
pprint(nobel_iter)

print('#################################################################')
print('Printing nobel scientists using for loop')
for scientist in scientists:
    if scientist.nobel is True:
        print(scientist)

print('#################################################################')
print('Printing nobel scientists using filter+lambda (changed to tuple)')
nobel_iter = tuple(filter(lambda x: x.nobel is True, scientists))   # changed to tuple (immutable)
print(type(nobel_iter))
pprint(nobel_iter)

print('#################################################################')
print('Printing physics and nobel')
pprint(tuple(filter(lambda x: x.field == 'physics' and x.nobel, scientists)))   # physics and nobel


def is_nobel(x):
    return x.nobel


print('#################################################################')
print('Printing nobel using is_nobel function')
pprint(tuple(filter(is_nobel, scientists)))

print('#################################################################')
print('Printing nobel using list comprehensions')
pprint(tuple(x for x in scientists if x.nobel is True))


print('#################################################################')
print('MAP MAP MAP MAP MAP MAP MAP MAP MAP MAP')
names_and_ages = tuple(map(lambda x: {'name': x.name, 'age': 2020 - x.born}, scientists))
pprint(names_and_ages)

print('#################################################################')
print('Using list comprehension')
pprint(tuple({'name': x.name, 'age': 2020 - x.born} for x in scientists))


