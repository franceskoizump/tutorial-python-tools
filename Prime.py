import math

def isPrime(number):
    if number == 0 or number == 1 or number < 0:
        return False
    if number == 2 or number == 3:
        return True
    for i in range(2, int(math.sqrt(number))):
            if number % i == 0:
                return False
    return True


def test_small_2():
    assert isPrime(2) == False

def test_small_3():
    assert isPrime(3) == True

def test_small_21():
    assert isPrime(22) == False
