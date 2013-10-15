''' 0.1 
input:  list l
output: unique tuples (x, y, z), with x + y = z, and x, y, z all belongs
        to list l
'''

import datetime

l = range(1000)
# python oneliner: list comprehensions #

begin = datetime.datetime.now()
a = [(x, y, z) for x in l for y in l for z in l if x + y == z]
end = datetime.datetime.now()
a.sort()
#print a
print "time = ", end - begin

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

b.sort()
#print b
print "time = ", end - begin

assert a == b
    
    

