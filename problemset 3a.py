def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    totRad = 0.0
    #for x in range(start, stop, step):
    #    totRad = totRad + f(x) * step
     
    while start < stop:
        totRad = totRad + f(start) * step
        start = start + step    
               
    return totRad
    
print radiationExposure(40, 100, 1.5)



