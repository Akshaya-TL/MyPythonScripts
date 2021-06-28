def rev(num):
    return int(str(num)[::-1])
def square(num):
    return num**2
def is_adam_number(num):
    return square(num) == rev(square(rev(num)))
def adam_numbers(limit):
    for num in range(limit):
        if '0' in str(num):
            continue
    return [x for x in range(1,limit) if is_adam_number(x)]
print(adam_numbers(15))
