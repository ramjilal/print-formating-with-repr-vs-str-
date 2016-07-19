# here we discuss repr() vs str()

import datetime

# use of str()
print 'date and time are : {}'.format(str(datetime.datetime.now()))
# ---outpur for above statment is :
# ----------------- ' date and time are : 2016-07-19 23:17:29.154689


# use of repr()
print 'date and time are : {}'.format(repr(datetime.datetime.now()))
# ---outpur for above statment is :
# ----------------- ' date and time are : datetime.datetime(2016, 7, 19, 23, 18, 29, 165682)

# here str() return readable string operation but reopr() return unambigous object


''' 
 str():                                 |           repr():
  - make object readable	            |         - need code that reproduces object
  - generate output for end user	    |         - generate output for developer


'''
