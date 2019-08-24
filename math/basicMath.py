from fractions import Fraction

def complex_magnitude(a):
    return (a.imag ** 2 + a.real ** 2) ** 0.5

f = Fraction(3,4)

print("This is a Fraction:",f)


print("Now, lets work with complex numbers, represent then by using j\n e.g a = 3 +3j instead of i (mathematical way)")

complex_number = 3 + 5j

print(complex_number)
print(type(complex_number))
print("Magnitude of this complex number:", complex_magnitude(complex_number))
print("Magnitude of this complex number:", abs(complex_number))
