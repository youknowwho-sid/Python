#Find the most repeated word in a text file
from collections import Counter
def myfunc():
    print("\nName: Siddhanth Jagtap")
    dict = {}
    with open("anthem.txt", "r") as f:
        w = []
        for l in f:
            x = l.lower().replace(',','').replace('.','').replace('\n', '').split(" ")
            for w1 in x:
                w.append(w1)

    c = Counter(w)  

    k, v = None, 0
    for key, value in c.items():
        if value > v:
            v = value
            k = key

    print(f"\nThe most repeated word in song lyrics is '{k}' and occurred {v} times")
    print()
myfunc()