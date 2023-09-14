# s1 = list(input()) # s1 : ['a','b','c','d']
# s2 = input()        #s2: abcd
# # s3 = s1 + s2
# s4 = s2 * 3
# print(s1)
# print(s2)

# s = 'Reverse this string'
# s = s[::-1]
# s = 'abcd'
# s = list(s)
# s.reverse()
# s = ''.join(s)

# def itoa(a):
#     s = ''
#     while a>0:
#         print(a%10)
#         a //= 10
#
# a = 123
# itoa(a)

# # 그나마 중요한 거 같음 reverse, slicing 없이 문자열 뒤집기.
# def itoa(a):
#     s = ''
#     while a>0:
#         s += chr(ord('0') + (a % 10)) #1의 자리 숫자의 ASCII코드값
#         a //= 10
#     return s  # [::-1] 하면 다시 뒤집어짐
# a = 123
# print(itoa(a)) # 321


#
# # KMP 알고리즘
# def kmp(t,p):
#     N = len(t)
#     M = len(p)
#     lps = [0] * (M+1)
#
#     j = 0  # 일치한 개수 == 비교할 패턴 위치
#     lps[0] = -1
#     for i in range(1, M):
#         lps[i] = j      # p[i]이전에 일치한 개수
#         if p[i] == p[j]:
#             j += 1
#         else:
#             j = 0
#     lps[M] = j
#     print(lps)
#
# # 암호화?
# for _ in range(10):
#     tc = int(input())
#     fs = input()
#     s = input()
#     cnt = 0
#     for i in range(len(fs),len(s)):
#         if s[i-len(fs):i] == fs:
#             cnt += 1
#     print(f'#{tc}', cnt)
#

'''
AI의 발전으로 인해 세상의 많은 것이 편해졌다. 하지만 이로 인해 많은 것이 불편해진 것도 있다,
그 중 하나가 바로 사이버 범죄가 너무 많이 일어난다는 것이다.
코코가 개발한 새로운 Captcha Code 생성기는 아래와 같다.
[1] 랜덤으로 N개의 길이의 sample이 주어진다.
[2] 그리고 k개의 길이의 Passcode가 주어진다.
[3] 사용자는 sample에서 passcode를 순차적으로 만들 수 있는지를 검증해야 한다.

코코는 자신이 만든 생성기에 문제가 있는지 없는지 직접 QA과정을 거치려고 한다.
Sample과 Passcode가 주어졌을때, sample에서 passcode를 만들 수 있는지 없는지를 판단하는 프로그램을 작성하라.
'''

# T = int(input())
# for tc in range(1,T+1):
#     N, K = map(int, input().split())
#     Sample = list(map(int, input().split()))
#     passcord = list(map(int, input().split()))
#
#     result = []
#
#     for i in range(N):
#         for j in range(K):
#             if Sample[i] == passcord[j]:
#                 result.append(Sample[i])
#
#         break
#
#     if result == passcord:
#         print(f'#{tc} 1')
#     else:
#         print(f'#{tc} 0')

# # 강사님 풀이
# #
# T = int(input())
# for tc in range(1,T+1):
#     N, K = map(int, input().split())
#     sample = list(map(int, input().split()))
#     passcord = list(map(int, input().split()))
#
#     cnt = 0
#     result = 0
#
#     for i in range(N):
#         if passcord[cnt] == sample[i]:
#             cnt += 1
#         if cnt == K:
#             result = 1
#             break
#     print(f'#{tc} {result}')
#
# # 내장함수 사용한 방법
# T = int(input())
# for tc in range(1,T+1):
#     N, K = map(int, input().split())
#     sample = list(map(int, input().split()))
#     passcord = list(map(int, input().split()))
#
#     indexes = []
#     result = 1
#
#     for i in range(len(passcord)):
#         now = passcord[i]
#         try:
#             index = sample.index(now)
#             sample = sample[index + 1 :]
#         except:
#             result = 0
#     print(f'#{tc} {result}')
'''
2
10 4
1 1 2 2 3 3 4 4 5 5
1 2 3 4  
# 1
7 4
1 2 2 4 3 3 4
4 3 2 1  
# 0

'''

