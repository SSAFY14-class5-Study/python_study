while True:
    try: #에러 발생 가능성 있는 코드
        A, B = map(int,input().split())
        print(A+B)
    except EOFError: #함수가 더 이상 읽을 내용이 없어서 발생하는 에러
        break
    except ValueError: #입력 빈줄 들어왔을 떄 발생하는 에러
        break

        
    