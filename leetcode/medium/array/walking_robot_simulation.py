from collections import defaultdict
from typing import List, Tuple, Dict, Set


class WalkingRobotSimulation:
    def robot_sim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        >>> sut = WalkingRobotSimulation()
        >>> expected = 49
        >>> actual = sut.robot_sim(commands = [6, -1, -1, 6, -1, -1, 6], obstacles = [[0,0]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 36
        >>> actual = sut.robot_sim(commands = [6, -1, -1, 6], obstacles = [[0,0]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 25
        >>> actual = sut.robot_sim(commands = [4, -1, 3], obstacles = [])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 65
        >>> actual = sut.robot_sim(commands = [4, -1, 4, -2, 4], obstacles = [[2,4]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 81
        >>> actual = sut.robot_sim(commands = [2,2,5,-1,-1], obstacles = [[-3,5], [-2,5], [3,2], [5,0], [-2,0], [-1,5], [5,-3], [0,0], [-4,4], [-3,4]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 4328
        >>> actual = sut.robot_sim(commands = [3,2,4,1,-2,-1,-1,3,8,7,5,-2,5,9,-2,8,3,-1,8,7,-2,7,-2,7,4,9,5,7,9,9,-1,2,-1,-1,-2,-1,8,-1,7,-1,2,6,6,3,-1,7,5,4,4,1,-2,9,4,-2,5,7,-2,-2,5,4,3,8,-2,5,5,6,6,6,8,-1,1,-1,-1,6,3,5,8,2,-1,7,-2,8,-2,-2,2,4,-1,-1,-2,3,4,-2,1,9,-1,-2,4,7,5,9], obstacles = [[39,83],[1,30],[-62,-88],[-82,-65],[81,-88],[-100,-74],[-33,64],[96,-15],[91,-71],[27,33],[-66,28],[99,83],[80,3],[-65,-53],[92,-47],[14,-71],[-70,-6],[-42,-31],[92,73],[-47,-59],[-77,-8],[-89,8],[-2,-22],[-95,61],[-76,-75],[5,-52],[81,32],[12,-15],[-69,-20],[81,-77],[-79,-42],[13,-32],[-6,12],[-6,95],[54,-17],[-55,-76],[9,-93],[51,-27],[73,-70],[13,-3],[-72,38],[8,56],[88,56],[62,16],[-5,-94],[-55,31],[-21,69],[-32,82],[-80,60],[-1,54],[-52,22],[30,52],[-35,-55],[-100,75],[98,10],[-67,41],[44,38],[18,-29],[73,0],[-29,-62],[-27,-67],[-42,-64],[-60,20],[-32,18],[60,-89],[-31,98],[-27,85],[53,-38],[-58,-33],[9,-9],[-66,-26],[72,46],[49,99],[58,-80],[-10,-76],[-22,13],[-34,100],[-31,-43],[89,-95],[52,-49],[61,-5],[20,-94],[-42,79],[-39,-60],[-70,39],[-21,-10],[-41,51],[-21,-51],[82,97],[-81,-77],[39,63],[24,96],[-73,36],[88,-92],[-84,27],[-33,78],[96,7],[-19,10],[19,-40],[-94,-25],[32,52],[42,-22],[77,65],[-64,-4],[93,94],[21,89],[-90,9],[-74,-33],[-30,-13],[35,2],[-38,84],[-29,96],[73,57],[-43,-9],[-9,-86],[50,-64],[24,-83],[2,18],[-96,52],[77,71],[-93,-57],[-88,-40],[85,-40],[2,-45],[1,47],[89,19],[-27,40],[-6,-39],[40,-19],[35,87],[88,-37],[31,-79],[33,8],[-2,56],[25,16],[-60,-9],[-7,-23],[-24,86],[-79,79],[80,-69],[10,-21],[-93,-25],[23,-59],[-81,-50],[-2,-46],[-64,-91],[82,25],[24,8],[-59,53],[-94,61],[-18,-67],[47,34],[77,11],[11,-81],[84,29],[-61,-12],[-94,41],[-56,-1],[-79,10],[-32,67],[17,45],[-11,-4],[44,66],[-98,-55],[67,43],[-28,-80],[72,-97],[-86,-99],[1,43],[-75,-72],[-24,-92],[-42,-44],[38,33],[-64,-12],[-82,-60],[38,-51],[71,-47],[40,42],[-85,60],[-46,-61],[-25,17],[-13,-17],[21,84],[-56,-72],[95,67],[-28,73],[53,-4],[-14,-92],[21,-43],[82,-63],[-98,42],[65,-97],[-78,72],[54,65],[44,-15],[-88,7],[23,-62],[-8,-6],[-11,-93],[43,81]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        v_x, v_y = 0, 1  # direction
        p_x, p_y = 0, 0
        max_distance: int = 0

        obstacles_by_x: Dict[int, Set[int]] = defaultdict(set)
        obstacles_by_y: Dict[int, Set[int]] = defaultdict(set)

        # gathering obstacle statistics
        for obstacle in obstacles:
            obstacles_by_x[obstacle[0]].add(obstacle[1])
            obstacles_by_y[obstacle[1]].add(obstacle[0])

        # processing commands
        for command in commands:
            if command in [-1, -2]:
                v_x, v_y = self.rotate(v_x, v_y, command)
            else:
                # moving
                for _ in range(command):
                    p_x += v_x
                    p_y += v_y
                    if (p_x in obstacles_by_x and p_y in obstacles_by_x[p_x]) or (
                        p_y in obstacles_by_y and p_x in obstacles_by_y[p_y]
                    ):
                        p_x -= v_x
                        p_y -= v_y
                        break
                max_distance = max(max_distance, p_x * p_x + p_y * p_y)
        return max_distance

    def rotate(self, x: int, y: int, command: int) -> Tuple[int, int]:
        new_x, new_y = x, y
        if command == -1:  # turn right 90 degrees
            if x == 0:
                if y == 1:
                    new_x, new_y = 1, 0
                elif y == -1:
                    new_x, new_y = -1, 0
            else:  # y is 0
                if x == 1:
                    new_x, new_y = 0, -1
                elif x == -1:
                    new_x, new_y = 0, 1
        elif command == -2:  # turn left 90 degrees
            if x == 0:
                if y == 1:
                    new_x, new_y = -1, 0
                elif y == -1:
                    new_x, new_y = 1, 0
            else:  # y is 0
                if x == 1:
                    new_x, new_y = 0, 1
                elif x == -1:
                    new_x, new_y = 0, -1

        return new_x, new_y

    def robot_sim_opt(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        >>> sut = WalkingRobotSimulation()
        >>> expected = 49
        >>> actual = sut.robot_sim_opt(commands = [6, -1, -1, 6, -1, -1, 6], obstacles = [[0,0]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 36
        >>> actual = sut.robot_sim_opt(commands = [6, -1, -1, 6], obstacles = [[0,0]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 25
        >>> actual = sut.robot_sim_opt(commands = [4, -1, 3], obstacles = [])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 65
        >>> actual = sut.robot_sim_opt(commands = [4, -1, 4, -2, 4], obstacles = [[2,4]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 81
        >>> actual = sut.robot_sim_opt(commands = [2,2,5,-1,-1], obstacles = [[-3,5], [-2,5], [3,2], [5,0], [-2,0], [-1,5], [5,-3], [0,0], [-4,4], [-3,4]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 4328
        >>> actual = sut.robot_sim_opt(commands = [3,2,4,1,-2,-1,-1,3,8,7,5,-2,5,9,-2,8,3,-1,8,7,-2,7,-2,7,4,9,5,7,9,9,-1,2,-1,-1,-2,-1,8,-1,7,-1,2,6,6,3,-1,7,5,4,4,1,-2,9,4,-2,5,7,-2,-2,5,4,3,8,-2,5,5,6,6,6,8,-1,1,-1,-1,6,3,5,8,2,-1,7,-2,8,-2,-2,2,4,-1,-1,-2,3,4,-2,1,9,-1,-2,4,7,5,9], obstacles = [[39,83],[1,30],[-62,-88],[-82,-65],[81,-88],[-100,-74],[-33,64],[96,-15],[91,-71],[27,33],[-66,28],[99,83],[80,3],[-65,-53],[92,-47],[14,-71],[-70,-6],[-42,-31],[92,73],[-47,-59],[-77,-8],[-89,8],[-2,-22],[-95,61],[-76,-75],[5,-52],[81,32],[12,-15],[-69,-20],[81,-77],[-79,-42],[13,-32],[-6,12],[-6,95],[54,-17],[-55,-76],[9,-93],[51,-27],[73,-70],[13,-3],[-72,38],[8,56],[88,56],[62,16],[-5,-94],[-55,31],[-21,69],[-32,82],[-80,60],[-1,54],[-52,22],[30,52],[-35,-55],[-100,75],[98,10],[-67,41],[44,38],[18,-29],[73,0],[-29,-62],[-27,-67],[-42,-64],[-60,20],[-32,18],[60,-89],[-31,98],[-27,85],[53,-38],[-58,-33],[9,-9],[-66,-26],[72,46],[49,99],[58,-80],[-10,-76],[-22,13],[-34,100],[-31,-43],[89,-95],[52,-49],[61,-5],[20,-94],[-42,79],[-39,-60],[-70,39],[-21,-10],[-41,51],[-21,-51],[82,97],[-81,-77],[39,63],[24,96],[-73,36],[88,-92],[-84,27],[-33,78],[96,7],[-19,10],[19,-40],[-94,-25],[32,52],[42,-22],[77,65],[-64,-4],[93,94],[21,89],[-90,9],[-74,-33],[-30,-13],[35,2],[-38,84],[-29,96],[73,57],[-43,-9],[-9,-86],[50,-64],[24,-83],[2,18],[-96,52],[77,71],[-93,-57],[-88,-40],[85,-40],[2,-45],[1,47],[89,19],[-27,40],[-6,-39],[40,-19],[35,87],[88,-37],[31,-79],[33,8],[-2,56],[25,16],[-60,-9],[-7,-23],[-24,86],[-79,79],[80,-69],[10,-21],[-93,-25],[23,-59],[-81,-50],[-2,-46],[-64,-91],[82,25],[24,8],[-59,53],[-94,61],[-18,-67],[47,34],[77,11],[11,-81],[84,29],[-61,-12],[-94,41],[-56,-1],[-79,10],[-32,67],[17,45],[-11,-4],[44,66],[-98,-55],[67,43],[-28,-80],[72,-97],[-86,-99],[1,43],[-75,-72],[-24,-92],[-42,-44],[38,33],[-64,-12],[-82,-60],[38,-51],[71,-47],[40,42],[-85,60],[-46,-61],[-25,17],[-13,-17],[21,84],[-56,-72],[95,67],[-28,73],[53,-4],[-14,-92],[21,-43],[82,-63],[-98,42],[65,-97],[-78,72],[54,65],[44,-15],[-88,7],[23,-62],[-8,-6],[-11,-93],[43,81]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        obstacles_s: Set[Tuple[int, int]] = set((x, y) for x, y in obstacles)
        directions = {
            0: (0, 1),  # north
            1: (1, 0),  # east
            2: (0, -1),  # south
            3: (-1, 0),  # west
        }
        max_dist: int = 0
        x, y, d = 0, 0, 0
        for cmd in commands:
            if cmd == -2:  # turn left
                d = (d - 1) % len(directions)
            elif cmd == -1:  # turn right
                d = (d + 1) % len(directions)
            else:  # go straight
                for _ in range(cmd):
                    dx, dy = directions[d]
                    if (x + dx, y + dy) in obstacles_s:
                        break
                    x += dx
                    y += dy
                max_dist = max(max_dist, x**2 + y**2)
        return max_dist


if __name__ == "__main__":
    import doctest

    doctest.testmod()
