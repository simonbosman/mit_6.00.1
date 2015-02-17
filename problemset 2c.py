balance = 999999
annualInterestRate = 0.18
b = balance
epsilon = 0.01
lb = balance/12.0
ub = balance * (1 + annualInterestRate/12.0) ** 12 / 12.0
mp = (lb+ub)/2.0

def monthlyPay(b, mp):
    for month in range(1,13):
        b = b - mp
        b = b + annualInterestRate/12.0*b
    return b  

cnt = 0
while True:
    cnt += 1
    b = monthlyPay(b, mp)
    if b > epsilon:
        lb = mp
    else:
        ub = mp
    mp = (lb + ub)/2.0
    if b <= epsilon and b >= 0:
        break
    b = balance
    
print 'Lowest Payment: ' + str(round(mp,2))
print str(cnt)