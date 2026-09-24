#Defining Values 
First_Num , Second_Num = -1, -1

#Getting Values From User and handling error
while int(First_Num) <= 0 and int(Second_Num) <= 0:
     user_input = input("Enter two Positive real numbers seperated By comma: Exp(20,10) ")
     First_Num, Second_Num = user_input.split(',') #String Error handling
     if not First_Num.isdigit() or not Second_Num.isdigit():
          print("Wrong input, please enter numbers only")
          First_Num , Second_Num = -1, -1
     elif int(First_Num) <= 0 or int(Second_Num) <= 0: #Negative input handling
          print("Wrong input, please enter positive numbers only")

#Determaning the higher and the Lower value
Higher_Value, Lower_Value = max(int(First_Num), int(Second_Num)), min(int(First_Num), int(Second_Num))

#Finding the GREATEST COMMON DIVISOR
while Lower_Value != 0:
     Higher_Value, Lower_Value = Lower_Value , Higher_Value % Lower_Value

#Printing the result
print(f"The GREATEST COMMON DIVISOR for {First_Num} and {Second_Num} is {Higher_Value}.")


'''This Could give you the greatest common divisor using while loob.

However (gcd) from math library can be used to get the same result more efficiency'''
