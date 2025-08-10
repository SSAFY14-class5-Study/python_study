T = int(input())    # 테스트 케이스

for tc in range(1, T + 1):
    box = [list(map(int, input().split())) for _ in range(9)]
    valid = 1       # 유효성 검사
 
    # 행 검사
    for row in box:
        if len(set(row)) != 9: 
            valid = 0   
            break
 
    # 열 검사
    if valid:
        for c in range(9):
            col = []    # 열 모으기
            for r in range(9):
                col.append(box[r][c])
 
            if len(set(col)) != 9:
                valid = 0
                break
 
    # 3x3 검사
    if valid:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = []
 
                for r in range(3):
                    for c in range(3):
                        square.append(box[i + r][j + c])
                         
                if len(set(square)) != 9:
                    valid = 0
                    break
    
    # 출력
    print(f"#{tc} {valid}")