def sum_digits(n):
    if n < 10:
        return n
    else:
        lastDigit = n % 10
        otherDigits = n // 10
        return lastDigit + sum_digits(otherDigits)


number = 25062000
print(f'The sum of all digits from number {number} is {sum_digits(number)}')

