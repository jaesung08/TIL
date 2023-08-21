# # pop
# my_set = {1, 2, 3}
# element = my_set.pop( )

# print(element) # 1
# print(my_set) # {2, 3}

# # 딕셔너리 매서드
# my_dict = { 'name' : 'Alice', 'age' : 25}
# # print(my_dict['name'])
# # print(my_dict.get('name'))

# # #찾고자하는 키가 없을때
# # # print(my_dict['country']) # key Error
# # print(my_dict.get('country')) # None
# # print(my_dict.get('country', 'Unknown')) # Unknown

# print(my_dict.keys())
# for key in my_dict.keys():
#     print(key)

# # items
# person = { 'name' : 'Alice', 'age' : 25}

# print(person.items()) # dict_items([('name','Alice') , ('age', 25 )])
# for k, v in person.items():
#     print(k, v)
# '''
# name Alice
# age 25
# '''

# #setdefault
# person = { 'name' : 'Alice', 'age' : 25}

# print(person.setdefault('country','KOREA')) # KOREA
# print(person) #  { 'name' : 'Alice', 'age' : 25, 'country' : 'KOREA' }

# # 비슷한 유형 연습

# blood_types = ['A','B','A','O','AB','AB','O','A','B','O','B','AB']

# # []
# new_dict = {}
# for blood_type in blood_types : # blood_type을 순회
#     if blood_type in new_dict : # 기존에 키가 존재한다면
#         new_dict[blood_type] +=1 # 기존에 키의 값을 1 증가
#     else :                      #
#         new_dict[blood_type] = 1 # 키가 존재하지않는다면
# print(new_dict)


# # .get()
# new_dict = {}
# for blood_type in blood_types : # blood_type을 순회
#     new_dict[blood_type] = new_dict.get(blood_type, 0) +1
# print(new_dict)

# # .setdefault()
# new_dict = {}
# for blood_type in blood_types : # blood_type을 순회
#     new_dict.setdefault(blood_type, 0)
#     new_dict[blood_type] += 1
# print(new_dict)


# # 얕은복사
# a=[1,2,3]
# # 슬라이싱
# b = a[:]
# b[0] = 100
# print(a,b) # [1,2,3] [100,2,3]

# # copy
# c = a.copy()
# c[0] = 100
# print(a,c) # [1,2,3] [100,2,3]

# # 얕은복사의 한계
# # 슬라이싱
# a= [1,2,[1,2]]

# b= a[:]
# b[2][0] = 999
# print(a,b) # [1, 2, [999, 2]] [1, 2, [999, 2]]

# # copy
# c = a.copy()
# c[2][0] = 999
# print(a,c) # [1, 2, [999, 2]] [1, 2, [999, 2]]


# # 깊은복사
# import copy

# original_list = [1,2,[1,2]]
# deep_copied_list = copy.deepcopy(original_list)

# deep_copied_list[2][0] = 999
# print(original_list, deep_copied_list) #[1, 2, [1, 2]] [1, 2, [999, 2]]


# # SET = 가변형 비시퀀스(중복x) = 집합과 같은 특징
# list1 = [1, 2, 3]
# list2 = [4, 5, 6, 7, 8, 9]
# set1 = set(list1)
# set2 = set(list2)

# #1. set1에 4추가
# set1.add(4)
# print(set1)
# #2. set1에 5,6,7 추가
# set1.update([5,6,7])
# print(set1)
# #3. set1에 7제거 (2가지 방법)
# set1.remove(7)
# print(set1)
# set1.discard(7)
# print(set1)
# #4. set1 차집합 set2 출력(2가지 방법)
# print(set1-set2)
# print(set1.difference(set2))
# #5. set1 교집합 set2 출력(2가지 방법)
# print(set1&set2)
# print(set1.intersection(set2))
# #6. set1 합집합 set2 출력(2가지 방법)
# print(set1|set2)
# print(set1.union(set2))

# # set1.pop() => 주소값이 작은 것 부터 제거
# print(id(1))
# print(id(2))
# print(id(3))
# print(id(4))
# print(set1.pop())
# print(set1.pop())
# print(set1.pop())
# print(set1.pop())
# print(set1)

