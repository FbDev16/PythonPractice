#Item 7
#visual trick
print("\n" + "="*30)
print("Sucessfully Register Product!")
print("="*30)

#type_bc = type_of_bicy

print(f"Service resume: \n Type: {type_bc} | Time Use: {time_of_use} | Price Per Minute: {base_price} | \nDiscount (if apply): {discount_applied} | Recharges (if apply): {recharge_applied} | Total Cost: {total_cost}")

#----------------------------------------------------------------------------------------------------------------------------------
    # item 8 -----> while into the main while, the function is ask to user if he want take other service or exit the program. (make tab into the main while)

validation = True

while validation:
    
    answer = input("do you want another rental?, Yes(Y) / No(N): ").lower()
    
    if answer == 'y':
        
        break
    
    elif answer == 'n':
        
        validation = False
          
        break
    
    else:
        
        print("ERROR: Response with 'Y' or 'N'.")
        


print("\n" + "="*30)
print("Thanks For Use Our Services")
print("="*30)
    
        
