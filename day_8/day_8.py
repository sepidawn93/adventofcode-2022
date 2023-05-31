

class Solution:
    def __init__(self):
        with open('input.txt', 'r') as input_file:
            self.data = input_file.read().split('\n')
        self.heights = [list(map(int, line)) for line in self.data]
        self.rows = len(self.heights)
        self.columns = len(self.heights[0])

    def count_visible_trees(self):
        total = 0
        for i in range(self.rows):
            for j in range(self.columns):
                current_tree = self.heights[i][j]
                up = all(current_tree > self.heights[u][j] for u in range(i))
                down = all(current_tree > self.heights[d][j] for d in range(i + 1, self.rows))
                left = all(current_tree > self.heights[i][l] for l in range(j))
                right = all(current_tree > self.heights[i][r] for r in range(j + 1, self.columns))
                total += up or down or left or right

        return total

    def find_highest_scenic_score(self):
        max_score = 0
        for i in range(self.rows):
            for j in range(self.columns):
                current_tree = self.heights[i][j]
                up = down = left = right = 0

                for u in range(i - 1, -1, -1):
                    up += 1
                    if current_tree <= self.heights[u][j]:
                        break
                for d in range(i + 1, self.rows):
                    down += 1
                    if current_tree <= self.heights[d][j]:
                        break
                for l in range(j - 1, -1, -1):
                    left += 1
                    if current_tree <= self.heights[i][l]:
                        break
                for r in range(j + 1, self.columns):
                    right += 1
                    if current_tree <= self.heights[i][r]:
                        break

                max_score = max(max_score, up * down * left * right)

        return max_score


if __name__ == '__main__':
    solution = Solution()
    print(f"Part 1 Solution: {solution.count_visible_trees()}")
    print(f"Part 2 Solution: {solution.find_highest_scenic_score()}")
