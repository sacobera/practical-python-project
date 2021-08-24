menus = [ ['Egg Sandwich', 'Bagel', 'Coffee'], #Breakfast
            ['BLT', 'PB&J', 'Turkey Sandwich'], #Lunch
            ['Soup', 'Salad', 'Spagehtti', 'Taco'] ] #Dinner 

print (menus [0][2])  # this prints out the item Coffee from the first list 


####

menus = { Breakfast : ['Egg Sandwich', 'Bagel', 'Coffee'], 
           Lunch:  ['BLT', 'PB&J', 'Turkey Sandwich'], 
            Dinner: ['Soup', 'Salad', 'Spagehtti', 'Taco'] }

for name, menu in menus.items(): #using name as a temporary variable for either (bfast, lunch, dinner, menu as a second temporary variable to get the list 
    print(name, ':', menu )  