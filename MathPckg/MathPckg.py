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
    print("The sum of Numbers", args, " is ", sum(args))
    return sum(args)


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

    print("The Product of the Numbers ",args,' is ',product)
    return product




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
    print("The Square of the Numbers ",args,' is ',res)
    return res



from math import sqrt
def SquareRoot(*args):
    '''
    DocString : This Function can take any number of numeric Arguments and return Square Root of the numbers. If any aplhanumeric value is passed to the function then Exception is raised.
    :param args: *args
    :return: integer value that is sum of all the numbers
    '''
    print("***The Number of arguments passed for finding Square Root are ",len(args))

    #Check if all the arguments are numeric
    try:
        for n in args:
            num = int(n)
    except ValueError:
        print("The Arguments passed in function for finding Square Root are NOT Numeric")
    #Find the square root of the numbers
    res = []
    for n in args:
        res.append(sqrt(n))

    print("The Square Root of the Numbers ", args, ' is ', res)
    return res


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

    print("The Cube of the Numbers ", args, ' is ', res)
    return res
