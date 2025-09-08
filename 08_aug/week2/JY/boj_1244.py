def change_light_state(N, lights, s, num):
    print(lights)
    if s == 1:
        for i in range(1,N+1):
            if i % num == 0:
                lights[i] = 1 -lights[i]
        print(lights)
    else:
        for i in range(num-1,0,-1):
            for j in range(num+1,N+1):
                if lights[i] == lights[j]:
                    lights[i] = 1 -lights[i]
                    lights[j] = 1 - lights[j]
        print(lights)
    return lights




N = int(input())
lights = [0] + list(map(int,input().split()))
students = int(input())
for i in range(students):
    s,num = map(int,input().split())
ans = change_light_state(N,lights, s,num)
print(ans)
