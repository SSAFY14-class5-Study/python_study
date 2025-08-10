# 이진탐색
# 이진탐색 함수
def binarySearch(total_page, target):
    cnt = 0
    left = 1
    right = total_page
 
    while left <= right:
        cnt += 1
        middle = int(left + right) // 2
 
        if middle == target:
            return cnt
        elif middle > target:   # 범위 다시 잡고 시작
            right = middle
        else:
            left = middle
 
    return cnt
 
 
T = int(input())    # 테스트 케이스
 
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
 
    target_A = binarySearch(P, A)
    target_B = binarySearch(P, B)
 
    if target_A < target_B:     # B의 횟수가 더 많으면 A가 이김
        winner = 'A'
    elif target_B < target_A:   # A의 횟수가 더 많으면 B가 이김
        winner = 'B'
    else:                       # 비긴 경우
        winner = 0
 
    # 출력
    print(f"#{tc} {winner}")