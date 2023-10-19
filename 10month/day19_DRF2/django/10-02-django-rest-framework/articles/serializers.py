from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):
    class ArticletitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title', )
    # override
    # article을 추가하는 순간 read_only_fields 가 먹히기 때문에 
    # read_only = True를 내부에 추가해준다.
    article = ArticletitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # 위에 article이라는 내부 변수가 생겨서 먹히기 때문에 사용불가
        # read_only_fields = ('article', )



class ArticleSerializer(serializers.ModelSerializer):
    # comment 는 다중 데이터이기에 many 작성
    # 댓글은 불러오기만 하면 되기때문에 read_only도 작성
    # comment_set = CommentSerializer(many=True, read_only=True)
    
    # models.py 에서 related_name을 바꾸면 바꾼 이름으로 새로 사용
    comments =CommentSerializer(many=True, read_only=True)
    # 만약 댓글의 내용 중 일부만 출력하고 싶다면 위의 commentserializer에서
    # 안에서 새롭게 정의한거처럼 정의해주어야 함
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


