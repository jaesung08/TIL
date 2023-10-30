from rest_framework import serializers
from .models import Book, Review



##### Review Seriazlier

# Review : Read (List)
# ReviewListSerializer 수정 금지
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['comment',]


# Review : Create
# 문제 08. book 필드가 유효성 검사에 의해 확인되지 않도록 읽기 전용으로 설정하기
class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


# Review : Read (Detail)
# ReviewSerializer 수정 금지
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


# Review : Update
# ReviewUpdateSerializer 수정 금지
class ReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'comment',]



#### Book Serializer

# Book : Read (List)
# 문제 01. 책의 제목(title)만 출력될 수 있도록 fields 수정하기
class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


# Book : Create, Update
# BookSerializer 수정 금지
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


# Book : Read (Detail)
# 문제 03. 해당 책에 달린 리뷰의 개수(review_count) 필드를 추가하기
#         (필드 명은 반드시 review_count 로 작성)
class BookDetailSerializer(serializers.ModelSerializer):
    review_set = ReviewListSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

