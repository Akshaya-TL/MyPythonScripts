class HoleCount:
    def get_sum_holes(self, limit = 10):
        return sum([self.get_num_hole_count(i) for i in range(limit + 1)])

    def get_num_hole_count(self, num):
        self.num = num
        holes = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1]
        if self.num < 10:
            return holes[self.num]
        return sum([self.get_num_hole_count(int(digits)) for digit in str(self.num)])
