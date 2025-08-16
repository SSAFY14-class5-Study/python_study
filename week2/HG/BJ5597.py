# 과제 안 내신분
# 시간복잡도 : O(1)	
not_sbmt = []
sbmt = []
students = []
#전체 학생 명단 생성
for i in range(1,31):
    students.append(i)
    
for j in range(1,29):
    n = int(input())
    sbmt.append(n)

for student in students: #student 는 작명임(i) 같은
    if student not in sbmt: # students를 반복순회하면서  sbmt에 student가 있니?
        not_sbmt.append(student)

print(not_sbmt[0])
print(not_sbmt[1])
