

s = 'Hello Python'

# s.reverse()

print(s[::-1])

print(''.join(reversed(s)))

def reverse_i(s):
    r = ''
    for c in s:
            r = c + r
    return r
print(reverse_i(s))

def reverse_r(s):
    if len(s) <= 1:
            return s
    else:
            return reverse_r(s[1:]) + s[0]
print(reverse_r(s))

r = list(s)
r.reverse()
print(''.join(r))

def reverse_li(s):
    r = []
    for c in s:
        r.insert(0, c)
    return ''.join(r)
print(reverse_li(s))

print(''.join([s[i] for i in range(len(s)-1, -1, -1)]))

print(''.join(s[i] for i in range(len(s)-1, -1, -1)))

def reverse_g(s):
    def sub(s):
        for i in range(len(s)-1, -1, -1):
            yield s[i]
    return ''.join(sub(s))
print(reverse_g(s))

from collections import deque
r = deque(s)
r.reverse()
print(''.join(r))

