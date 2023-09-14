# print(help(list))

# # bash에서 python 파일명.py로 실행하기
# # 밑에 내용이 주르륵 나오면 q를 눌러 탈출.

# string1= 'abc1234acv'
# print(string1.isalpha()) 

# numbers = [1,2,3]
# numbers2 = [4,5,6]
# # print(numbers.append(numbers2))
# # print(numbers.extend(numbers2))
# # 두가지는 원본은 변경하기때문에 None이 출력된다.

# numbers.append(numbers2)
# print(numbers) #[1,2,3,[4,5,6]]
# #or 
# numbers.extend(numbers2)
# print(numbers) #[1,2,3,4,5,6]

# numbers =[1,3,5,4,2,6]
# # sort 메서드 // 정렬 하는 것은 같음.
# print(numbers.sort()) # None
# # sorted 함수 // 반환이 있다. 원본이 바뀌지 않았기때문에 출력 가능
# print(sorted(numbers)) #[1,2,3,4,5,6]
# print(numbers) #[1,3,5,4,2,6]

# numbers =[1,3,5]
# # 1. 할당
# list1 = numbers

# # 2. 슬라이싱
# list2 = numbers[ : ]
# numbers[0] = 100

# print(list1) #[100,3,5] // numbers의 주소를 참조하기 때문에 똑같아 짐
# print(list2) #[1,3,5] //슬라이싱 했기때문에 numbers와는 다른 새로운 주소(복사본)가 생성됌.

# 실습 5-1
# ws_5_1.py

# # 아래 함수를 수정하시오.
# def reverse_string():
#     pass

# result = reverse_string("Hello, World!")
# print(result)
#########
# def reverse_string(string):
#     reverse_name = ''
#     for c in string:
#         reverse_name = c + reverse_name
#     return reverse_name

# result = reverse_string("Hello, World!")
# print(result)

# 실습 5-2
# ws_5_2.py

# 아래 함수를 수정하시오.
# def remove_duplicates():
#     new_lst = []
#     pass

#     return new_lst

# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(result)

# def remove_duplicates(old_lst):
#     new_lst = []
#     new_lst=list(set(old_lst))

#     return new_lst
####################
# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(result)

# 실습 5-3
# ws_5_3.py

# 아래 함수를 수정하시오.
# def sort_tuple():
#   new_tuple = ()
#   pass
#   return new_tuple

# result = sort_tuple((5, 2, 8, 1, 3))
# print(result)
####################
# def sort_tuple(numbers):
#   new_tuple = ()
#   new_tuple = tuple(sorted(numbers))
#   return new_tuple

# result = sort_tuple((5, 2, 8, 1, 3))
# print(result)

# 실습 5-4
# ws_5_4.py

# # 아래 함수를 수정하시오.
# def capitalize_words(sentence):
#     result1 = sentence.split(',')
#     result2 = result1.capitalize()
#     result3 = ', '.join(result2)
    
#     return result3
    
#########################
# # 아래 함수를 수정하시오.
# def capitalize_words(sentence):
#     Result = "" # 결과 값 표현을 하기 위한 변수 선언
#     SplitT = sentence.split(" ")
#     for i in SplitT: # 나누어진 단어들 루프 돌기
#         i = i.capitalize() #각 단어 앞글자 대문자로 변경
#         Result += i + ' '
    
#     return Result

# result = capitalize_words("hello, world!")
# print(result)

# 실습5-5
# ws_5_5.py

# 아래 함수를 수정하시오.
# def even_elements():
    

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = even_elements(my_list)
# print(result)
####################
# def even_elements(lst):
#     even_list = []
#     list_length = len(lst)
#     for i in range(list_length-1, -1, -1):
#         last_element = lst.pop()

#         if last_element % 2 == 0:
            
#             even_list.extend([last_element])
#     return sorted(even_list)
    
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = even_elements((my_list))
# print(result)

# 실전 5-2
# main.py

# 아래 함수를 수정하시오.
# def count_character(text, ):
    

# result = count_character("Hello, World!", "o")
# print(result) # 2
###################
# def count_character(text, x):
#     count = text.count(x)
#     return count
# result = count_character("Hello, World!", "o")
# print(result) 

# # 실전5- 3
# # main.py

# # 아래 함수를 수정하시오.
# def find_min_max():
#     pass

# result = find_min_max([3, 1, 7, 2, 5])
# print(result) # (1, 7)
####################
# def find_min_max(lst):
#     a = max(lst)
#     b = min(lst)
#     return (b, a)

# result = find_min_max([3, 1, 7, 2, 5])
# print(result) # (1, 7)

#############################################

# a= "practice makes perfect"

# #1. 문자열 a에서 'e의 갯수세기
# print(a.count('e'))
# #2. 문자열 a에서 'i'의 위치찾기 (2가지)
# print(a.index('i')) # 'i'가 존재하지 않으면 에러
# print(a.find('i')) # 'i가 존재하지 않으면 -1 리턴 // 보통 문제에서 이거 많이씀!!
# #3. 문자열a 의 문자사에이 .(점) 삽입
# print('.'.join(a))
# #4  문자열 a를 공백 기준으로 분리하여 출력 -> 리시트로 출력
# print(a.split())
# #5  문자열 a에서 ' makes'를 'made'로 바꿔서 출력
# print(a.replace('makes','made'))
# #6 문자열 a를 대문자와 소문자로 변환하여 출력
# print(a.upper())
# print(a.lower())
# #7 문자열 a에서 양쪽 공백 삭게하기
# print(a.strip())

# # 더 궁금하면 ctrl누르고 메서드 클릭하기   

# # 대문자 A의 아스키코드 56
# # 소문자 a의 아스키코드 64

# # 문자 분리 하기.
# C =input().split('-')
# print(C)

# # 리스트 메서드 실습
# a = ['b','a','n','a','n']
# # 반환하지 않는 메서드 = 원본은 변경
# #1. 리스트 a의 마지막에 'a'추가하기
# a.append('a')
# print(a)
# #2. 리스트 a를 오름차순으로 정렬. a출력(원본변경)
# a.sort()
# print(a)
# #2-1. 오름차순 정렬 (원본변경x)
# print(sorted(a))
# #3. 리스트 a를 내림차순으로 정렬. a출력
# a.sort(reverse=True)
# print(a)
# #4. 리스트 a를 역순으로 뒤집기. a출력
# a.reverse()
# print(a)
# #5. 리스트 a에서 문자 'a' 삭제하기. a출력
# a.remove('a')
# print(a)

# # 반환하는 메서드 = 대부분 원본 변경 XX
# #6. 리스트 a의 마지막 요소를 꺼내서 삭제하고 삭제한 요소 출력
# print(a.pop())
# #7. 리스트 a에서 문자 'n'의 개수를 출력
# count = a.count('n')
# print(count)