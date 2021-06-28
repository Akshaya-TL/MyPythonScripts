def next_collatz(n : int) -> int:
    if n % 2 != 0:
        return n * 3 +1
    else:
        return n // 2
def collatz_sequence(start : int) -> [int]:
    if start == 4:
        return [4, 2, 1]
    return [start] + collatz_sequence(next_collatz(start))
print(collatz_sequence(2))



