dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def mark(maze, pos):                        #mark the position has been there
    maze[pos[0]][pos[1]] = 2

def passable(maze, pos):                    #judge the next position is the possibale way to go
    return maze[pos[0]][pos[1]] == 0

def find_path(maze, pos, end):
    mark(maze, pos)
    #print(pos)
    if pos == end:
        print(pos, end = '\n')
        return True
    for i in range(4):
        next_pos = pos[0] + dir[i][0], pos[1] + dir[i][1]
        if passable(maze, next_pos):
            if find_path(maze,next_pos,end):
                print(pos, end  = '\n')
                return True
    return False

'''
    迷宫的回溯法实现
    采用栈来实现
'''
from quene import *

def maze_stack(maze, start, end):
    if start == end:
        print(start)
        return
    st = SStack()
    mark(maze, start)
    st.push((start,0))
    while not st.is_empty():
        pos, nxt = st.pop()
        for i in range(nxt,4):
            next_pos = pos[0] + dir[i][0], pos[1] + dir[i][1]
            if next_pos == end:
                print_path(end, pos, st)
                #print(end,'\n', pos)
                #while not st.is_empty():
                return
            if passable(maze,next_pos):
                st.push((pos, i + 1))
                mark(maze, next_pos)
                st.push((next_pos, 0))
                break
    print('no path to end')

def print_path(end, pos, st):
    print(end,end = '\n')
    print(pos,end = '\n')
    while not st.is_empty():
        x, nex = st.pop()
        print(x)
    return

if __name__ == '__main__':
    maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,1,1,0,0,0,1,0,0,0,1],
            [1,0,1,0,0,0,0,1,0,1,0,1,0,1],
            [1,0,1,0,1,1,1,1,0,1,0,1,0,1],
            [1,0,1,0,0,0,0,0,0,1,1,1,0,1],
            [1,0,1,1,1,1,1,1,1,1,0,0,0,1],
            [1,0,1,0,0,0,0,0,0,0,0,1,0,1],
            [1,0,0,0,1,1,1,0,1,0,1,1,0,1],
            [1,0,1,0,1,0,1,0,1,0,1,0,0,1],
            [1,0,1,0,1,0,1,0,1,1,1,1,0,1],
            [1,0,1,0,0,0,1,0,0,1,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    pos, start = (1,1),(1,1)
    #print(maze)
    end = (10,12)
    maze_stack(maze,start,end)
    print(maze)
    #find_path(maze,pos,end)