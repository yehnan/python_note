

from __future__ import print_function

names = ['Amy', 'Eric', 'Cathy', 'David', 'Bob']

for i in range(len(names)):
    print(names[i], ' ', end='')
print()

for name in names:
    print(name, ' ', end='')
print()

for i, name in enumerate(names):
    print(i, name)

for name in reversed(names):
    print(name, ' ', end='')
print()

for name in sorted(names):
    print(name, ' ', end='')
print()

for name in sorted(names, reverse=True):
    print(name, ' ', end='')
print()

for name in sorted(names, key=lambda x: len(x)):
    print(name, ' ', end='')
print()


