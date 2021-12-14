#Write a dictionary to a file in Python
def myfunc():
    dictionary = {"Name": "Siddhanth", "Age": 18}
    file_ = open("new.txt", "a")
    file_.write(str(dictionary))
    file_.close()
    # Reading the copy file 
    file_ = open("new.txt", "r")
    print()
    print(file_.read())
    print()
    file_.close()
myfunc()