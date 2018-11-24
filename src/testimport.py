import testruns

print('In the import')

#test whether we can access variables in the other file
g = testruns.l

print(g)

#Return a list of odd numbers between inputs l and r
def oddNumbers(l, r):
    retval = []
    for i in range(l, (r+1)):
        if (i%2) != 0:
            retval.append(i)
            
    return retval