# join과 find를 쓰는 방법도 있음


# # swea 4864 문자열 비교
# T = int(input())
# for tc in range(1, T+1):
#     str1 = input()
#     str2 = input()
#     cnt = 0
#
#     if str1 in str2 :
#         cnt +=1
#
#     print(f'#{tc} {cnt}')

# # if _ in _ 을 쓰지 못할경우
# T = int(input())
# for tc in range(1, T+1):
#     str1 = input()
#     str2 = input()
#
#     result = 0
#     # 두번째 문자열 안에서 첫번째 문자열을 찾는다.
#     for i in range(len(str2) - len(str1)):
#         cnt = 0
#         # 첫번째 문자열 모든 문자 검사
#         for j in range(len(str1)):
#             # 첫번째 문자열의 j번째 와 두번째 문자열의 i+j번째 문자가 일치하는지 확인
#             if str1[j] ==str2[i+j]:
#                 cnt += 1
#         # 카운트가 첫번째 문자열의 길이와 같다면
#         if cnt == len(str1):
#             result = 1
#     print(f'#{tc} {result}')


# # swea 4861 회문 // 다시풀기 출력오류
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(input()) for _ in range(N)]
#     lst = []
#
#     for i in range(N):
#         for j in range(N-M+1):  # 가로줄 내에서 M의 범위를 맞추기 위해서
#             if arr[i][j:M+j] == arr[i][j:j+M][::-1]:  # 가로는 하나의 리스트 이기 때문에 슬라이싱으로 가져옴
#                 lst.append(arr[i][j:M+j])  # 위의 조건이 같은 경우 새 리스트 생성
#
#     for i in range(N-M+1):  # 세로줄 내에서 M의 범위를 맞취기 위해
#         for j in range(N):
#             c_lst = []
#             for k in range(M):  # 세로줄은 하나의 리스트 내용이 아니기 때문에 각 문자를 뽑아 새로운 리스트 작성
#                 c_lst.append(arr[i+k][j])
#                 if c_lst == c_lst[::-1]:  # reverse로 뒤집으면 원본에도 영향이 가기 때문에 슬라이싱으로 뒤집어야함
#                     lst.append(''.join(c_lst))
#
#     print(f'#{tc} {"".join(lst)}')

# # 강사님 풀이
# def find_p(N, M, arr):
#     for i in range(N):
#         for j in range(N - M +1):
#             h = arr[i][j:j+M]
#             v = [arr[k][i] for k in range(j, j+M)]
#             # 회문인지 판별
#             if h == h[::-1]:
#                 return h
#             if v == v[::-1]:
#                 return v
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(input()) for _ in range(N)]
#     result = find_p(N, M, arr)
#     print(f'#{tc}',  ' '.join(result))
#


# # swea 4865 글자수
# T = int(input())
# for tc in range(1, T+1):
#     str1 = input()
#     str2 = input()
#     N = len(str1)
#     M = len(str2)
#     result = 0
#     for i in range(N):
#         cnt = 0
#         for j in range(M):
#             if str1[i] == str2[j]:
#                 cnt += 1
#         if result <= cnt:
#             result = cnt
#     print(f'#{tc} {result}')
#
# # 강사님 풀이
# T = int(input())
# for tc in range(1, T+1):
#     str1 = input()
#     str2 = input()
#     cnt_list = []
#     # str1의 문자를 하나씩 str2와 비교
#     for i in str1:
#         cnt_list.append(str2.count(i))
#     result = max(cnt_list)
#     print(f'#{tc} {result}')
#


# # # 강사님 기출 _ 죄수 판별
# case = input()
# i = 0
# while i < len(case):
#     name = ""
#     while i < len(case) and case[i].isalpha():
#         name += case[i]
#         i += 1
#     number = ""
#     while i < len(case) and case[i].isdigit():
#         number += case[i]
#         i += 1
#     print(name + '#' + str(int(number) + 17))


