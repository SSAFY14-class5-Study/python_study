# 단어 공부

N = list(input().upper())
cnt_arr = [0]* 26

max_idx = -1
max_count = -1

for i in range(0,len(N)): # 0 ~ N까지
    now = ord(N[i]) - 65 # 0부터 시작하는 index로 바꿔주기 위해 
    cnt_arr[now] += 1

    if cnt_arr[now] > max_count:
        max_count = cnt_arr[now]
        max_idx = now #최댓값이 있는 인덱스

result = chr(max_idx+65) # 65부터 시작하는 index로 바꿔줘서 typecasting
flag = False # False : max를 아직 안찾은 상태 True : max를 이미 한 번 찾은 상태
for i in range(0,26):
    if cnt_arr[i] == max_count:
        if flag == False:
            flag = True
            continue
    
        else:
            result = '?'
            break;
    
    # if flag == False and cnt_arr[i] == max_count: #cnt_arr[i]는 count값
    #     flag = True
    #     continue

    # if flag == True and cnt_arr[i] == max_count:
    #     result = '?'
    #     break 

print(result)

# max_idx max_count for문에서 갱신
# 65빼서 0부터 시작하는 알파벳 index 만드는거 (char to int)
# 0부터 시작하는 index에서 65더해서 charactor만들기 (int to char)
# flag로 어려운 제어문
# 제어문에서 continue랑 break 로 흐름 제어
# result로 미리 결과 넣고 제어문에서 갱신해서 답 출력하는 기법

# 주의
# 배열의 [] 안에 idx말고 값 넣지 않기