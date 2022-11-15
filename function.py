
print('this is start of new code')
mi = 0 
mx = 0

def minmax(x,y):
    if(x<y):
        return x,y
    else:
        return y,x

mi,mx = minmax(50,60)
print(mi,mx)
mi,mx = minmax(150,120)
print(mi,mx)


xG = 100
def aFunct():
    xL = 500
    print(xL)
    print(xG*2)

aFunct()
print(xG)

######

print('this is start of new code')

def fun():
    x = 10
    y = 20.5
    z = 'zebra'
    return x,y,z
t = fun()
print(type(t))
print(t)


####

print('this is start of new code')

def fun(l):
    l[0] = 100;
    
L1 = [10,20,30,50]
print(L1)
fun(L1)
print(L1)
