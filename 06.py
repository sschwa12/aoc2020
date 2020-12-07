from utils import read_file

data = read_file('06', do_strip=False)

# part 1
forms = [set(''.join(l.split('\n'))) for l in ''.join(data).split('\n\n')]

print('p1', sum([len(f) for f in forms]))

# part 2
forms = [l.split('\n') for l in ''.join(data).split('\n\n')]

print('p2', sum([len(set(f[0]).intersection(*f)) for f in forms]))
