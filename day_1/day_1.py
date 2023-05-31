

class Solution:
    def __init__(self):
        with open('input.txt', 'r') as input_file:
            self.data = input_file.read().split('\n\n')
        self.total_calories = []
        self.set_total_calories()

    def set_total_calories(self):
        for items in self.data:
            self.total_calories.append(sum([int(item.strip()) for item in items.split('\n')]))

    def count_calories(self, part):
        if part == 1:
            return max(self.total_calories)
        if part == 2:
            return sum(sorted(self.total_calories)[-3:])


if __name__ == "__main__":
    solution = Solution()
    print(f"Part 1 Solution: {solution.count_calories(1)}")
    print(f"Part 2 Solution: {solution.count_calories(2)}")
