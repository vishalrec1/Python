from MathPckg import Sum,Multiply,Square,SquareRoot,Cube
#import the Functions from the file(or module) MathPckg.py

print("********THIS CALCULATOR CAN PERFORM OPERATIONS ON MULTIPLE NUMBERS AT A TIME**********\n")

print("Enter the Numbers one by one (press enter after each number). Press 'n' or 'N for exit")
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
t_num = tuple(num)
print(t_num)

#DEFINE DICTIONARY OF FUNCTIONS THAT ARE DEFINED IN MODULE MathPckg.py
ops = {'A': Sum,'C':Cube,'M':Multiply,'R':SquareRoot,'S':Square}

print("Please select the Calculation option below that you want to do : \n")
print("Options are  A : Addition \n"
      "             C : Cube \n"
      "             M : Multiplication \n"
      "             R : Square Root\n"
      "             S : Square")
while(True):
      o = input("Selected Option is : ")
      if o not in ops.keys():
            print("You have not entered correct option. Please choose correct option from the list mentioned above")
      else:
            print("Selected Option is : ",o)
            break

res = ops[o](*t_num) #PLEASE NOTE THAT WE NEED TO USE * TO "UNPACK" THE TUPLE INTO INDIVIDUAL ARGUMENTS
print(res)
