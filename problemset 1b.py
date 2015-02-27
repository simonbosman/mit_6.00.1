s = 'obobobbobbwsobobobobojbbobbybo'
bobs = 0
startidx = 0
first = True

while True:
   
    if (first):
        startidx = s.find('bob')
        if startidx != -1:
            bobs += 1
        first = False;
        
    startidx = s.find('bob', startidx+1)
    
    if startidx == -1:
        break
        
    bobs += 1
   

print 'Number of times bob occurs is: ' + str(bobs)
        
    