

class Solution:
    def __init__(self):
        with open('input.txt', 'r') as input_file:
            self.data = input_file.read().split('\n')
        self.total_disk_space = 70000000
        self.required_space = 30000000
        self.file_system = {'/': {'files': [], 'size': 0}}
        self.directories = []
        self.process_input()

    def process_input(self):
        for line in self.data:
            if line.startswith('$ cd'):
                directory = line.split()[-1]
                if directory == '/':
                    self.directories = ['/']
                elif directory == '..':
                    self.directories.pop()
                else:
                    self.directories.append(directory)

            if line.startswith('dir'):
                self.add_directory(line.split()[-1])

            if line.split()[0].isnumeric():
                size, name = line.split()
                self.add_file(name, int(size))

    def get_directory_path(self, partial=None):
        if partial:
            return '/'.join(self.directories[:partial])
        return '/'.join(self.directories)

    def add_directory(self, name):
        directory_path = self.get_directory_path() + '/' + name
        self.file_system[directory_path] = {'files': [], 'size': 0}

    def add_file(self, name, size):
        self.file_system[self.get_directory_path()]['files'].append((name, size))
        for i in range(len(self.directories)):
            self.file_system[self.get_directory_path(i + 1)]['size'] += size

    def find_directories(self, part):
        if part == 1:
            return sum([directory['size'] for directory in self.file_system.values()
                        if directory['size'] <= 100000])
        if part == 2:
            used_space = self.file_system['/']['size']
            free_space = self.total_disk_space - used_space
            delete_space = self.required_space - free_space
            return min([directory['size'] for directory in self.file_system.values()
                        if directory['size'] >= delete_space])


if __name__ == '__main__':
    solution = Solution()
    print(f"Part 1 Solution: {solution.find_directories(1)}")
    print(f"Part 2 Solution: {solution.find_directories(2)}")
