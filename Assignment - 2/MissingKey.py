#Handling missing keys in Python dictionaries
def myfunc():
    print("\nName: Siddhanth Jagtap")
    country_code = {'a' : 1, 'b' : 2, 'c' : 3}
    print()
    print(country_code.get('a', 'Not Found'))
    print()
    print(country_code.get('f', 'Not Found'))
    print()
myfunc()