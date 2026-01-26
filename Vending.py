def money(a , rate):
   
    conversion = a * rate
    print ("COVERTED MONEY:",conversion )

    price = 90 
    if(conversion >= 90):
        print("Machine can procced with the can ")
        change = conversion - price 
        print("KEEP YOUR CHANGE = ",change)
        if change > 0:
            print("dont forget to take the change")
    else:
        print("Sorry we Cant procced")
    


money(2, 90)

   

 
