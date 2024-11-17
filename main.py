def is_prime(num):
    """
    This function determines if a number is a prime number.
    A prime number is greater than 1 and divisible only by 1 and itself.
    """
    if num < 2:
        return False  
    
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0: 

            return False
    return True  

def find_two_digit_primes():
    """
    This function finds and prints all two-digit prime numbers.
    Two-digit numbers range from 10 to 99.
    """
    print("Finding all two-digit prime numbers...\n")
    primes = []  
    
    for num in range(10, 100):  

        if is_prime(num):  

            primes.append(num)  
    
    
    print(f"Total number of two-digit primes: {len(primes)}")
    print("Here are the two-digit prime numbers:")
    

    for i in range(0, len(primes), 10):  

        print(", ".join(map(str, primes[i:i+10])))
    
    print("\nTask complete! You now have a list of all two-digit primes.")

if __name__ == "__main__":
    find_two_digit_primes()
