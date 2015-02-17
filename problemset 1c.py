s = 'zyxwvutsrqponmlkjihgfedcba'
substr = ''
startidx = 0
lenidx = 0
    

for idx in range(len(s)):
    
    if idx == 0:
        substr = s[idx]
        continue 
   
    if idx == len(s)-1:
        if ord(s[idx]) >= ord(s[idx-1]):
            lenidx += 1
        if lenidx > len(substr):
            substr = s[startidx : startidx+lenidx]
        break  
        
    if ord(s[idx]) >= ord(s[idx-1]):
        if lenidx == 0:
            startidx = idx-1
            lenidx += 2
        else:
            lenidx += 1
   
    else:
        if lenidx>0 and lenidx > len(substr):
            substr = s[startidx : idx]
        lenidx = 0
              
    
print 'Longest substring in alphabetical order is: ' + substr
        
        
    
    

         
    
    