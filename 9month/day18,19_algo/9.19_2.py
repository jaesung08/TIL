# # 연습문제 3 트리 순회
# arr = {1, 2, 1, 3, 2, 4, 3, 5, 3, 6}
#
#
# # 0. 이진 트리 저장
# #    - 일차원 배열 저장
# # 왼쪽 = N * 2 + 1
# # 오른쪽 = N * 2 + 2
# # 1. 연결 리스트로 저장
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#     # 삽입 함수
#     def insert(self, childNode):
#         # 왼쪽 자식이 없을 경우
#         if not self.left:
#             self.left = childNode
#             return
#         # 오른쪽 자식이 없을 경우
#         if not self.right:
#             self.right = childNode
#             return
#
#         return
#
#
# # 2. 인접 리스트로 저장
#
# # 이진트리 만들기
# nodes = [TreeNode(i) for i in range(1, 7)]
# for i in range(0, len(arr), 2):
#     parentNode = arr[i]
#     childNode = arr[i + 1]
#     nodes[parentNode].insert(nodes[childNode])
#     nodes[childNode].append(parentNode)


