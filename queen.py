import random

def conflict(pos,row):                                  # 判断当前行上的皇后与之前列有无冲突
    for i in range(row + 1):                            # 之前所有列
        for j in range(i+1,row + 1):                    # 对于当前判断列与之后列
            if pos[i] == pos[j] or abs(i - j) == abs(pos[i] - pos[j]):      #是否位于同一行、列或斜线
                return True                         
    return False

def queen():                                            # 主函数
    num = int(input('input the size(>=4)\n'))         # 输入行数，至少大于3
    pos = [0] * num
    row = 0
    global rol                                          # 存入结果
    rol = []
    count = 0
    calculate(pos, row)     
    #for i in rol:
    #    print(i)
    #    count += 1
    #print(count)
    random_rol = random.choice(rol)
    print(random_rol)
    col_pos = [['#']*num for row in range(num)]
    for x in range(num):
        col_pos[x][random_rol[x]] = '0'
    for x in col_pos:
        print(x)

def calculate(pos, row):                # 计算函数（迭代函数），输入当前操作行与皇后在不同行对应列数的列表
    if row == len(pos):                 # 如果行数到达输入值，即为正确解
        rol.append(tuple(pos))          # 防止结果更改
    else:
        for col in range(len(pos)):     # 可将皇后放入当前操作行的列
            pos[row] = col              
            if not conflict(pos,row):   # 判断当皇后位于当前列时与之前列是否有冲突
                calculate(pos,row + 1)  # 若无冲突则继续对下一列进行操作
                                        # 否则将皇后换列
queen()