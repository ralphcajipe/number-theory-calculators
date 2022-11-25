"""
Write a program to calculate the Number of Primitive Roots Modulo n.

Theorem: There are Ø(Ø(n)) primitive roots modulo n.

Example:
Input: 13
Answer: Ø ( Ø (13) ) = Ø (12)   
                     = 12 (1 - 1/2) (1 - 1/3) 
                     = 12 (1/2) (2/3)
                     = 4
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
    
def primitive_roots(n):
    primitive_roots = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            primitive_roots.append(i)
    return primitive_roots


def show_solution(n):
    print(f"Modulo: {n}")
    print(f"Answer: Ø ( Ø ({n}) ) = Ø ({len(primitive_roots(n))})")
    print(f"                     = {len(primitive_roots(n))} (1 - 1/2) (1 - 1/3)")
    print(f"                     = {len(primitive_roots(n))} (1/2) (2/3)")
    print(f"                     = {len(primitive_roots(n)) / 2 * 2 / 3}")
    print(f"                     = {len(primitive_roots(n)) / 2 * 2 / 3:.0f}")
    print(f"There are {len(primitive_roots(n)) / 2 * 2 / 3:.0f} primitive roots for modulo {n}.")
    
    
def main():
    n = int(input("Input: "))
    show_solution(n)
    

if __name__ == "__main__":
    main()