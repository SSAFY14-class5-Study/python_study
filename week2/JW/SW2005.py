# 파스칼의 삼각형

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 비어있는 파스칼 삼각형 리스트(기본 숫자 : 1) 생성
    pascal = []
    for i in range(1, N + 1):
        temp_arr = [1] * i
        pascal.append(temp_arr)

    # 좌표 돌아가며 숫자 더하기
    for r in range(2, N):
        for c in range(1, r):
            pascal[r][c] = pascal[r - 1][c - 1] + pascal[r - 1][c]

    # 결과 출력
    print(f"#{tc}")
    for i in range(N):
        print(*pascal[i])  # 언패킹 사용
        # print(" ".join(map(str, pascal[i])))  # .join 사용
