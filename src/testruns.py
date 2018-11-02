g = dict(song = 'gangam style', run = '10k', home = 'NYC')

for k, v in g.items():
    print('This {0} is {1}'.format(k, v))

#print('Trying it {}.{}.{}'.format(**g))

def foo(song, home, run):
    print(song + ' ' + home + ' ' + run)

foo(**g)

l = [1, 2, 3, 4, 5]

first, *rest, last = l

print(str(first) + ' cool ' + str(rest) + ' ' + str(last))

def main(**kwargs):
    print('This is the main function')

if __name__ == '__main__':
    main()
