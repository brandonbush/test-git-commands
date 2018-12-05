import debug_dec

#Use the debug decorator function
@debug_dec.debug
def foo(song, home, run):
    print(song + ' ' + home + ' ' + run)

#Jon -- Uncomment below line
@debug_dec.debug
def tswizzle(age=22):
    return 'I don\'t know about you, but I\'m feeling {}'.format(age)

def main(**kwargs):
    print('This is the main function - ksdjbqekdb - dsjdbj')

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

#Fun with functions and default arguments

print(tswizzle())

print(tswizzle(31))

#Get a file from this directory
with open('testfile.txt', 'r') as localfile:
    for line in localfile:
        print(line)

print("Comment 1 - asdjkl")