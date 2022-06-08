length = eval(input('Enter a length in centimeters: '))

if length < 0:
    print('Invalid length')
    
else: print(length, 'centimeters is', length/2.54, 'inches')