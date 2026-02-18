MAX_TOTAL = 200
total = 0
while total < MAX_TOTAL:
   number = int(input("enter a number between 50 and 100")) 
   total = number + total 
if MAX_TOTAL <= total:
    print (f"the total is {total}") 



