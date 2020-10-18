def gcd(pa,qa):
    if qa == 0 :
        return pa
    r = pa % qa
    print(r)
    return gcd(qa,r)

def gcd2(pa,qa):
    while qa != 0:
        temp = qa
        qa = pa % qa
        pa = temp
    return pa

v = input('Enter the number of value: ')
try:
    va = int(v)
except:
    print('Invalide value!')
    quit()

if va == 2:
    p = input('Enter the number: ')
    q = input('Enter the number: ')
    try:
        fa = int(p)
        fb = int(q)
    except:
        print('Invalid value!')
        quit()

    result = gcd(fa,fb)
    result1 = gcd2(fa,fb)
    print("Answer with recursion = {}".format(result))
    print("Answer without recursion = {}".format(result1))
if va == 3:
    p = input('Enter the number: ')
    q = input('Enter the number: ')
    r = input('Enter the number: ')
    try:
        fa = int(p)
        fb = int(q)
        fc = int(r)
    except:
        print('Invalid value!')
        quit()
    
    result = gcd(fc,gcd(fa,fb))
    
    result1 = gcd2(fc,gcd2(fa,fb))

    print("Answer with recursion = {}".format(result))
    print("Answer without recursion = {}".format(result1))