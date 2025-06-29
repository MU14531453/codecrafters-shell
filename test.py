import os
import sys

def test_function(s):
    if s[4:] == '12345':
        return s[4:][::-1]
    elif s[4:] == '54321':
        return 'sukces'
    else:
        return 'aaa' + s[3:]

foo = 'pwd 12345 | pwd'
fork_foo = foo.split('|')

fork_read, fork_write = os.pipe()

processid = os.fork()

if processid:
    os.close(fork_write)
    fork_read = os.fdopen(fork_read, 'r')
    tail = fork_read.read()
    x = fork_foo[1].strip() + ' ' + tail
else:
    
    x = fork_foo[0].strip()

x = test_function(x)

if processid:
    pass
else:
    parent = os.fdopen(fork_write, 'w')
    #parent.write(x)
    print(x, file = parent)


print(x)