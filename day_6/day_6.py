from collections import Counter


class Solution:
    def __init__(self):
        with open('input.txt', 'r') as input_file:
            self.data = input_file.read()

    def count_characters(self, window_length):
        for i in range(len(self.data) - window_length):
            if len(Counter(self.data[i:i + window_length])) == window_length:
                return i + window_length

    def find_start(self, part):
        if part == 1:
            return self.count_characters(4)
        if part == 2:
            return self.count_characters(14)


if __name__ == '__main__':
    solution = Solution()
    print(f"Part 1 Solution: {solution.find_start(1)}")
    print(F"Part 2 Solution: {solution.find_start(2)}")
