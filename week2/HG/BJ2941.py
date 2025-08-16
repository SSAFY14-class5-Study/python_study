# 크로아티아 알파벳

N = input()
arr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
cnt = 0
# replace() 사용해서 3글자 먼저 *로 바꾸기
# 만약 N 문자열의 i에 arr의 알파벳이 있다면

for i in arr:  # 단어 N 안에 arr알파벳이 포함된다면,
    N = N.replace(i, "*")

print(len(N))
