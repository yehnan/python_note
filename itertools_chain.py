

from __future__ import print_function
from itertools import chain

a = [70, 81, 92]
b = ['hi', 'hello', 'aloha', 'ahoy']
c = [31.3, 32.5, 29.2, 28.5]

for e in chain(a, b, c):
    print(e, ' ', end='')
print()

def my_chain(*iterables):
    for it in iterables:
        for e in it:
            yield e

for e in my_chain(a, b, c):
    print(e, ' ', end='')
print()

####

def foo(x):
    i = 1
    while i <= x:
        yield range(0, i)
        i += 1

for e in chain.from_iterable(foo(4)):
    print(e, ' ', end='')
print()

def my_chain_from_iterable(iterables):
    for it in iterables:
        for e in it:
            yield e

for e in my_chain_from_iterable(foo(4)):
    print(e, ' ', end='')
print()

