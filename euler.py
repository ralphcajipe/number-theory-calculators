"""
Write a program to calculate Euler's Theorem.

The problem is to find the last two digits of a^b.

The user will need to enter two numbers a and b.
a is the base and b is the exponent.

Example:
base: 33
raised to the power of: 42
"""
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    

def euler_theorem(a, b):
    if gcd(a, 100) == 1:
        return (a ** b) % 100
    else:
        return (a ** (b % 4)) % 100
    
    
def main():
    a = int(input("base: "))
    b = int(input("raised to the power of: "))
    # print("The last two digits of {}^{} is {}".format(a, b, euler_theorem(a, b)))
    # Turn print statement into f-strings
    print(f"The last two digits of {a}^{b} is {euler_theorem(a, b)}")
    
    
if __name__ == "__main__":
    main()