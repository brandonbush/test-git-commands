import testruns

print('In the import')

g = testruns.l

print(g)

def oddNumbers(l, r):
    retval = []
    for i in range(l, (r+1)):
        if (i%2) != 0:
            retval.append(i)
            
    return retval