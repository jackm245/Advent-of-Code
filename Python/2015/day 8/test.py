from curses import ascii as a

print(a.ascii('\x27'))
print(a.ascii('\xfb'))
print('\x27')
print(chr(27))
print((hex(39)))
print(type('\x27'))

a = '\x27'
print(a)
