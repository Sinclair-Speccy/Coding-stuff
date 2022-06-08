p = input('What is your principal value?: ')
p = input('What is your time period?: ')
p = input('What is your rate of interest?: ')

def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)
    
    si = (p * t * r)/100
    
    print('The simple interest is', si)
    return si