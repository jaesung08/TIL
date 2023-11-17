from rest_framework import generics, status
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Article, Comment
from .serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

## 좋아요
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def like_post(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    user = request.user
    
    if article.likes.filter(username=user).exists():
        article.likes.remove(user)
        return Response({"message": "Liked remove successfully"}, status=status.HTTP_201_CREATED)
    else:
        article.likes.add(user)
        return Response({"message": "Article liked successfully"}, status=status.HTTP_201_CREATED)
    
## 댓글 작성 및 조회
@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = Comment.objects.filter(article=article)

    if request.method == 'GET':
        
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        
        comments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            article = get_object_or_404(Article, pk=article_pk)
            serializer.save(user=request.user, article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



## 게시글 리스트 및 게시글 detail

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    
    elif request.method == 'POST':
        # authentication_classes = [BasicAuthentication, SessionAuthentication]
        # # permission 추가
        # permission_classes = [IsAuthenticatedOrReadOnly]
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        # 조회수 추가 시키기
        article.views += 1
        article.save()
        
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        #partial : 일부 데이터를 수정하기 위해 사용
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BA)