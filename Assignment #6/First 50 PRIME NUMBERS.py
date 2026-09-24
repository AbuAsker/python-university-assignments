import math

# Defining values
Count = 0                  # Counter for how many primes we have found
Number = 2                 # Start checking from the first possible prime
Numbers_Per_Line = 10      # How many numbers to print per line

# Keep looping until we find 50 prime numbers
while Count < 50:
    # Assume the number is prime until proven otherwise
    Divisor = 2
    Is_Prime = True

    # Check if Number is divisible by any value from 2 up to its square root
    while Divisor <= math.sqrt(Number):
        if Number % Divisor == 0:
            Is_Prime = False   # Found a divisor, so it's not prime
            break
        Divisor += 1

    # If the number is prime, print it and update the count
    if Is_Prime:
        print(Number, end=' ')
        Count += 1

        # Move to a new line after every 10 numbers
        if Count % Numbers_Per_Line == 0:
            print()

    # Move on to check the next number
    Number += 1
