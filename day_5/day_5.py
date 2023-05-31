import copy


class Solution:
    def __init__(self):
        with open('input.txt', 'r') as input_file:
            self.data = input_file.read().split('\n\n')
        self.stacks = None
        self.instructions = []
        self.process_input_data()

    def process_input_data(self):
        start = self.data[0].split('\n')
        procedure = self.data[1].split('\n')

        n_stacks = int(start[-1].split()[-1])
        self.stacks = [list() for _ in range(n_stacks)]
        for s in start[-2::-1]:
            crates = s[1::4]
            for i, crate in enumerate(crates):
                if crate != ' ':
                    self.stacks[i].append(crate)

        for p in procedure:
            p = p.split()
            self.instructions.append((int(p[1]), int(p[3]) - 1, int(p[5]) - 1))

    def rearrange_part1(self):
        stacks = copy.deepcopy(self.stacks)
        for number, source, destination in self.instructions:
            stacks[destination].extend(stacks[source][-1:-1 - number:-1])
            stacks[source] = stacks[source][:-number]
        return stacks

    def rearrange_part2(self):
        stacks = copy.deepcopy(self.stacks)
        for number, source, destination in self.instructions:
            stacks[destination].extend(stacks[source][-number:])
            stacks[source] = stacks[source][:-number]
        return stacks

    def rearrange(self, part):
        if part == 1:
            stacks = self.rearrange_part1()
        if part == 2:
            stacks = self.rearrange_part2()
        return ''.join([s[-1] for s in stacks])


if __name__ == '__main__':
    solution = Solution()
    print(f"Part 1 Solution: {solution.rearrange(1)}")
    print(f"Part 2 Solution: {solution.rearrange(2)}")
