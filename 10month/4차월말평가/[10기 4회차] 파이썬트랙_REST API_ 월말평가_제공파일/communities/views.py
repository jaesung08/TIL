from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Book, Review
from .serializers import (
    BookSerializer,
    BookListSerializer,
    BookDetailSerializer,
    ReviewSerializer,
    ReviewCreateSerializer,
    ReviewListSerializer,
    ReviewUpdateSerializer
)


@api_view(['GET', 'POST'])
def books(request):
    if request.method == 'GET':
        book_list = get_list_or_404(Book)
        serializer = BookListSerializer(book_list, many=True)
        return Response(serializer.data)
    
    # 문제 02. 책 정보를 생성 후 생성한 책의 data와 적절한 status code 를 응답하도록 수정하기 
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# 문제 04. 책 정보를 수정할 수 있도록 코드를 수정하기
@api_view(['GET', 'DELETE'])
def book_one(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    
    if request.method == 'GET':
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    # 문제 05. 삭제 후 200 status coder가 아닌 적절한 status 코드 리턴하기
    elif request.method == 'DELETE':
        book.delete()
        return Response({'msg': f'{book_pk}번 책 삭제'})
    

@api_view(['GET', 'POST'])
def reviews(request, book_pk):
    # 문제 06. 잘못된 pk 로 요청했을 경우 404 에러를 리턴할 수 있도록 코드 수정하기
    book = Book.objects.get(pk=book_pk)

    if request.method == 'GET':
        # 문제 07. 전체 Review List 가 아닌 
        # variable routing 으로 전달되는 book_pk에 작성된 Review List 를 볼 수 있도록 수정하기
        review_list = Review.objects.all()
        serializer = ReviewListSerializer(review_list, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(book=book)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_one(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    # 문제 09. 리뷰의 디테일 페이지를 html 형식이 아닌 JSON 으로 리턴하기
    #          (ReviewSerializer를 이용한다.)
    if request.method == 'GET':
        context = {
            'review': review
        }
        return render(request, 'communities/detail.html', context)
    
    # 문제 10. 유효성 검사를 통과하지 못했을 때 400 에러가 발생되도록 수정하기
    elif request.method == 'PUT':
        serializer = ReviewUpdateSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response({'msg': f'{review_pk}번 리뷰 삭제'}, status=status.HTTP_204_NO_CONTENT)
