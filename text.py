x = 8
y = 16
z = 14

if x%2 != 0 and (x > y or y%2 == 0) and (x > z or z%2 == 0):
    print 'x is biggest'
   
elif y%2 != 0 and (y > z or z %2 == 0):
    print 'y is biggest'
    
elif (z%2 != 0):
   print 'z is biggest' 
   
else:
    print 'no odd number'