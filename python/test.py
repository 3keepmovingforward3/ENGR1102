import pprint
"""
 * PREMISE: This Code Sprint is meant to test your proficiency in array
 *  creation and manipulation. It will also test your ability to
 *  construct a proper loop. Lastly, it will test your ability to breakdown
 *  a problem into smaller subsections, i.e. functions.
 *
 * INPUT: You are given one 2-dimensional array, inventory, as input that correspond 
 *  to the inventory list of your supermarket. You are also given a target department 
 *  to search for when obtaining the total product count. Lastly, you are given an 
 *  option, always '0' for this Code Sprint, that dictates what task, i.e. which created 
 *  function to call, you will perform.
 *
 * OUTPUT: You are to RETURN a single integer from your created function, which 
 *  holds the total product count from the target department. Then you are to display
 *  this result using the required string format given to you above. 
"""
def store_owner(inventory, option, target, sale_item, price_change, count_change):
    if len(inventory) == 0:
        print("Error: Empty list!")
    else:
        print("Welcome to ENGR 1102's Stop-n-shop!")
        if option == '0':
            print("That was last weeks' problem!")
        elif option == '1':
            updatePrice(inventory,sale_item,price_change)
        elif option == '2':
            updateQuantity(inventory,sale_item,count_change)
        else:
            print("I don't know how to do that!")
            
##########################################################################################
# Start your function(s) under here
##########################################################################################
def updatePrice(inventory,sale_item,price_change):
    
    print("Which item do you wish to update the price for?")
    j = 0
    for i in range(0,10):
        if (inventory[i][0] == sale_item) and (sale_item in inventory[i][0]) :
            j = i
            print(sale_item)
            print("Please enter the new price of "+str(sale_item)+ ":")
            inventory[j][2]= price_change
            inventory[j][3]= 10
            print(inventory[j][2])
            print("The new inventory is:")
            for rows in inventory:
                print(rows)
            return()

    print("We don't have any "+sale_item+" left in stock.")



def updateQuantity(inventory,sale_item,count_change):
    print("Which item do you wish to update the quantity for?")
    j=0
    for j in range(0,10):
        if inventory[j][0] == sale_item:
            print(sale_item)
            print("Please enter the new quantity of "+str(sale_item)+":")
            inventory[j][3]= count_change
            print(count_change)
            print("The new inventory is:")
            for rows in inventory:
                print(rows)
            return()
    print("We don't have any "+sale_item+" left in stock.")
    



