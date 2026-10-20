from random import randint
class Enemy:
    def __init__(self, position):
        self.position = position.copy()
        self.symbol = "G"
class Game:
    def __init__(self):
        self.map_grid = [[0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0]]
        self.distribution_obstacles = randint(3,6)
        self.distribution_energy = randint(1,3)
        for i in range(len(self.map_grid)):
            for j in range(len(self.map_grid[i])):
                if randint(1,10) <= self.distribution_obstacles:
                    self.map_grid[i][j] = "#"
                elif randint(1,10) <= self.distribution_energy:
                    self.map_grid[i][j] = "*"
        self.obstacles_enemies = {"#","G"}
        self.obstacles_player = {"#"}
        self.current_position = [7, 7]
        self.enemies = [Enemy([0, 0]),Enemy([7, 0])]
        self.energy = 100
        self.diff = 4
        self.count = 0
        self.place_actors()
    def place_actors(self):
        self.map_grid[self.current_position[1]][self.current_position[0]] = "@"
        for enemy in self.enemies:
            x, y = enemy.position
            self.map_grid[y][x] = enemy.symbol
    def display_map(self):
        for row in self.map_grid:
            print(" ".join(map(str, row)))
    def game_over(self):
        print("Game Over! Your score is:")
        print(self.count * 10)
    def path_finder(self, enemy_position, current_position):
        hashmap = {tuple(enemy_position): tuple(enemy_position)}
        frontline = [tuple(enemy_position)]
        new_frontline = []
        def path_builder(position, enemy_position):
            path = [position]
            def traceback(position):
                if tuple(position) == tuple(enemy_position):
                    return
                path.append(hashmap[tuple(position)])
                traceback(hashmap[tuple(position)])
            traceback(position)
            path.reverse()
            return path
        def expand_position(position):
            nonlocal new_frontline, hashmap
            if tuple(position) == tuple(current_position):
                return True
            x, y = position
            if y > 0 and (x, y - 1) not in hashmap and (self.map_grid[y-1][x] not in self.obstacles_enemies):
                new_frontline.append((x, y - 1))
                hashmap[(x, y - 1)] = position
            if x > 0 and (x - 1, y) not in hashmap and (self.map_grid[y][x-1] not in self.obstacles_enemies):
                new_frontline.append((x - 1, y))
                hashmap[(x - 1, y)] = position
            if y < 7 and (x, y + 1) not in hashmap and (self.map_grid[y+1][x] not in self.obstacles_enemies):
                new_frontline.append((x, y + 1))
                hashmap[(x, y + 1)] = position
            if x < 7 and (x + 1, y) not in hashmap and (self.map_grid[y][x+1] not in self.obstacles_enemies):
                new_frontline.append((x + 1, y))
                hashmap[(x + 1, y)] = position
            return False
        while frontline:
            for position in frontline:
                if expand_position(position):
                    return path_builder(position, enemy_position)
            frontline = new_frontline.copy()
            new_frontline = []
        return None
    def boundary_check(self, position, movement):
        x, y = position
        movement = movement.lower()
        if movement == "w" and y > 0 and (self.map_grid[y-1][x] not in self.obstacles_player) :
            return [x, y - 1]
        elif movement == "a" and x > 0 and (self.map_grid[y][x-1] not in self.obstacles_player):
            return [x - 1, y]
        elif movement == "s" and y < 7 and (self.map_grid[y+1][x] not in self.obstacles_player):
            return [x, y + 1]
        elif movement == "d" and x < 7 and (self.map_grid[y][x+1] not in self.obstacles_player):
            return [x + 1, y]
        return position
    def valid_map(self):
        for enemy in self.enemies:
            if self.path_finder(enemy.position,self.current_position) == None:
                return False
        return True
    def valid_sequence(self,movement):
        def empty_string(sequence):
            if len(sequence) == 0:
                return True
            return False
        def insufficient_energy(sequence):
            if len(sequence) > self.energy:
                return True
            return False
        if empty_string(movement) == False and insufficient_energy(movement) == False:
            return True
        return False
    def run(self):
        if self.valid_map() == False:
            return False
        self.display_map()
        collectibles_lookup = set()
        while True:
            for pos in collectibles_lookup.copy():
                if pos in {tuple(enemy.position) for enemy in self.enemies}:
                    continue
                self.map_grid[pos[1]][pos[0]] = "*"
                collectibles_lookup.remove(pos)
            trail = set()
            trail_enemy = set()
            movement = input("Enter movement sequence (W/A/S/D): ")
            while self.valid_sequence(movement) != True:
                movement = input("Enter movement sequence (W/A/S/D): ")
            for move in movement:
                old_position = self.current_position.copy()
                new_position = self.boundary_check(self.current_position,move)
                if new_position == old_position:
                    continue
                if any(new_position == enemy.position for enemy in self.enemies):
                    self.game_over()
                    return
                if self.map_grid[new_position[1]][new_position[0]] == "*":
                    self.energy += 25
                self.current_position = new_position
                self.map_grid[old_position[1]][old_position[0]] = "."
                trail.add(tuple(old_position))
                self.energy -= 1
            self.map_grid[self.current_position[1]][self.current_position[0]] = "@"
            for enemy in self.enemies:
                path = self.path_finder(enemy.position,self.current_position)
                if path is None:
                    continue
                i = 1
                steps = 0
                while steps < self.diff and i < len(path):
                    next_position = list(path[i])
                    if next_position == self.current_position:
                        self.game_over()
                        return
                    old_enemy_position = enemy.position.copy()
                    if tuple(old_enemy_position) not in collectibles_lookup:
                        self.map_grid[old_enemy_position[1]][old_enemy_position[0]] = "."
                    else:
                        self.map_grid[old_enemy_position[1]][old_enemy_position[0]] = "*"
                    if self.map_grid[next_position[1]][next_position[0]] == "*":
                        collectibles_lookup.add(tuple(next_position))
                    enemy.position = next_position
                    self.map_grid[enemy.position[1]][enemy.position[0]] = enemy.symbol
                    trail_enemy.add(tuple(old_enemy_position))
                    i += 1
                    steps += 1
            self.display_map()
            for pos in trail:
                self.map_grid[pos[1]][pos[0]] = 0
            for pos in trail_enemy:
                self.map_grid[pos[1]][pos[0]] = 0
            self.place_actors()
            self.count += 1
def restart():
    boolean = input("Want to play again? (Y/N): ")
    if boolean.lower() == "n":
        return False
    elif boolean.lower() == "y":
        return True
    else:
        print("Invalid input!")
        return restart()
while True:
    game = Game()
    if game.run() == False:
        continue
    flag = restart()
    if flag != True:
        break
    