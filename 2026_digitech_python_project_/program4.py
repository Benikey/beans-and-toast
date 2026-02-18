# pmo pmo pmo pmo

num = input("enter a code")
length = len(num)

if length == 13:
         
    barcode = num
    country = barcode[0:1]
    manufacture = barcode [2:7]
    product_code = barcode[7:12]
    check_no = barcode[12:13]

    print(F"Country code {country}")
    print(F"manufacturer code {manufacture}")
    print(F"country code {product_code}")
    print(F"Check code {check_no}")



else: print("what the flip man, try again")

