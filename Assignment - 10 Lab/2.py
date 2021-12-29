#Name: Siddhanth Nilesh Jagtap Regno.: 21BCE7490
#Program for recursive function that accepts an integer argument n to return the nth Fibonacci number. 

# Function for nth Fibonacci number

def fibonacci(x):
	if x == 1:
		return 0
	elif x == 2:
		return 1
	else:
		return fibonacci(x-1)+fibonacci(x-2)            #sum of previous 2 = next number


def myfunc():
    x = int(input("Enter the number of terms: "))           #input element
    res = fibonacci(x)                          #call function
    print(res)
myfunc()