class ReversibleNumbers:
    def __init__(self, limit = 100):
        self.limit = limit
     
    def get_count_of_reversible_numbers(self):
        return len([num for num in range(self.limit) if self.is_reversible_number(num)])

    def rev_num(self, num):
        return int("".join(str(num)[::-1]))

    def is_unique_digits(self, num):
        return len(set(str(num))) == len(str(num))

    def is_reversible_number(self, num):
        if num % 10 == 0 or not self.is_unique_digits(num):
            return False
        return (num + self.rev_num(num)) % 2 != 0
