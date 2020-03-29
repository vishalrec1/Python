'''
THIS PROGRAM IS A SIMPLE CALCULATOR PROGRAM THAT DEMONSTRATES HOW MODULE WORKS.
THERE ARE 5 .py FILES THAT ARE CREATED IN "MathModules_1" FOLDER NAMELY : Square.py, Cube.py, Sum.py, Multiply.py, SquareRoot.py
WE ARE IMPORTING FUNCTIONS FROM EACH OF THE FILE INDIVIDUALLY AND THEN PERFORMING THE CALCULATIONS.
WE ARE ASKING USER TO INPUT THE INTEGER NUMBERS. EXCEPTION IS RAISED AND SHOWN TO USER WHEN WRONG INPUT IS PROVIDED.
USER CAN ENTER AS MANY NUMBERS THEY WANT (making use of *args)
USER IS ASKED TO ENTER THE CHOICE OF OPERATION AND BASED ON INPUT THE CORRESPONDING MATH OPS IS PERFORMED. (Functions are stored in Dictionary and called Dynamically without if-else statement)
RESULT OF CALCULATION IS RETURNED IN LIST FOR MULTI VALUES OUTPUT LIKE SQUARE, SQAUREROOT, CUBE
'''

from Sum import Sum
from Cube import Cube
from Multiply import Multiply
from SquareRoot import SquareRoot
from Square import Square


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
ops = {'A': Sum,'C':Cube,'M':Multiply,'R':SquareRoot,'S':Square,'a': Sum,'c':Cube,'m':Multiply,'r':SquareRoot,'s':Square,'Q':'Quit','q':'Quit'}

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