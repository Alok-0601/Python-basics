a=input("What's your weight :")
b=input("(L)bs or (K)gs: ")
if b.upper()=='K':
    print(f'Your weight is  :{a}Kgs')
elif b.upper()=='L':
    print(f'Yor weight is : {a}pounds')
else:
    print('Your weight should be in pounds or kilograms!!')
