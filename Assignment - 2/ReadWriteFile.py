#Read content from one file and write it into another file
print("\nName: Siddhanth Jagtap")
with open(r"D:\Personal\Python\Assignment - 2\text.txt","r") as h:
    print(h.read())

    text2 = open(r"D:\Personal\Python\Assignment - 2\text2.txt)", "w")

    with open(r"D:\Personal\Python\Assignment - 2\text.txt", "r") as g:
        text2.write(g.read())
    text2.close()

with open(r"D:\Personal\Python\Assignment - 2\text2.txt","r") as i:
    print(i.read())