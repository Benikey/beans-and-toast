#password yo

count = 0
PASSWORD = input("input password")

if PASSWORD =="charmander":
    print ("correct password vro")

else: 
    print ("incorrect, try again")
    count + 1
    
if count >= 5:
    print ("Too many failed attempts. Access denied.")