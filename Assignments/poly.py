def store_pol(n):
    poly = []
    for i in range(n + 1):
        coeff = int(input(f"Give value for coefficient for x^{i}: "))
        poly.append(coeff)
    return poly
 
def display_pol(poly):
    terms = []
    for i, coeff in enumerate(poly):
        if coeff != 0:
            term = f"{coeff}x^{i}"
            terms.append(term)
    polynomial_str = " + ".join(terms)
    print(polynomial_str if polynomial_str else "0")
 
def add_poly(poly1, poly2):
    n = max(len(poly1), len(poly2))
    add = [0] * n
    for i in range(n):
        if i < len(poly1):
            add[i] += poly1[i]
        if i < len(poly2):
            add[i] += poly2[i]
    return add
 
def multiply_poly(poly1, poly2):
    n = len(poly1) + len(poly2) - 1
    multi = [0] * n
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            multi[i + j] += poly1[i] * poly2[j]
    return multi
 
n = int(input("Highest degree of polynomial you want: "))

print("Enter coefficients for the first polynomial:")
poly1 = store_pol(n)
 
print("Enter coefficients for the second polynomial:")
poly2 = store_pol(n)
 
result_add = add_poly(poly1, poly2)
print("Addition of polynomial:")
display_pol(result_add)
 
result_multiply = multiply_poly(poly1, poly2)
print("Multiplication of polynomial:")
display_pol(result_multiply)
