def is_even(num):
    return num % 2 == 0


def parity(num):
    return "even" if is_even(num) else "odd"


def armstrong(num):
    power = len(str(num))
    num_list = [int(digit) for digit in str(num)]

    return sum([n**power for n in num_list]) == num


def num_props(num):
    """
    Returns a list of properties [odd, even, armstrong] of number num
    """
    props = [parity(num)]
    if armstrong(num):
        props.append("amstrong")

    return props


def is_perfect(n):
    if n <= 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def digit_sum(num):
    return sum([int(digit) for digit in str(num)])


def get_data(num):
    import requests

    endpoint = f"http://numbersapi.com/{num}"
    fun_fact = requests.get(endpoint).text

    return {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": num_props(num),
        "digit_sum": digit_sum(num),
        "fun_fact": fun_fact,
    }
