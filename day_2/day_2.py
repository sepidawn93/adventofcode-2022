

class Solution:
    def __init__(self):
        with open('input.txt', 'r') as input_file:
            self.strategies = input_file.read().split('\n')

    def rock_paper_scissors(self, part):
        if part == 1:
            shape_scores = {'X': 1, 'Y': 2, 'Z': 3}
            outcome_scores = [[3, 6, 0], [0, 3, 6], [6, 0, 3]]
        if part == 2:
            shape_scores = {'X': 0, 'Y': 3, 'Z': 6}
            outcome_scores = [[3, 1, 2], [1, 2, 3], [2, 3, 1]]

        results = [shape_scores[s[2]] + outcome_scores[ord(s[0]) - ord('A')][ord(s[2]) - ord('X')]
                   for s in self.strategies]
        return sum(results)


if __name__ == '__main__':
    solution = Solution()
    print(f"Part 1 Solution: {solution.rock_paper_scissors(1)}")
    print(f"Part 2 Solution: {solution.rock_paper_scissors(2)}")
