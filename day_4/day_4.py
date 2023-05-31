

class Solution:
    def __init__(self):
        with open('input.txt', 'r') as input_file:
            self.pairs = input_file.read().split('\n')

        self.partial_overlaps = 0
        self.full_overlaps = 0
        self.count_overlaps()

    def count_overlaps(self):
        for pair in self.pairs:
            p0, p1 = pair.strip().split(',')
            p0_min, p0_max = map(int, p0.split('-'))
            p1_min, p1_max = map(int, p1.split('-'))

            if (p0_min <= p1_min and p0_max >= p1_max) or (p1_min <= p0_min and p1_max >= p0_max):
                self.full_overlaps += 1

            if max(p0_min, p1_min) <= min(p0_max, p1_max):
                self.partial_overlaps += 1

    def find_overlaps(self, part):
        if part == 1:
            return self.full_overlaps
        if part == 2:
            return self.partial_overlaps


if __name__ == '__main__':
    solution = Solution()
    print(f"Part 1 Solution: {solution.find_overlaps(1)}")
    print(f"Part 2 Solution: {solution.find_overlaps(2)}")
