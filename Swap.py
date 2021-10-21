#Program To Swap Two Numbers 
def myfunc():
    x = int(input('Enter value for x: '))
    y = int(input('Enter value for y: '))
    k=x
    x=y
    y=k
    print('The swapped values of x and y are:',x,',',y)
myfunc()