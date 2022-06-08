temprature = eval(input('Enter a temperature in celsius: '))

if temprature <-273.15:
    print('That temperature is invalid because it is below absolute zero')

elif temprature ==-273.15:
    print('That temperature is absolute zero')
    
elif temprature >=-273.15 and temprature <0:
    print('That temperature is below freezing')
    
elif temprature ==0:
    print('That temprature is at the freezing point')
    

    
    
