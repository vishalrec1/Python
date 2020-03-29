def Multiply(*args):
    '''
    DocString : This Function can take any number of numeric Arguments and return Product of the numbers. If any aplhanumeric value is passed to the function then Exception is raised.
    :param args: *args
    :return: integer value that is sum of all the numbers
    '''
    print("***The Number of arguments passed for Multiplication are ",len(args))

    #Check if all the arguments are numeric
    try:
        for n in args:
            num = int(n)
    except ValueError:
        print("The Arguments passed in function for Multiplication are NOT Numeric")
    #Multiply the numbers
    product = 1
    for n in args:
        product = product*n
    return product