from hw8_class import BankAccount, OverdraftException

if __name__ == "__main__":
    """ let's do some bank account stuff """
    BA_bob = BankAccount(100)
    BA_jane = BankAccount(200)

    # Tracks an initial account balance
    # Tracks deposits in the account
    # Tracks withdrawals to the account
    # the above is handled in the BankAccount class imported from hw8_class

    # Create a script that imports the Banking class and instantiates two users with balances.
    BA_bob = BankAccount(100.00)
    BA_jane = BankAccount(200.00)

    # Prints out a current balance
    print ("Bob has ${:.2f} in his account".format(BA_bob.balance))
    print ("Jane has ${:.2f} in her account".format(BA_jane.balance))

    # Update the script to have the users deposit to their account
    BA_jane.transaction(20)
    print ("Jane has ${:.2f} in her account".format(BA_jane.balance))

    # Update the script to have the users withdraw from their bank account
    # Prints an error message if someone tries to withdraw more money than what is currently in the account
    while True:
        try:
            BA_bob.transaction(-10)
            print ("Bob has ${:.2f} in his account".format(BA_bob.balance))
        except OverdraftException:
            print ("Bob tried to overdraw!")
            break

    # let's print their statements:
    for item in enumerate(BA_bob.statement):
        if item[0] == 0:
            print ("Bob's starting balance was ${:.2f}".format(item[1]))
        else:
            if item[1] < 0:
                print ("Bob's transaction #{} was a withdrawal of ${:.2f}".format(item[0],abs(item[1])))
            else:
                print ("Bob's transaction #{} was a deposit of ${:.2f}".format(item[0],abs(item[1])))

    for item in enumerate(BA_jane.statement):
        if item[0] == 0:
            print ("Jane's starting balance was ${:.2f}".format(item[1]))
        else:
            if item[1] < 0:
                print ("Jane's transaction #{} was a withdrawal of ${:.2f}".format(item[0],abs(item[1])))
            else:
                print ("Jane's transaction #{} was a deposit of ${:.2f}".format(item[0],abs(item[1])))
