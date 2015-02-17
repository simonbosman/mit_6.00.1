balance = 3329
annualInterestRate = 0.2
b = balance
step = 10.0
mp = 10.0

def monthlyPay(b, mp):
    for month in range(1,13):
        b = b - mp
        b = b + annualInterestRate/12.0*b
    return b     

cnt = 0
while True:
    cnt += 1
    b = monthlyPay(b, mp)
    if b <= 0:
        break
    mp = mp + step
    b = balance
  
print 'Lowest Payment: ' + str(round(mp,2))
print str(cnt)
