# This program askes the user various questions, in the correct order, and only accepts valid inputs.
price = 0.00
name = input("Name: ").capitalize()

# verifying validity of name input.
# If the name includes any non-alphabetic characters, "Invalid input." will be returned and the program will quit.
if name.isalpha() == False:
    print("Invalid input.")
    quit()

beverage = input("Beverage: ").lower()

# operations when beverage is coffee (Asks for size, then flavor input etc.)
# the user can enter "C", "c", or spell "coffee" with with any combination of upper and lower case characters.
if beverage == "coffee" or beverage == "c":
    beverage = "coffee"

    # size input, when price is inputted the corresponding cost is added to the "price" variable"
    # If invalid size is entered, the message "Sorry, that's not a vald size." will be printed and the program will quit.
    size = input("Size: ").lower()
    if size == "small" or size == "s":
        size = "small"
        price = price + 1.50
    elif size == "medium" or size == "m":
        size = "medium"
        price = price + 2.50
    elif size == "large" or size == "l":
        size = "large"
        price = price + 3.25
    # if input for size is invalid
    else:
        print("Sorry, that's not a valid size.")
        quit()

    # Coffee flavoring input
    # The customer can choose between chocolate, vanilla, or no flavoring.
    flavoring = input("Flavoring: ").lower()
    if flavoring == "vanilla" or flavoring == "v":
        flavoring = "vanilla"
        price = price + 0.25
    elif flavoring == "chocolate" or flavoring == "c":
        flavoring = "chocolate"
        price = price + 0.75
    elif flavoring == "" or flavoring == "none":
        flavoring = "no"
    else:
        print("Sorry, that flavor is not an option.")
        quit()

# operations when beverage is tea (asks for size, then flavoring etc.)
elif beverage == "tea" or beverage == "t":
    beverage = "tea"

    # size input
    # If invalid size is entered, the message "Sorry, that's not a vald size." will be printed and the program will quit.
    size = input("Size: ").lower()
    if size == "small" or size == "s":
        size = "small"
        price = price + 1.50
    elif size == "medium" or size == "m":
        size = "medium"
        price = price + 2.50
    elif size == "large" or size == "l":
        size = "large"
        price = price + 3.25
    # if input for size is invalid
    else:
        print("Sorry, that's not a valid size.")
        quit()

    # Tea flavoring input
    # The customer can choose between mint, lemon, or no flavoring.
    flavoring = input("Flavoring: ").lower()
    if flavoring == "lemon" or flavoring == "l":
        flavoring = "lemon"
        price = price + 0.25
    elif flavoring == "mint" or flavoring == "m":
        flavoring = "mint"
        price = price + 0.50
    elif flavoring == "" or flavoring == "none":
        flavoring = "no"
    else:
        print("Sorry, that flavor is not an option.")
        quit()

# If beverage is neither coffee or tea, this function will end the program (invalid input).
else:
    print("Sorry, we don't serve that here.")
    quit()

# adding tax (+13%) and rounding price to 2 decimal places
price = round(price * 1.13, 2)

# Final output of customer's requested order
print("For {}, a {} {} with {} flavoring. Cost: ${} (tax included).".format(name, size, beverage, flavoring, price))
