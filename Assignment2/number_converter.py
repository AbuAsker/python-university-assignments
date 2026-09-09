import math

# Condition to repeat if the input is wrong
Trans_Type = ""
while Trans_Type not in ["B", "D"]:
    Trans_Type = input(
        "Enter the type of conversion you want,\nfrom decimal to binary enter B, from binary to decimal enter D: "
    ).upper()
    if Trans_Type not in ["B", "D"]:
        print("The input is wrong, Please Enter D or B\n")

# Converting from decimal to binary
if Trans_Type == "B":
    Decimal = int(input("Enter the Decimal number: "))
    
    if Decimal == 0:
        print("The Binary number is: 0")
    else:
        List_Bi = []
        temp_dec = Decimal
        while temp_dec > 0:
            Remain = temp_dec % 2
            List_Bi.insert(0, Remain)
            temp_dec //= 2
        print("The Binary number is: ", "".join(map(str, List_Bi)))

# Converting from binary to decimal
elif Trans_Type == "D":
    Binary = input("Enter the Binary number: ")
    Decimal = 0
    is_valid = True
    
    for i in range(len(Binary)):
        if Binary[i] not in ['0', '1']:
            print("Invalid binary number. Please enter only 0s and 1s.")
            is_valid = False
            break
        Decimal += int(Binary[i]) * (2 ** (len(Binary) - i - 1))
    
    if is_valid:
        print("The Decimal number is: ", Decimal)
