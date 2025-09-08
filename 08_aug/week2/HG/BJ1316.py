# 그룹 단어 체커
# 불리언 배열 26개
# 문자가 연속해서 나타나거나, 각 문자가 전부 다른 단어 찾기
# 0번째 문자, 1번째 문자 0번째 문자와 새로운 문자가 들어올수 있음

# 1. 함수 정의를 먼저 합니다.
def isGroup(word):
    # 각 알파벳이 이미 나왔는지 확인하기 위한 리스트
    bools = [False] * 26 
    
    # 첫 번째 문자는 미리 처리
    pst = word[0] # pst는 이전 문자(previous)를 의미
    bools[ord(pst) - 97] = True

    # 두 번째 문자부터 끝까지 확인
    for i in range(1, len(word)):
        current = word[i]
        
        # 이전 문자와 현재 문자가 다른 경우에만 검사
        if current != pst:
            index = ord(current) - 97 # 4. ord() 사용법 오타 수정
            
            # 이전에 이미 나온 문자라면 그룹 단어가 아님
            if bools[index] == True:
                return False # 함수 종료 및 False 반환
            
            # 처음 나온 문자라면
            else:
                bools[index] = True # 나왔다고 표시
                pst = current       # 이전 문자(pst)를 현재 문자로 갱신

    # for 루프를 무사히 통과했다면 그룹 단어임
    return True

N = int(input())
count = 0 
for tc in range(N):
    if isGroup(word=input()):
        count += 1

print(count)

#word_cnt = 0

# for tc in range(N):
#     word = input()
#     flags = [False] * 26  # 불리언 배열 알파벳 순서대로
#     # 중복 처리
#     a = ord(word[0]) - 97
#     flags[a] = True
#     past = word[0]  # 문자 1개
#     result_flag = 1
#     for i in range(1, len(word)):
#         word_idx = ord(word[i]) - 97
#         if word[i] == past:  # 중복 문자면
#             flags[word_idx] = True
#             continue  # 중복 문자 2개 처리 (모두 True)
#         if flags[word_idx] == False:  # 처음 받는 문자면
#             flags[word_idx] = True
#             past = word[i]
#             continue
#         if flags[word_idx] == True:
#             result_flag=0
#             break
#     word_cnt += result_flag

# print(word_cnt)



