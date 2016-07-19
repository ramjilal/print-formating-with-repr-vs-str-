a = 1
b = 12.1445
c = 'here'
print 'hello %s only %d value of %f' % (c,a,b)

#here %x.yf -> represented as:

# x is number of digits before decimels
# let consider given digit is 12.34 and here x = 6
# than there two whitspace before print this value

# y is number past digit of decimal 
#for example 
#let consider ' V = 12.1456 ' is vale and y = 2
# than print '%.yf' %V 
# which gives -> 12.14 only . left digits remove from number

print 'hello %s only %d value of %1.2f' % (c,a,b)

# %r is also represent for string
print 'hello %r only %d value of %f' % (c,a,b)

# format() is also use print formating 
print 'hello {c} only {a} value of {b}'.format(c='here',a=1,b=12.1445) 
