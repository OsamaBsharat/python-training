weight = float(input("Weight:"))
choose = str(input("(K)g or (L)bs: "))
choose = choose.upper()

if choose=="K":
    result=str(weight/0.45)
    print("Weight in Lbs : " + result)
elif choose=="L":
    result=str(weight*0.45)
    print("Weight in Kg : " + result)    
else:
    print("Wrong Choice")
