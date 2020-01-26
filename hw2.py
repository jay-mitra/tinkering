#!/usr/bin/env python

# Wrap all of the following in a single function definition, then invoke the function (no parameters are needed). See Module 1 "Scripts, Statements and Functions" for a refresher.
# Gather the following user inputs and store each item as a variable:
# Purchaser name
# Purchaser address
# Purchaser phone number (entered as 503-555-1211)
# Car Make and Model
# Purchase Price
# After the user inputs the above information, your program should add the following values to the sale price:
# Sales tax as a percent of sale price (10.1% combined rate for ZIP 98101)
# Licensing fee
# Dealer prep fee
# Calculate total cost (as a float)
# Assign the transaction a unique ID composed of the last four letters of the purchaser's last name and their area code, separated by an underscore
# Print out the information to the screen, with the same line breaks as shown in the example below

def main():
    """main function; gathers user input, calculates tax and fee structure, adds a transaction ID and prints information to stdout"""
    print ("Please provide the following information (You will see formatting instructions inside brackets).")
    print ("----------")
    # get customer data, and format it for use
    purchaser_name = input("Name (Last, First): ")
    purchaser_address = input("Address (Street Number, Street Name, City, State, Zip): ")
    purchaser_phone = input("Phone Number (XXX-XXX-XXXX): ")
    purchaser_car = input("Car Make and Model (Make, Model): ")
    car_net_price = input ("Purchase Price ($XXX.XX): ")
    # this bit of code strips out any potential non numerical $ signs and casts it to a float for future calculations
    car_net_price = float(car_net_price.replace("$",""))
    # tax and fee structure from here
    # for the purpose of this exercise, we are assuming a standard tax of 10.1%, we could extend this by using conditionals based on zip code of the resident as we know the sales tax rates for the states
    tax_constant = .101
    car_tax_price = car_net_price * tax_constant
    car_license_fee = 100
    car_dealer_fee = 200
    car_gross_price = car_net_price + car_tax_price + car_license_fee + car_dealer_fee
    # set transaction ID
    transaction_id = purchaser_name.split(",")[0][0:4] + "_" + purchaser_phone.split("-")[0]
    # print everything out, using print ("%.2f" % foo) to format correctly to 2 decimal places for the cents after rounding the float
    print ("----------")
    print ("Hello " + purchaser_name.split(",")[1].replace(" ","") + " " + purchaser_name.split(",")[0] + ",")
    print ("Thank you for your purchase of a " + str(purchaser_car) + ". Following is a breakdown of your total price:")
    print ("Sales Price: $" + "%.2f" % round(car_net_price,2))
    print ("Tax: $" + "%.2f" % round(car_tax_price,2))
    print ("Licensing Fee: $" + "%.2f" % round(car_license_fee,2))
    print ("Dealer Prep Fee: $" + "%.2f" % round(car_dealer_fee,2))
    print ("Grand Total: $" + "%.2f" % round(car_gross_price,2))
    print ("----------")
    print ("Your purchase has been assigned an ID number of " + transaction_id + ". Please refer to this ID number if you have any questions.")

main()
