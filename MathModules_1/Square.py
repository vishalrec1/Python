def Square(*args):
    '''
    DocString : This Function can take any number of numeric Arguments and return Square of the numbers. If any aplhanumeric value is passed to the function then Exception is raised.
    :param args: *args
    :return: integer value that is sum of all the numbers
    '''
    print("***The Number of arguments passed for finding Square are ",len(args))

    #Check if all the arguments are numeric
    try:
        for n in args:
            num = int(n)
    except ValueError:
        print("The Arguments passed in function for finding Square are NOT Numeric")

    #Find the Square of the numbers
    res = []
    for n in args:
        res.append(n**2)
    return res