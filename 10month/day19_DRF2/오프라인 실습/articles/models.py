from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)


class Article(models.Model):
    # M:N 관계 실습해보기
    topics = models.ManyToManyField(Topic, blank =True, null=True)

    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 상세 페이지 구분을 위한 조회수
    # 조회수는 상세페이지에서만 조회 가능하다 가정
    views = models.IntegerField(default=0)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # override
    # __str__ class호출시 자동으로 호출되는 매직 메서드
    # 아래와 같이 오버라이딩하면 comment를 볼 수 있다
    def __str__(self):
        return self.content