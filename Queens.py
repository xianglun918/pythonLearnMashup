# Method 2 - 递归求解
import copy

dimension = 8
total = 0
q_list = list()
start = 0


# 接收一个 list 并返回检查值，作用与Method1中相同
def conflict(i_list):

    list_len = len(i_list)
    plus_list = list()
    minus_list = list()
    for i in range(list_len):
        plus_list.append(i_list[i] + i)     # 存放 y+x 的值
        minus_list.append(i_list[i] - i)    # 存放 y-x 的值
    for i in range(list_len - 1):           # 如若任何两个元素 y 或 y+x 或 y-x 的值相等，返回冲突
        if plus_list[i] == plus_list[i+1]:
            return True
        if minus_list[i] == minus_list[i+1]:
            return True
    for i in q_list:
        if i_list.count(i) > 1:
            return True
    return False                            # 反之不冲突


# 顺序寻找第一个符合要求的Q_list
def queens(row, pos):                       # row 是判断的行，pos 是该行开始判断的点
    global total, q_list, start
    total += 1
    if row == dimension:                    # 如果满 8 行输出得到的 list
        return q_list
    else:                                   # 未满 8 行，判断 list 是否合法
        for i in range(pos, dimension):     # 从该行检测位置一直检测到 8 如果有合法的值，检测下一行
            q_list.append(i)
            if not conflict(q_list):        # 合法
                print('No conflict. Processing to next line. Current list: ', q_list)
                return queens(row + 1, 0)   # 检测下一行
            else:                           # 不合法，测试下一个位置
                print('Conflict occurs. Trying next pos. Current list: ', q_list)
                q_list = q_list[:len(q_list)-1]
                continue

        # 当前行没有合法值，退回前一行或者前两行
        start = q_list[-1]
        print('No proper value found. Back to check last row.', q_list, ' Start: ', start)
        if start < 7:                       # 如果前一行的已检测到的合法值 < 7, 测试该行下一个位置
            start += 1
            q_list = q_list[:len(q_list)-1]
            return queens(row - 1, start)

        else:                               # 如何前一行的已检测值 = 7，再退回一行，检测该行的下一个位置
            start = q_list[-2]
            q_list = q_list[:len(q_list)-2]
            return queens(row - 2, start + 1)


def main():     # 展示找到的 Q_list
    r_list = queens(0, 0)
    display_str = list()
    line = list()
    display = list()
    for i in range(dimension):
        display_str.append('')
        line.append(' ')
    print(r_list)
    for i in range(dimension):          # 以下是为了方便展示对于 list 的处理
        display.append(copy.copy(line))
        display[i][r_list[i]] = 'Q'
        for j in range(0, dimension*2 + 2, 2):
            display[i].insert(j, '|')
        for c in display[i]:
            display_str[i] += c
    for i in display_str:
        print(i)
    print('Number of counts: ', total)


main()

