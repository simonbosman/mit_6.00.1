balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalpaid = 0
b = balance

for month in range(1,13):
    print 'Month: ' + str(month)
    print 'Minimum monthly payment: ' + str(round(b*monthlyPaymentRate,2))
    totalpaid = totalpaid + round(b*monthlyPaymentRate, 2)
    b = b - (b*monthlyPaymentRate)
    b = b + annualInterestRate/12.0*b
    print 'Remaining balance: ' + str(round(b,2)) 
  
print 'Total paid: ' + str(totalpaid)
print 'Remaining balance: ' + str(round(b,2))