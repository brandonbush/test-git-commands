import debug_dec

#Use the debug decorator function
@debug_dec.debug
def foo(song, home, run):
    print(song + ' ' + home + ' ' + run)

def main(**kwargs):
    print('This is the main function')

#Only runs if this script is the one invoked from the command line
if __name__ == '__main__':
    main()

#Playing with dictionaries
testvar = dict(song = 'gangam style', run = '10k', home = 'NYC')

for k, v in testvar.items():
    print('This {0} is {1}'.format(k, v))

foo(**testvar) 

#Easily break apart a list
l = [1, 2, 3, 4, 5]

first, *rest, last = l

print(str(first) + ' cool ' + str(rest) + ' ' + str(last))

#Playing with lambdas and list comprehension
squares = lambda x: x*x
testlist = [squares(x) for x in range(10)]

print(', '.join(str(t) for t in testlist))