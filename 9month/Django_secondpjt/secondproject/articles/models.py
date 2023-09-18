from django.db import models

# Create your models here.
class Article(models.Model):
    # 데이터 베이스에서 열(column) => 필드, 행(row) => 레코드
    # 엑셀도 DB? 스키마구조, 테이블구조로 형식은 같으나 보안성이 없기때문에 DB라 할수 없다.
    # CharField: 길이 제한이 있는 문자열을 저장하는 필드를 생성 
    # TextField: 글자수가 많을 때 사용 = > 긴 텍스트 정보를 저장하는 필드를 생성
    title = models.CharField(max_length=10)
    content = models.TextField()
    # DateTimeField: 날짜와 시간정보를 함께 저장하는 필드를 생성
    # auto_now_add: 처음 데이터가 생성될 때의 날짜와 시간을 자동으로 저장
    # auto_now: 데이터가 수정될 때 마다 날짜와 시간을 자동으로 업데이트하여 저장
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)