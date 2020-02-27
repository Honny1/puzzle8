from .node import Node
import math
import sys
from collections import deque


class Puzzle:
    def __init__(self, start, goal):
        self.goal = goal
        if len(start) == len(goal):
            self.n = len(start)
        else:
            raise Exception("Start and goal are not the same")
        self.start = Node(start, 0, 0)
        self.start.score = self.score(self.start)

    def score(self, node):
        node.score = self.calc_different_between_goal_node(
            node.data)
        return node.score

    def calc_different_between_goal_node(self, data):
        temp = 0
        for i in range(self.n):
            for j in range(self.n):
                if data[i][j] != self.goal[i][j] and data[i][j] != 0:
                    temp += 1
        return temp

    def is_solvable(self, data):
        values = []
        for i in range(self.n):
            for j in range(self.n):
                values.append(data[i][j])
        count = 0
        for i in range(len(values) - 1):
            for j in range(i, len(values)):
                if (values[i] > values[j] and
                        values[j] != 0):
                    count += 1
        return count % 2 != 1

    def get_best(self, items):
        out = []
        x = min(self.score(j) for j in items)
        for i in items:
            if self.score(i) == x:
                out += [i]
        return out

    def translate(self, nodes):
        nodes.reverse()
        out = []
        for node in nodes:
            out.append(node.data)
        return out

    def process(self):
        if self.is_solvable(self.start.data):
            temp_solution = [self.start.data]
            explored_set = self.start.expand_children()
            while True:
                for i in explored_set:
                    explored_set += i.expand_children()
                    x = self.get_best(explored_set).pop()
                    if x.data == self.goal:
                        return self.translate(x.parents)
                    elif x.data not in temp_solution:
                        temp_solution += [x.data]
                        explored_set = x.expand_children()
                    else:
                        explored_set.pop(explored_set.index(x))
        return None
