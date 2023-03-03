def check_weight():
    if bmi < 18.4:
        print('Under weight!!!')
    elif bmi >= 18.5 or bmi < 24.9:
        print('normal')
    elif bmi >= 24.9 or bmi < 29.9:
        print('over weight')
    elif bmi >= 29.9 or bmi < 34.5:
        print('Obese')
    else:
        print('Extrim obese')

ghad = float(input('ghad(cm): '))
vazn = float(input('vazn(kg): '))
bmi = (vazn / ghad / ghad ) * 10000
print(bmi) # calculate bmi and print
check_weight()