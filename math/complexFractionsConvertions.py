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


try: 
    input_flt_number = float(input("Enter a float number"))
except ValueError:
    print("You entered an invalid value")
    

print("Finding the factors of a number:")

def is_factor(a,b):
    if b % a == 0:
        return True
    else:
        return False

def print_menu():
    print('\n\n1. Kilometers to Miles')
    print('2. Miles to Kilometers')
def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609
    print('Distance in miles: {0}'.format(miles))
def miles_km():
	miles = float(input('Enter distance in miles: '))
	km = miles * 1.609
	print('Distance in kilometers: {0}'.format(km))
if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do?: ')
    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()
