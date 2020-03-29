'''
THIS PROGRAM IS A SIMPLE CALCULATOR PROGRAM THAT DEMONSTRATES HOW MODULE WORKS.
THERE ARE 5 .py FILES THAT ARE CREATED IN SUBPACKAGE "Functions" INSIDE PACKAGE "MathPckg" NAMELY : Square.py, Cube.py, Sum.py, Multiply.py, SquareRoot.py
WE ARE IMPORTING FUNCTIONS FROM EACH OF THE MODULE INDIVIDUALLY AND THEN PERFORMING THE CALCULATIONS.
WE ARE ASKING USER TO INPUT THE INTEGER NUMBERS. EXCEPTION IS RAISED AND SHOWN TO USER WHEN WRONG INPUT IS PROVIDED.
USER CAN ENTER AS MANY NUMBERS THEY WANT (making use of *args)
USER IS ASKED TO ENTER THE CHOICE OF OPERATION AND BASED ON INPUT THE CORRESPONDING MATH OPS IS PERFORMED. (Functions are stored in Dictionary and called Dynamically without if-else statement)
RESULT OF CALCULATION IS RETURNED IN LIST FOR MULTI VALUES OUTPUT LIKE SQUARE, SQAUREROOT, CUBE
'''

#WE HAVE CREATED PACKAGE "MathPckg" AND SUBPACKAGE "Functions" INSIDE THIS PACKAGE. FIVE FILES ARE PLACED IN THE SUBPACKAGE NAMELY : Square.py, Cube.py, Sum.py, Multiply.py, SquareRoot.py.
#THESE FILES ARE MODULES
from MathPckg.Functions import Sum
from MathPckg.Functions import Cube
from MathPckg.Functions import Multiply
from MathPckg.Functions import SquareRoot
from MathPckg.Functions import Square


print("\n********THIS CALCULATOR CAN PERFORM OPERATIONS ON MULTIPLE NUMBERS AT A TIME**********\n")

print("Enter the Numbers one by one (press enter after each number). Press 'n' or 'N for exit\n")
num = []
n = 0
while(True):
      try:
            n = input("Please Enter Number : ")
            num.append(int(n))
      except ValueError:
            if n == 'N' or n == 'n':
                  break
            else:
                  print("The value of n is ",n)
                  print("The Entered Value is NOT Numeric")

#CONVERTING LIST TO TUPLE FOR PASSING TO THE FUNCTION
t_num = tuple(num)

print('\nThe Numbers Entered by Users are : ',t_num,'\n')

#DEFINE DICTIONARY OF OPERATIONS
#SINCE FUNCTIONS ARE IN MODULES, WE NEED TO CALL THE FUNCTIONS IN THIS CASE USNG . NOTATION i.e. <module>.<function>
ops = {'A': Sum.Sum,'C':Cube.Cube,'M':Multiply.Multiply,'R':SquareRoot.SquareRoot,'S':Square.Square,'a': Sum.Sum,'c':Cube.Cube,'m':Multiply.Multiply,'r':SquareRoot.SquareRoot,'s':Square.Square,'Q':'Quit','q':'Quit'}

while(True):
      print("Please select from the Calculation options below that you want to perform : \n")
      print("Options are  A/a : Addition \n"
            "             C/c : Cube \n"
            "             M/m : Multiplication \n"
            "             R/r : Square Root\n"
            "             S/s : Square\n"
            "             Q/q : Quit\n"
            )
      while(True):
            o = input("Selected Option is : ")
            if o not in ops.keys():
                  print("You have not entered correct option. Please choose correct option from the list mentioned above")
            else:
                  #print("Selected Option is : ",o)
                  break
      if o =='Q' or o == 'q':
            print('\n*****EXITING FROM THE CALCULATOR********')
            break
      res = ops[o](*t_num)
      print(res,'\n\n')
