while True :
    ch= (input('enter a y to continue\n'))
    if ch=='y':
        a=int(input('enter a number'))
        c=a%2
        if a%2==0:
            print ('its even')
            print(c)
        else :
            print('its odd')
            print(c)
    else:
        break
    

          