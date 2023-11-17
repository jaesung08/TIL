from .models import Article, Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # 조회는 괜찮은데, 생성할 때는 해당필드는 빼고 생각하도록
        read_only_fields = ('article', )


# 전체 데이터에 대한 serializer
class ArticleListSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source='likes.count')
    
    # 댓글수 추가 
    comments_count = serializers.IntegerField(source='comment_set.count')
    class Meta:
        model = Article
        fields = '__all__'


# 상세 데이터에 대한 serializer
class ArticleSerializer(serializers.ModelSerializer):
    # likes = serializers.ManyRelatedField(source='likes', many=True)
    # Comment 내용 포함시키기
    # 1. Commentserializer 활용하기
    comment_set = CommentSerializer(many= True, read_only = True)

    # 2. 각 필드를 재정의
    # 필드명은 자유롭게 구성
    # primaryKeyRelatedField: 참조하는 테이블의 PK
    comment_id = serializers.PrimaryKeyRelatedField(source='comment_set', many=True, read_only=True)
    coment_content = serializers.StringRelatedField(source='comment_set', many=True, read_only=True)

    # 3. serializerMethodField

    comments = serializers.SerializerMethodField()
    # 자동으로 get_comments 메소드를 호출한다.
    # obj : instance
    def get_comments(self, obj):
        comments = obj.comment_set.all()
        return [{
            'id' : comment.id,
            'content':comment.content
        } for comment in comments ]

    class Meta:
        model = Article
        # all: 전체필드
        # => 역참조시 필요로 하는 'comment_set'도 포함되어있다
        fields = '__all__'