# # 딕셔너리 영한 사전 실습
# my_dict = {
#     'plus':['더하기','장점'],
#     'minus':['빼기','적자'],
#     'multiply':['곱하기','다양하게'],
#     'division':['나누기','분열']
# }
# #1. 영어단어를 입력하면 단어의 뜻을 보여주는 프로그램 (2가지 방법)
# print(my_dict.get(input()))
# print(my_dict.setdefault(input()))
# print(my_dict[input()])
# #2. 영한사전에서 단어들의 목록을 출력
# print(my_dict.keys())
# for k in my_dict.keys():
#     print(k)
# # 3. 다음 단어와 뜻을 추가하고, 사전에 있는 모든 단어와 뜻을 출력(3가지 방법)
# # square, 제곱,사각형
# new_dict = {'square' : '제곱'}
# my_dict.update(new_dict)
# # or
# my_dict.update(square = '제곱')

# my_dict['square'] = ['제곱','사각형']

# my_dict.setdefault('suqare',['제곱','사각형'])

# print(my_dict)
# print(my_dict.items())

# #4. 입력받은 단어와 뜻을 삭제하는 프로그램 작성(2가지 방법)
# my_dict.pop(input())
# print(my_dict)

# del my_dict[input()]
# print(my_dict)

# ### 혈액형 연습
# blood_types = ['A','B','A','O','AB','AB','O','A','B','O','B','AB']
# #Counter 매서드를 활용하여 실습
# from collections import Counter
# result = Counter(blood_types)
# print(result) # Counter({'A': 3, 'B': 3, 'O': 3, 'AB': 3})

# # 할당, 얕은복사, 깊은복사
# # 불변 데이터 원본 변경 X, 가변데이터
# #1. 할당 : 원본 데이터 변경 O
# list1 = [1, 2, 3, 4]
# list2 = list1
# list2[0] = 5

# print(id(list1), id(list2))
# print(list1, list2)

# #2. 얕은 복사
# a= [1,2,[1,2]]

# b= a[:]
# b[2][0] = 999
# b[0] = 5
# print(a,b) # [1, 2, [999, 2]] [1, 2, [999, 2]]
# print(id(a), id(b))
# print(id(a[2],), id(b[2]))
# # copy
# c = a.copy()
# c[2][0] = 999
# print(a,c) # [1, 2, [999, 2]] [1, 2, [999, 2]]

# #3. 깊은 복사
# import copy

# original_list = [1,2,[3,4]]
# deep_copied_list = copy.deepcopy(original_list)

# deep_copied_list[2][0] = 5
# print(id(original_list), id(deep_copied_list))
# print(id(original_list[2]), id(deep_copied_list[2]))
# print(original_list, deep_copied_list) #[1, 2, [1, 2]] [1, 2, [999, 2]]


# 실습 6-1
# def union_sets(A, B):
#     return A|B

# result = union_sets({1, 2, 3}, {3, 4, 5})
# print(result)

#실습 6-2
# # ws_6_2.py

# # 아래 함수를 수정하시오.
# def get_value_from_dict(D, word):
#     return D.get(word)

# my_dict = {'name': 'Alice', 'age': 25}
# result = get_value_from_dict(my_dict, 'name')
# print(result) # Alice

# #실습 6-3
# # 아래 함수를 수정하시오.
# def intersection_sets(D1,D2):
#     return D1 & D2

# result = intersection_sets({1, 2, 3}, {3, 4, 5})
# print(result) # {3}

# 실습 6-4
# ws_6_4.py

# # 아래 함수를 수정하시오.
# def get_keys_from_dict():
#     pass

# my_dict = {'name': 'Alice', 'age': 25}
# result = get_keys_from_dict(my_dict)
# print(result) #['name', 'age']
# ###########################
# def get_keys_from_dict(D):
#     ND = []
#     for i in D.keys() :
#         ND = ND + [i]
#     return ND

# my_dict = {'name': 'Alice', 'age': 25}
# result = get_keys_from_dict(my_dict)
# print(result)

# 실습 6-5
# ws_6_5.py

# # 아래 함수를 수정하시오.
# def difference_sets(D1, D2):
#     return D1-D2

# result = difference_sets({1, 2, 3}, {3, 4, 5})
# print(result)

# 실전과제 6-2 
# hw_6_2.py

# 아래 함수를 수정하시오.
# def remove_duplicates_to_set():
#     pass

		
# result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
# print(result)
###################
# def remove_duplicates_to_set(Lst):
#     return set(Lst)

		
# result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
# print(result)


# 실전 과제 6-4
# hw_6_4.py

# 아래 함수를 수정하시오.
def add_item_to_dict(dictionary, B, C):
    new_dict = dictionary.copy()
    add_dict = { B : C }
    new_dict.update(add_dict)
    return new_dict

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
