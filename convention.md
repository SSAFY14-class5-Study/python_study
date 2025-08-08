# 1. 문제파일 작명 컨벤션

## 1-1. 작명

- 백준 : BJ
- SWEA : SW
- 프로그래머스 : PG

## 1-2. 예시

- 백준 2557
  - BJ2557.py

# 2. 커밋 컨벤션

[이름]'상태' '사이트' '파일이름'

- (있다면) 사유

## 2-1. 커밋 상태

- 반드시 첫글자 대문자
- ':'은 앞은 붙이고 뒤는 띄어쓰기
- 커밋메시지에는 마침표 작성 금지

1. Refactor: `완성` 후 최적화나 코드 수정이 있을 때

- Refactor에는 개행 후 사유 간단히 작성

2. Sol: 일단 완성 했을 때
3. Temp: 임시 저장용 커밋

## 2-2. 커밋 메시지 예시

[혜진] Refactor: BJ2557.py

- 자료구조 스택으로 변경

## 2-3. 스터디 문제 푸는 방법

1. 매주 (월) 또는 초 sync fork (최신 코드로 동기화) 하기

- your repository -> python_study -> sync fork 버튼 클릭
- 문제 1개 당 커밋 1회

** (주의) ** 1커밋에 1개의 파일 단위로 추가, 수정하기

2. fork한 로컬 레포지토리에서 문제 풀고 커밋 여러개 쌓기(일주일동안)

## 2-4. 주 1회 self PR 및 머지

1. 내 원격저장소(fork) 에 푸시 하기

- 1주일 치 작업 끝나면,
  로컬에 쌓아둔 파일을 내 github 원격 저장소로 한번에 보내기

터미널에 git push origin main 명령어 입력

2. 풀 리퀘스트(PR) 작성하기

- 내 github 레포지토리 접속 ->

"Your branch is \_ commits ahead of ..." 메세지 확인 ->

Compare & pull request 버튼 클릭

- (없다면 organization 에 python-study ->

Pull requestes 탭 ->
New pull request 버튼 클릭)

3.  생성된 PR 직접 머지하기

- organization python_study -> Pull requests 탭 클릭

- 코드 충돌 확인

"This branch has no conflicts ..." 메세지 뜨면 정상

- 초록색 Merge pull request 버튼 클릭

- 컨펌 머지 클릭

# 3. SWEA 간단 스니펫

```json
{
  "SWEA": {
    "prefix": "swea",
    "body": [
      "T = int(input())",
      "for test_case in range(1, T + 1):",
      "\t# 여기에 로직을 작성해주세요",
      "\t$0",
      "\n",
      "\tprint(f'#{test_case}')"
    ],
    "description": "SWEA Code Snippet"
  }
}
```
