# Matthew hall
# December 10, 2024
# 1.1 While Loop Practice

# 7-5 Movie Tickets
prompt = "What is your age (0 to quit): "
while True:
    movie_ticket = int(input(prompt))

    if movie_ticket == 0:
        break
    elif movie_ticket >= 1 and movie_ticket <= 3:
        print(f"You are {movie_ticket} years old and your ticket is free!")
        print()
    elif movie_ticket >= 3 and movie_ticket <= 12:
        print(f"You are {movie_ticket} years old and your ticket is $10.00!")
        print()
    elif movie_ticket >= 12:
        print(f"You are {movie_ticket} years old and your ticket is $15.00!")
        print()
    else:
        print("Enter a number!!!")

# 7.6 Three exits
prompt = "Give me a pizza topping (quit to exit): "
while True:
   pizza_topping = input(prompt) 
   
   if pizza_topping == "quit":
       break
   else:
       print(f"Ok, I will put {pizza_topping} on your pizza.")

prompt = "\nGive me a pizza topping (quit to exit): "
toppings = 0
while True:
   pizza_topping = input(prompt) 
   
   if toppings > 3:
       break
   else:
       print(f"Ok, I will put {pizza_topping} on your pizza.")
       toppings = toppings + 1














































































































































































