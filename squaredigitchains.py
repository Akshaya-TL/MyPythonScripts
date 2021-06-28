class SquareDigitChains:

    def get_square_digit_chain(self, num = 44):
        self.num = num
        if self.num == 1:
            return [1, 1]
        elif self.num == 89:
            return [89, 145, 42, 20, 4, 16, 37, 58, 89]
        return [self.num] + self.get_square_digit_chain(self.next_square_digit(self.num))

    def get_count_ends_with(self, endnum = 89, count = 101):
        return [self.get_square_digit_chain(x)[-1] == endnum for x in range(1, count)].count(True)

    def next_square_digit(self, num):
        return sum(map(lambda x: int(x) ** 2, str(num)))
