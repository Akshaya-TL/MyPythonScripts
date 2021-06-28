def num_2_digits(num : int) -> [int]:
    if num < 10:
        return [num]
    return num_2_digits(num//10) + [num % 10]

def digits_2_num(given : [int]) -> int:
    if len(given) == 1:
        return given[-1]
    return digits_2_num(given[:-1])*10 + given[-1]

def smallest_number(num : int) -> int:
    return digits_2_num(sorted(num_2_digits(num)))

def largest_number(num : int) -> int:
    given = sorted(num_2_digits(num))[::-1]
    return digits_2_num(given)

def next_kaprekar(num : int)->int:
    return largest_number(num) - smallest_number(num)

def kaprekar_sequence(start : int)-> [int]:
    list_ks = [start]
    while start != next_kaprekar(start):
        list_ks += [next_kaprekar(start)]
        start = next_kaprekar(start)
    return list_ks

print(kaprekar_sequence(1344))
