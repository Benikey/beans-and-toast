# for paracetamol 

CHILDAGE = 12

age = int(input("how old is the child?"))

if age > CHILDAGE:
    print ("take 2 tablets")

else:
    weight = int(input("how much do they weigh?"))
    dosage = weight * 10 
    print (f"take {dosage} mg of paracetamol")




