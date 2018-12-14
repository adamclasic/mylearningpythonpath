def is_in_range(p):
    p=int(p)
    if 100000 <= p<= 999999:
        r=True
    else:
        r=False

    return r

def is_there_alt(p):
    r=False
    f=p[0]
    for l in p[2::2]:
        
        
        if l == f:
            r=True
        else:
            f=l
            
    f=p[1]        
    for l in p[3::2]:
        
        if l == f:
            r=True
        else:
            f=l
    return r

# This while Loop is for test only


while True:
     
    p=input('enter the postal code :')
    print()
    if len(p)<3 :
        print('please enter a valid Zipcode ')
    else:
        
        
        if not is_there_alt(p) and is_in_range(p) is True :
            print(p, ' is a valid Zipcode')
        else:
            print('please enter a valid Zipcode ')


    




