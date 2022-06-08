temp = eval(input('Enter a temprature: '))
unit = input('Celsius or Fahrenheit?')

if unit == 'Celsius':
    print(temp, 'Celsius is', 9/5*temp+32, 'Fahrenheit')

elif unit == 'Fahrenheit':
    print(temp, 'Fahrenheit is', 5/9*temp-32, 'Calsius')
    
