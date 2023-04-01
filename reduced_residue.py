"""
Program to calculate the Reduced Residue System Modulo n.

• A set of Ø(n) integers such that each element of the set is relatively prime to
n, and no two different elements of the set are congruent modulo n.
• In mathematics, a subset of R of the integers if:
1. GCD(r, n) = 1 for each r in R
2. R contains Ø(n) elements
3. No two elements of R are congruent modulo n


User will input a number and it will display first the 
Complete residue system modulo n and then it will display
the Reduced residue system modulo n.

Example:
Input: 12
Complete Residue System Modulo 12: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
Reduced residue system modulo 12: {1, 5, 7, 11}
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
    
def complete_residue_system(n):
    residue_system = []
    for i in range(n):
        residue_system.append(i)
    return residue_system


def reduced_residue_system(n):
    residue_system = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            residue_system.append(i)
    return residue_system


def main():
    n = int(input("Input: "))
    # print("Complete Residue System Modulo {}: {}".format(n, complete_residue_system(n)))
    # print("Reduced residue system modulo {}: {}".format(n, reduced_residue_system(n)))
    # Turn print statements into f-strings
    print(f"Complete Residue System Modulo {n}: {complete_residue_system(n)}")
    print(f"Reduced residue system modulo {n}: {reduced_residue_system(n)}")
    
    
if __name__ == "__main__":
    main()
