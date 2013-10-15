''' 0.1 
input:  list l
output: unique tuples (x, y, z), with x + y = z, and x, y, z all belongs
        to list l
'''

import datetime


l = range(800)
# python oneliner: list comprehensions #
def oneliner(l):
    begin = datetime.datetime.now()
    a = [(x, y, z) for x in l for y in l for z in l if x + y == z]
    end = datetime.datetime.now()
    return (a, end-begin)

''' assume all postive numbers '''
def allpost(l):
    begin = datetime.datetime.now();
    # if all positive
    b = list()
    l.sort(reverse=True)
    ld = dict()
    for i in l:
        ld[i] = dict()
        # all positive saves you this: don't have to do another for loop
        for (number, number_dict) in ld.items():
            number_dict[number - i] = i
    
    for i in l:
        for (number, number_dict) in ld.items():
            if i in number_dict:
                b.append((i, number - i, number))
    end = datetime.datetime.now()
    
    return (b, end-begin)
    
def findsum(l):
    begin = datetime.datetime.now();
    b = list()
    ld = dict()
    for i in l:
        ld[i] = dict()
        for j in l:
            ld[i][i - j] = j
    
    for i in l:
        for (number, number_dict) in ld.items():
            if i in number_dict:
                b.append((i, number - i, number))
    end = datetime.datetime.now()
    
    return (b, end-begin)

(a, t1) = oneliner(l)
(b, t2) = allpost(l)
(c, t3) = findsum(l)

a.sort()
b.sort()
c.sort()
assert a == b
assert a == c
print "positive numbers: "
print "oneliner = \t", t1, "\nallpost = \t", t2, "\nfindsum = \t", t3, "\n"

l = range(-100, 600)
(a, t1) = oneliner(l)
(c, t3) = findsum(l)    
a.sort()
c.sort()
assert a == c
print "all numbers: "
print "oneliner = \t", t1, "\nfindsum = \t", t3, "\n"
    

