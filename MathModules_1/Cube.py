def Cube(*args):
    '''
    DocString : This Function can take any number of numeric Arguments and return Cube of the numbers. If any aplhanumeric value is passed to the function then Exception is raised.
    :param args: *args
    :return: integer value that is sum of all the numbers
    '''
    print("***The Number of arguments passed for finding Cube are ",len(args))

    #Check if all the arguments are numeric
    try:
        for n in args:
            num = int(n)
    except ValueError:
        print("The Arguments passed in function for finding Cube are NOT Numeric")

    #Find the Cube of the numbers
    res = []
    for n in args:
        res.append(n**3)
    return res