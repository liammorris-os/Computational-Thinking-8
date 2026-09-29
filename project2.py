pizza_or_starbucks = input("You are feeling hungry today. Where will you go? pizza place, starbucks or gym (Type in all lowercase or else it will not work)")

if pizza_or_starbucks == "starbucks":
    food = input("What food will you get? matcha, banana bread, or cake pop?")

    if food == "banana bread":
        print ("the banana bread was very yummy")
    
    elif food == "cake pop":
        ant = input("the cake pop had a poison antidote what will you do. say either give to employee or throw away")
        if ant == "throw away":
            print("you see someone dying from poisoned matcha and they could have used the antidote")
        elif ant == "give to employee":
            print ("the employee throws it away and gives you a new cake pop and you leave")
    if food == "matcha":
        hospitale = input ("The matcha was poisoned. Do you want to go to the hospital? or let someone in starbucks help you. Type hospital Type help")
        if hospitale == "hospital":
            print("You get help at the hospital and you live. Thanks for playing!!!")
        elif hospitale == "help":
            print("Nobody is able to help you in starbucks. You slowly die and are very sad you drank matcha. Thanks for playing!!!")
        else:
            print("Please type one of the answers")

if pizza_or_starbucks == "pizza place":
    pizza_food = input("What pizza will you order. pepperoni or cheese")
    
    if pizza_food == "cheese":
        toppings_or_no = input("The server asks if you want toppings. do you? type yes, no or pineapple")
        if toppings_or_no == "yes":
            print("You got peppers, onions, and some more cheese sprinkled on top. Thanks for playing!!!")
        elif toppings_or_no == "no":
            print("you get a plain cheese pizza and it is still just as good. Thanks for playing!!!")
        elif toppings_or_no == "pineapple":
            print("leave the game right now. not thanks for playing.")
        
    if pizza_food == "pepperoni":
        print("The pepperoni was very good. Thanks for playing!!!")
    else:
        print("Please pick one of the answers")
else:
    print("Please pick one of the answers")
if pizza_or_starbucks == "gym":
    work_out = input("Do you want to work out? type yes or no")
    if work_out == "yes":
        print("you have a very nice workout")
    if work_out == "no":
        print("why are you at the gym then")
    else:
        print("Please type one of the answers")