# # 강사님 기출 _ 자동 수학 계산기
# # input = 100+100-50+30
# # print(eval(input())) # 메서드 쓰면 한방에 끝
#
# # eval 메서드 안쓰고 푸는법
# ex = input()
# if ex[0] == '-':
#     ex = '0' + ex
# word = ex.split('+') # 덧셈기호 기준으로 분리
# ans = 0
# for w in word:
#     w = w.split('-') # 뺄셈으로 분리  => 100(+)100(-)50(+)30
#     inner_ans = int(w[0]) # 첫번째 요소는 더해줄 값
#
#     for i in range(1, len(w)): #나머지 요소들은 빼줄값
#         inner_ans -= int(w[i])
#     ans += inner_ans
# print(ans)


# # 강사님 기출 _ 괄호 친구들
# word = input()
# result = 0
# for i in range(len(word)):
#     temp = ''
#     # 현재 검사할 문자의 다음 인덱스
#     index = i + 1
#     if word[i] == '[':
#         while word[index] != ']':
#             # 임시 문자열 temp변수에 현재 문자 추가
#             temp += word[index]
#             index += 1
#         result += int(temp)
#     elif word[i] == '{':
#         while word[index] != '}':
#
#             temp += word[index]
#             index += 1
#         result *= int(temp)
# print(result)


# # 강사님 기출 _ 날짜 경우의 수
#
# word = input()
#
#
# def Date_Calculation(word):
#     Date = word.split('.')
#     result_y = 1
#     result_m = 0
#     result_d = 0
#     year = Date[0]
#     month = Date[1]
#     day = Date[2]
#     # if 'X' in year:
#     #     result_y += 1
#
#     if len(month) == 2:
#         if month[0] == 'X' and month[1] == 'X':
#             result_m += 3
#         elif month[0] == 'X':
#             result_m += 1
#         elif month[1] == 'X':
#             result_m += 10
#         else :
#             result_m += 1
#     if len(month) == 1:
#         if month[0] == 'X':
#             result_m += 9
#
#     if len(day) == 2:
#         if day[0] == 'X' and day[1] == 'X':
#             result_d += 22
#         elif day[0] == 'X' and int(day[1]) <= 1:
#             result_d += 3
#         elif day[0] == 'X' and int(day[1]) > 1:
#             result_d += 2
#         elif day[1] == 'X' and int(day[0]) == 3:
#             result_d += 2
#         elif day[1] == 'X' and int(day[0]) < 3:
#             result_d += 10
#         else:
#             result_d += 1
#
#     if len(day) == 1:
#         if day[0] == 'X':
#             result_d += 9
#
#     result = result_d * result_m * result_y
#     return result
#
# Result = Date_Calculation(word)
# print(Result)
#

# # 강사님 기출_ Ok맨
# word = input()
#
# def Ok_man(word):
#     dict = {}
#     No_word = 'bad', 'no', 'puck'
#
#     if word.count('_____') > 1: # 언더바 5개 이상 없음
#         return "Fail"
#
#     for No in No_word: # 조건단어들 없기.
#         if No in word:
#             return "Fail"
#
#     for w in word: # 숫자 없음
#         if w.isdigit():
#             return "fail"
#
#     for w in word:  # 알파벳이 5개를 넘지 않음
#         if w.isalpha(): # 알파벳 여부를 확인
#             if w in dict: # 알파벳이 딕셔너리에 이미 있다면 +1
#                 dict[w] += 1
#             else: # 알파벳이 딕셔너리에 없는 새로운 문자라면 1을 추가해서 딕셔너리에 추가
#                 dict[w] = 1
# s
#     for w, count in dict.items():
#         if count >= 5:
#             return "fail"
#
#     return 'Pass'
#
# result = Ok_man(word)
# print(result)
