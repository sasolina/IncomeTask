def quitA():
    quitA = str(input('do you want to go futher (yes) or (no)'))
    if quitA == 'yes' or quitA == 'Yes':
        return()
    elif quitA == 'no' or quitA == 'No':
        quit()
    else:
        print ('Invalid input, please enter yes or no ')
        quitA()

TaxableIncome = int(input('Please enter your Salary \n'))
floTaxableIncome = TaxableIncome = float(TaxableIncome)
quitA()
if TaxableIncome <= 12570:
    print('You are in the personal allowance band \n')
    print(floTaxableIncome * 0 )
    quitA()
elif TaxableIncome >= 12571 and TaxableIncome <= 50270:
    print('You are in the basic band \n')
    print(floTaxableIncome * 0.20 )
    quitA()
elif TaxableIncome >= 50271 and TaxableIncome <= 125140:
    print('You are in the higher allowance band \n')
    print(floTaxableIncome * 0.40 )
    quitA()
    
else:
    print('You are in the Additonal allowance band \n')
    print(floTaxableIncome * 0.45 )
    quitA()
