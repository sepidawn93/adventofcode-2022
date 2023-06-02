

class Solution:
    def __init__(self):
        with open('input.txt', 'r') as input_file:
            self.motions = input_file.read().split('\n')
        self.motions = [(motion.split()[0], int(motion.split()[1])) for motion in self.motions]
        self.initial_state = (0, 0)
        self.number_of_knots = 2

    @staticmethod
    def are_adjacent(point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        if abs(x1 - x2) > 1 or abs(y1 - y2) > 1:
            return False
        return True

    @staticmethod
    def move_in_direction(point, direction):
        x, y = point
        direction_mapping = {'U': (x, y + 1),
                             'D': (x, y - 1),
                             'R': (x + 1, y),
                             'L': (x - 1, y)}
        return direction_mapping[direction]

    @staticmethod
    def move_one_step(point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        if x1 < x2:
            x1 += 1
        elif x1 > x2:
            x1 -= 1
        if y1 < y2:
            y1 += 1
        elif y1 > y2:
            y1 -= 1
        return x1, y1

    def follow_motions(self, part):
        if part == 1:
            self.number_of_knots = 2
        if part == 2:
            self.number_of_knots = 10

        visited = set()
        visited.add(self.initial_state)
        knots = [self.initial_state] * self.number_of_knots

        for motion in self.motions:
            direction, steps = motion
            for i in range(steps):
                knots[0] = self.move_in_direction(knots[0], direction)
                for j in range(1, len(knots)):
                    if not self.are_adjacent(knots[j], knots[j-1]):
                        knots[j] = self.move_one_step(knots[j], knots[j - 1])
                    else:
                        break
                visited.add(knots[-1])

        return len(visited)


if __name__ == '__main__':
    solution = Solution()
    print(f"Part 1 Solution: {solution.follow_motions(1)}")
    print(f"Part 2 Solution: {solution.follow_motions(2)}")
