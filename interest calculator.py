#fixed deposit calculator
principal = float(input('Enter your principal amount in SGD: '))
interestRate = float(input('Enter your interest rate in %: '))
period = float(input('Enter your tenor in years: '))

#formula
interest = principal * (interestRate/100) * period
totalAmt = principal + interest

#output
print('Your interest accumulated for the period of {:.2f}'.format(period) + ' years is SGD {:.2f}.'.format(interest))
print('You total amount including principal and accumulated interest is SGD {:.2f}.'.format(totalAmt))