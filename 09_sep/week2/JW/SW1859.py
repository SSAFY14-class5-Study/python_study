# 1859. 백만 장자 프로젝트

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    price_list = list(map(int, input().split()))    # 날짜별 매매가
    result = 0  # 최대 이익
    max_price = 0

    # 가격 확인 순서 : 뒤 -> 앞
    for i in range(N-1, -1, -1):
        # 최고 매매가 갱신
        if max_price < price_list[i]:
            max_price = price_list[i]
        else:
            result += max_price - price_list[i]
    
    print(f'#{tc} {result}')