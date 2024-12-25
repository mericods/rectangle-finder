def isupperleft(i, j, P):
    if j+1 < len(P[0]) and i+1 < len(P):
        if P[i][j+1] == '1' and P[i+1][j] == '1':
            return True
    return False

def islowerright(i, j, P):
    if j > 0 and i > 0:
        if P[i][j-1] == '1' and P[i-1][j] == '1':
            return True
    return False


def possible(P):
    upperlefts = []
    lowerrights = []
    for i in range(len(P)):
        for j in range(len(P[0])):
            if P[i][j] == '1':
                if isupperleft(i,j,P):
                    upperlefts.append((i,j))
                if islowerright(i,j,P):
                    lowerrights.append((i,j))

    possible_rectangles = []
    for ul in upperlefts:
        for lr in lowerrights:
            if (ul[0] < lr[0] - 1) and (ul[1] < lr[1] - 1):
                possible_rectangles.append([ul, lr])

    return possible_rectangles


def rectangle_checker(possible_rectangles, P):
    rectangles = []
    for p in possible_rectangles:

            if '0' not in P[p[0][0]][p[0][1]+2:p[1][1]]:
                if '0' not in P[p[1][0]][p[0][1]:p[1][1]-1]:
                    check1 = 1
                    for y in range(p[0][0], p[1][0]):
                        if (P[y][p[0][1]] == '0') or (P[y][p[1][1]] == '0'):
                            check1 = 0
                            break

                    if check1:
                        check2 = 0
                        for y in range(p[0][0]+1, p[1][0]):
                            if '0' in P[y][p[0][1]+1:p[1][1]]:
                                check2 = 1
                                break
                        if check2:
                            rectangles.append(p)
    return rectangles

def count_rectangles(P):
    possible_rectangles = possible(P)
    rectangles = rectangle_checker(possible_rectangles, P)
    return len(rectangles)
