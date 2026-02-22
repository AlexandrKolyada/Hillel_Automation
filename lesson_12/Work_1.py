def multiplication_table(number):
    # Initialize the appropriate variable
    if number <= 0:
        return "Number must be greater than zero"
    print("Number must be greater than zero")
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        if  result > 25:
            return "number is too big"
        print(f"{number}" + "x" + f"{multiplier}"+ "=" f"{result}")
        # Increment the appropriate variable
        multiplier += 1
    #return None

multiplication_table(0)