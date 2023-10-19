from rest_framework import serializers
from .models import Article, Comment, Topic

# serializer 는 Queryset 요청을 json으로 바꿔주기 위해 씀

# serialziers.Serializer 
# serialziers.ModelSerializer 
# 폼과 모델폼의 차이와 같다 
# 폼은 일반적인 웹 양식을 생성하고 처리하는 데 사용되며, 
# 모델 폼은 데이터베이스 모델과 관련된 입력 폼을 자동으로 생성하고 
# 데이터베이스 연동을 간편하게 만들어줌


# 전체, 상세 데이터 조작시 사용되는 필드가 동일하기 때문에 
# 댓글 serializer는 하나만 생성
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # 조회는 괜찮은데, 생성할 때는 해당필드는 빼고 생각하도록
        read_only_fields = ('article', )



class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


# 전체 데이터에 대한 serializer
class ArticleListSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many = True, read_only = True)
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'topics', )


# 상세 데이터에 대한 serializer
class ArticleSerializer(serializers.ModelSerializer):
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

