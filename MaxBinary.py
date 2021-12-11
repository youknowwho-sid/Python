import time
def myfunc():
    start_time = time.time()
    binary = ""
    binary += " "
    c = 1 
    i = 0
    max = 0
    while i<len(binary)-1:
        if (binary[i] == binary[i+1]):
            c = c + 1
            if(c>max):
                max = c
                k = binary[i]
        else:
            c = 1
        i = i + 1
    print (k,max)
    print(f"done in: {time.time() - start_time}")
myfunc()