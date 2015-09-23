# Sequential Steps:
# In an ordered series thoughtout
print 'Start sequential test! :-P'

x = 2
print "x is:", x

x = x+ 10
print "now x is:", x

print 'Sequential test done!'

# Conditional Steps:
# Carried out only under certain conditions
print 'Start conditional test! :-)'

x = 5

if x < 10:
    print 'x is small-ish'

if x > 20:
    print 'x is large-ish'

if x:
    print 'Conditional test done!'

# Repeated Steps:
# Iteration variables (e.g. n) that change each time through a loop.
# Often these iteration variables go through a sequence of numbers.
print 'Start repeated test! :-D'

n = 5

while n > 0:
    print 'Loop executed, n is: ', n
    n = n - 1

print 'Repeated test done!'
