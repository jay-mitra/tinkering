import math

def safe_int_input(prompt):
    """Helper function to get an int from user input safely"""
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            print ("Sorry, I didn't understand that.")
            continue
        else:
            break
    return user_input

def how_many_pizzas(how_many_people, average_slices):
    """"How many pizzas to order based on number of people and average number of slices, and how many slices are leftover
"""
    result = int(math.ceil((how_many_people * average_slices) / TOTAL_SLICES))
    left_over = int(TOTAL_SLICES - ((how_many_people * average_slices) % TOTAL_SLICES))
    return result, left_over

def total_pizza_cost(how_many):
    """Calculates total pizza cost, which is number of pizzas + delivery fee * tax + tip (i.e. to make the tip untaxed)"""
    result = (((how_many * PIZZA_COST) + DELIVERY_FEE) / 100) * (100 + TAX_RATE) / 100 * (100 + TIP_RATE)
    return result

def cost_per_person(how_many_people, cost):
    """Cost per person"""
    result = cost / how_many_people
    return result

# Declaring global constants
PIZZA_COST = 15.99
TOTAL_SLICES = 8
TAX_RATE = 10.1
TIP_RATE = 18
DELIVERY_FEE = 3.99

# Number of people who want pizza
how_many_people = safe_int_input("How many people want pizza? ")
# Average number of slices per person
average_slices = safe_int_input("How many slices do you want per person, on average? ")

# Calculate results
how_many_pizzas, left_over_slices = how_many_pizzas(how_many_people, average_slices)
total_cost = (total_pizza_cost(how_many_pizzas))

print ("You will need {} pies, for a total cost of ${} including tip and delivery fee".format(how_many_pizzas,round(total_cost,2)))
print ("Each person will need to pay ${}".format(round(total_cost / how_many_people,2)))
print ("You'll have {} slices left.".format(left_over_slices))
