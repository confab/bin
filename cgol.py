#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import random

class InputError(BaseException):
    pass

class Grid:

    def __init__(self, x, y):
        self.grid = [[0 for i in range(x+2)] for j in range(y+2)]
        self.height = y
        self.width = x
    
    def populate(self, percent):
        for y in range(1, self.height+1):
            for x in range(1, self.width+1):
                if random() < percent:
                    self.grid[y][x] = 1
    
    def populateFromFile(self, f, length):
        with open(f, 'r') as f:
            population = f.readline()
        if len(population) != length**2:
            print('File is of invalid length; must contain %d characters.' % length**2)
        self.grid = [population[i:i+3] for i in range(0, len(population), length)]
            
    
    def display(self, dead=' ', alive='#'):
        key = {1: alive, 0: dead}
        return [''.join([key[j] for j in i[1:-1]]) for i in self.grid[1:-1]]
    
    def generate(self):
        grid_buffer = [[0 for i in range(self.width+2)] for j in range(self.height+2)]
        for y in range(1, self.height+1):
            for x in range(1, self.width+1):
                cell = self.grid[y][x]
                neighbours = [
                                self.grid[y-1][x-1],
                                self.grid[y-1][x],
                                self.grid[y-1][x+1],
                                self.grid[y+1][x-1],
                                self.grid[y+1][x],
                                self.grid[y+1][x+1],
                                self.grid[y][x-1],
                                self.grid[y][x+1]
                             ]
                live_neighbours = neighbours.count(1)
                if cell:
                    if live_neighbours > 1 and live_neighbours < 4:
                        grid_buffer[y][x] = 1
                    else:
                        grid_buffer[y][x] = 0
                else:
                    if live_neighbours == 3:
                        grid_buffer[y][x] = 1
                    else:
                        grid_buffer[y][x] = 0
        self.grid = grid_buffer

############################

import curses

stdscr = curses.initscr()

def setup():

    # Get info for generating CGOL
    max_size = stdscr.getmaxyx()
    curses.echo()
    stdscr.addstr(1, 1, 'Enter number of rows in grid (max is %d):' % (max_size[0]-4))
    y = int(stdscr.getstr(2, 1))
    stdscr.addstr(3, 1, 'Enter number of columns in grid (max is %d):' % max_size[1])
    x = int(stdscr.getstr(4, 1))
    stdscr.addstr(5, 1, 'Enter starting population density (number between 0 and 1):')
    pop = float(stdscr.getstr(6, 1))
    curses.noecho()
#    stdscr.clear()

    # Create CGOL grid
    grid = Grid(x, y)
    grid.populate(pop)

    # Create window for grid
    display = curses.newwin(y+2, x+2, 0, 0)
    display.box()
#    stdscr.refresh()
    
    return grid, display, y

def printGrid(grid, display, y):
    buff = grid.display()
    for i, j in zip(buff, range(1,y+1)):
        display.addstr(j, 1, i)
    display.refresh()
    stdscr.addstr(y+3, 0, 'SPACE = next generation; r = reset; q = quit')
    stdscr.refresh()

def getOpt():
    y_corner, x_corner = [i-1 for i in stdscr.getmaxyx()]    
    opt = stdscr.getch(y_corner, x_corner)
    while (opt != ord(' ')) and (opt != ord('r')) and (opt != ord('q')):
        opt = stdscr.getch(y_corner, x_corner)
    return chr(opt)
    
def run():
    opt = 'r'
    while opt == 'r':
        stdscr.clear()
        grid, display, y = setup()
        printGrid(grid, display, y)
        opt = getOpt()
        while opt == ' ':
            grid.generate()
            printGrid(grid, display, y)
            opt = getOpt()
    stdscr.keypad(0)
    curses.endwin()
    quit()

run()
