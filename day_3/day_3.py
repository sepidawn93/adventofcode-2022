

class Solution:
    def __init__(self):
        with open('input.txt', 'r') as input_file:
            self.rucksacks = input_file.read().split('\n')

    @staticmethod
    def get_priority(item):
        if item.islower():
            return ord(item) - ord('a') + 1
        else:
            return ord(item) - ord('A') + 27

    def get_part_1_priorities(self):
        priorities = 0
        for rucksack in self.rucksacks:
            common_items = set(rucksack[:len(rucksack) // 2]).intersection(set(rucksack[len(rucksack) // 2:]))
            priorities += self.get_priority(common_items.pop())

        return priorities

    def get_part_2_priorities(self):
        priorities = 0
        for i in range(0, len(self.rucksacks), 3):
            common_items = set(self.rucksacks[i]).intersection(set(self.rucksacks[i + 1])).intersection(
                self.rucksacks[i + 2])
            priorities += self.get_priority(common_items.pop())

        return priorities

    def prioritize(self, part):
        if part == 1:
            return self.get_part_1_priorities()
        if part == 2:
            return self.get_part_2_priorities()


if __name__ == '__main__':
    solution = Solution()
    print(f"Part 1 Solution: {solution.prioritize(1)}")
    print(f"Part 2 Solution: {solution.prioritize(2)}")
