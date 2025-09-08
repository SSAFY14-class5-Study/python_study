# [S/W 문제해결 기본] 1일차 - Flatten

for tc in range(1, 11):
    number = int(input())  # 덤프 횟수(평탄화하는 횟수)
    boxes = list(map(int, input().split()))  # 박스 높이

    # 카운트(덤프할 때마다 +1) 초기값을 0으로 설정
    cnt = 0

    while True:
        if cnt == number:  # 덤프 횟수와 카운트 횟수가 같아지면 멈춤
            break

        # max, min 사용하지 않은 버전
        # 각 인덱스 값의 초기값을 0으로 설정
        max_idx = 0
        min_idx = 0
        for i in range(len(boxes)):
            if boxes[max_idx] < boxes[i]:
                max_idx = i
                # ㄴ> 맥스 인덱스에 해당하는 박스 높이가 i번째 박스 높이보다 작다면 맥스 인덱스 값을 i로 바꾼다
            if boxes[min_idx] > boxes[i]:
                min_idx = i

        # max값에 -1, min값에 +1
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        # max, min 사용한 버전
        # boxes[boxes.index(max(boxes))] -= 1
        # boxes[boxes.index(min(boxes))] += 1

        # 한 사이클을 돌면 평탄화 횟수 +1
        cnt += 1

    print(f"#{tc} {max(boxes) - min(boxes)}")
