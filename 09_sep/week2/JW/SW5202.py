# 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 사용 신청 내역(횟수)
    
    dock = []
    for _ in range(N):
        temp = tuple(map(int, input().split()))
        dock.append(temp)

    # 끝나는 시간 순서대로 정렬
    dock.sort(key=lambda x: (x[1]))
    
    start, end = dock[0]
    dock.pop(0)
    cnt = 1     # 화물차 이용 횟수

    while len(dock) > 0:
        s, e = dock[0]
        if end > s:
            dock.pop(0)
        else:
            start, end = dock[0]
            cnt += 1
            dock.pop(0)
    
    print(f'#{tc} {cnt}')