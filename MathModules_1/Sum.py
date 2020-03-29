def Sum(*args):
    '''
    DocString : This Function can take any number of numeric Arguments and return sum of the numbers. If any aplhanumeric value is passed to the function then Exception is raised.
    :param args: *args
    :return: integer value that is sum of all the numbers
    '''
    print(args)
    print("***The Number of arguments passed for Addition are ",len(args))

    #Check if all the arguments are numeric
    try:
        for n in args:
            num = int(n)
    except ValueError:
        print("The Arguments passed in function for Addition are NOT Numeric")
    #Add the numbers
    print("The sum of Number is ", sum(args))
    return sum(args)