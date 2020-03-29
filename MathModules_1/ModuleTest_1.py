'''
THIS PROGRAM IS A SIMPLE TEST TO LEARN HOW MODULE WORKS.
THERE ARE 5 .py FILES THAT ARE CREATED IN "MathModules_1" FOLDER NAMELY : Square.py, Cube.py, Sum.py, Multiply.py, SquareRoot.py
WE ARE IMPORTING FUNCTIONS FROM EACH OF THE FILE INDIVIDUALLY AND THEN PERFORMING THE CALCULATIONS.
'''

from Sum import Sum
from Cube import Cube
from Multiply import Multiply
from SquareRoot import SquareRoot
from Square import Square

res = Sum(10,20,30,40,50)

print('Sqaure of Numbers are : ',Square(10,20,30,40,50))

print('Sqaure Root of Numbers are : ',SquareRoot(10,20,30,40,50))

print('Cube of Numbers are : ',Cube(10,20,30,40,50))

print('Product of Numbers are : ',Multiply(10,20,30,40,50))