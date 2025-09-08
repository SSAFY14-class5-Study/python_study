def rectangle_union_area(rects):
    covered =[[0]*101 for _ in range(101)]
    
    for x1,y1,x2,y2 in rects:
        for x in range(x1,x2):
            for y in range(y1,y2):
                covered[x][y] = 1
    count = 0
    for i in range(101):
        for j in range(101):
            if covered[i][j] == 1:
                count += 1

    return count

rects=[list(map(int,input().split()))for _ in range(4)]
print(rectangle_union_area(rects))