# 더하기 사이클

N = int(input())

i = 0
a = 0
b = 0
start = N
while True:
    a = N // 10  # 십의 자리 만약 N이 한자리수라면 0으로 계산됨. 별도 if 문 필요없음
    b = N % 10  # 일의 자리
    sum = a + b  # 사용할 식
    c = sum % 10
    result = b * 10 + c  # 새로 조합한 수
    i += 1
    if result == start:
        print(i)
        break
    N = result #주의 result와 N 값 비교 후에 갱신해야함 위치 주의
