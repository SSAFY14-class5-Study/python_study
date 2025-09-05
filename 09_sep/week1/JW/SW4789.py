# 4789. 성공적인 공연 기획

T= int(input())

for tc in range(1, T+1):
    people = list(map(int, input()))
    
    result_cnt = 0      # 고용할 사람의 수
    applaud_cnt = 0     # 박수치는 사람의 수

    # 1번 인덱스부터 점검
    for i in range(len(people)-1):
        # i = people의 인덱스 값 = i+1번째 숫자 만큼의 사람이 박수치기 위해 필요한 사람의 수(조건)
        applaud_cnt += people[i]

        if applaud_cnt < i+1:
            result_cnt += i+1 - applaud_cnt
            applaud_cnt += i+1 - applaud_cnt
    
    print(f'#{tc} {result_cnt}')
    