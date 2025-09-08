# 너의 평점은
grede_sum = 0 #학점 x 과목 평점
score_sum = 0 # 학점 총합

grade_list = {'A+':4.5,'A0': 4.0, 'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F': 0}
while True:
    try:
        subject, score, grade = input().split() #str으로 받음
        if grade == 'P':
            continue
        score_sum += float(score)
        grede_sum += float(score) * grade_list[grade]




    except EOFError:
        break

print(float(grede_sum / score_sum)) #나눗셈 연산자. 나머지를 소수점으로 반환