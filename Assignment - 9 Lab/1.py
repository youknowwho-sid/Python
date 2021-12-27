#Name: Siddhanth Nilesh Jagtap Regno: 21BCE7490
#Python program to read a text file and display words that are ending with 'H'/'h'

def myfunc():
	
	f = open("Vit.txt","r")					#open file
	data = f.read()							#store data
	print("File Data=")
	print(data)
	print("\nWords ending in H =")				
	l = data.replace(",","").replace(".","").replace(":","").split()			#removing non-alpha characters 
	for w in l:
		if (w[-1] == 'h' or w[-1] == 'H'):
			print(w)		
	f.close()						#closing file

myfunc()