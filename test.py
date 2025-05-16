file = '/tmp/quz/foo.md'

t = filepath = file[::-1].split(chr(47), 1)[1][::-1]

print(t)