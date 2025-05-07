import math

def tamsil(x_degrees, terms=10):
    
    x_radians = math.radians(x_degrees)
    result = 0
    for n in range(1, terms + 1):
        result += ((-1) ** n) * (x_radians ** (2 * n)) / math.factorial(2 * n)
    return result


x_degrees = 60  # Nilai dalam derajat
cos_x = tamsil(x_degrees, terms=10)
print(f"cos(60 derajat) dari n = 1 hingga n = 10 : {cos_x}")