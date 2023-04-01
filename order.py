"""
Program to calculate the Order of an Integer Modulo n.
Definition: Let n > 1 and gcd(a, n) = 1.
The order of a modulo n (in older terminology: the exponent
to which a belongs modulo n) is the smallest positive integer
k such that a^k ≡ 1 (mod n).

Notation used: ord_n(a)
Note: If GCD(a, n) > 1, no solution exists.

User will have two inputs, the first input will be the integer and the second input will be the modulo.

Example:
Integer: 2
Modulo: 7

To find the order of 2 modulo 7, we compute the least positive residues modulo 7 of powers of 2.

2^1 ≡ 2 (mod 7), 2^2 ≡ 4 (mod 7), 2^3 ≡ 1 (mod 7).

Therefore, ord_7(2) = 3.

"""
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
    
def order(a, n):
    if gcd(a, n) > 1:
        return "No solution exists."
    else:
        for k in range(1, n):
            if (a ** k) % n == 1:
                return k
        return "No solution exists."
    
    
"""
Ffunction that shows the solution like this with sentences:

To find the order of 2 modulo 7, we compute the least positive residues modulo 7 of powers of 2.

2^1 ≡ 2 (mod 7), 2^2 ≡ 4 (mod 7), 2^3 ≡ 1 (mod 7).

Therefore, ord_7(2) = 3.
"""
def order_solution(a, n):
    if gcd(a, n) > 1:
        return "To find the order of {} modulo {}, we compute the least positive residues modulo {} of powers of {}.\n" \
               " However, since gcd({a}, {n}) > 1, no solution exists.".format(a, n, n, a, a=a, n=n)
    else:
        solution = "To find the order of {} modulo {}, we compute the least positive residues modulo {} of powers of {}.\n" \
                   "{}^1 ≡ {} (mod {}),".format(a, n, n, a, a, a % n, n)
        for k in range(2, n):
            solution += "{}^{} ≡ {} (mod {}), ".format(a, k, (a ** k) % n, n)
        solution += "{}^{} ≡ 1 (mod {}). ".format(a, n, n)
        solution += "\n\nTherefore, ord_{}({}) = {}.".format(n, a, order(a, n))
        return solution
            
        
def main():
    a = int(input("Integer: "))
    n = int(input("Modulo: "))
    # print("ord_{}({}) = {}".format(n, a, order(a, n)))
    # Turn print statement into f-string
    print(f"ord_{n}({a}) = {order(a, n)}")
    print("\n")
    print(order_solution(a, n))
    
    
    
if __name__ == "__main__":
    main()
