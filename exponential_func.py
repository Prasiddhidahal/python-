#print(2**3) #2^3

def reise_to_power(base_number, pow_number):
    result =1
    for i in range(pow_number):
        result *= base_number
    return result

print(reise_to_power(2,7))